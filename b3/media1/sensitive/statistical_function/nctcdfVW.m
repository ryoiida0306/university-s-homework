function [cdf,details,hplot] = nctcdfVW(x,nu,ncp,tail,nSubs)
%NCTCDFVW Cummulative distribution function (cdf) of the noncentral
%   Student's t-distribution with NU degrees of freedom and noncentrality
%   parameter NCP, cdf = Prob(T_NU(NCP) <= X)
%
%   P = NCTCDFVW(X,NU,NCP) returns the noncentral T cdf with NU
%   degrees of freedom and noncentrality parameter NCP, at the values X.
%
%   The size of P is the common size of the input arguments. A scalar input
%   functions as a constant matrix of the same size as the other inputs.
%
%   Optionally, the upper tail Q = 1 - P = Prob(T_NU(NCP) > X) is
%   evaluated by Q = NCTCDFVW(X,NU,NCP,'UPPER')
%
%   The CDF is computed by the GAUSS-KRONOD (non-adaptive) quadrature over 
%   nSubs sub-intervals. This requires 15*nSubs function evaluations for
%   each computed value of CDF.
%
%   By DEFAULT nSubs = 16 for single evaluation, and nSubs = 6, for 
%   evaluation of vector inputs, which should be sufficient in most cases.
%   Optionally, alternative choice is nSubs = 32, 16, 12, 10, 8, 6, 4, 2.
%
%   Based on preliminary testing the relative error of NCTCDFVW is in most 
%   cases better than 1e-12, possibly worse for some extreme cases.
% 
%   Use the PLOT output as a tool for checking the integrand function and 
%   the used integration limits [A,B].
%
%   In particular:
%
%   If X == 0:
%   Prob(T_NU(NCP) <= X) = NORMCDF(-NCP).
%
%   If X > 0:
%   Prob(T_NU(NCP) <= X ) = NORMCDF(-NCP) +
%               + Integral_{-NCP}^{+INF} (1-CHI2CDF(Q,NU)) * normpdf(Z) dZ,
%   where Q = NU * (Z + NCP)^2 / X^2;
%
%   If X < 0:
%   Prob(T_NU(NCP) <= X) = 1 - Prob(T_NU(-NCP) <= -X).
%
% SYNTAX:
%   [cdf,details,hplot] = nctcdfVW(x,nu,ncp,tail)
%
% EXAMPLE 1. Comparison with TCDF (Statistics Toolbox) for X, NU (NCP = 0)
%   format longe
%   x = 1; nu = 1;
%   [cdfvw,details,~] = nctcdfVW(x,nu)
%   cdf = tcdf(x,nu)
%   relError = abs(cdfvw-cdf)/cdfvw
%   disp([cdfvw cdf relError])
%
% EXAMPLE 2. Comparison with NCTCDF (Statistics Toolbox), small X, NU, NCP:
%   x = 1; nu = 15; ncp = 4; tail = 'lower'; nSubs = 6;
%   [cdfvw,details,handle] = nctcdfVW(x,nu,ncp,tail,nSubs)
%   cdf = nctcdf(x,nu,ncp)
%   relError = abs(cdfvw-cdf)/cdfvw
%   disp([cdfvw cdf relError])
%
% EXAMPLE 3. Comparison with NCTCDF, large X, NU, NCP:
%   x = 500; nu = 1000; ncp = 600;  
%   [cdfvw,details,~] = nctcdfVW(x,nu,ncp)
%   cdf = nctcdf(x,nu,ncp)
%   relError = abs(cdfvw-cdf)/cdfvw
%   disp([cdfvw cdf relError])
%
% EXAMPLE 4. Comparison with NCTCDF, vector X, NU, NCP:
%   x = (550:650)'; nu = 15; ncp = 600; tail = 'lower'; nSubs = 8;
%   tic; [cdfvw,details] = nctcdfVW(x,nu,ncp,tail,nSubs); toc
%   tic; cdf = nctcdf(x,nu,ncp); toc
%   relError = abs(cdfvw-cdf)./cdfvw;
%   disp([cdfvw cdf relError])
%
% REFERENCES:
%  [1]  Witkovsky V. (2013). A Note on Computing Extreme Tail
%       Probabilities of the Noncentral T Distribution with Large
%       Noncentrality Parameter. Working Paper, Institute of Measurement
%       Science, Slovak Academy of Sciences, Bratislava.

% Handmade in EU by using ecologically sustainable code
% (c) Viktor Witkovsky (witkovsky@savba.sk)
% Ver.: 05-Jun-2013 08:01:48

%% CHECK INPUTS AND OUTPUTS

narginchk(2, 5);
if nargin < 5, nSubs = []; end
if nargin < 4, tail = []; end
if nargin < 3, ncp = []; end

% SET THE DEFAULT VALUES (input parameters)
if isempty(ncp), ncp = 0; end
if isempty(tail), tail = 'lower'; end

if isempty(nSubs)
    if length(x) == 1
        nSubs = 16;
    else
        nSubs = 6;
    end
end

x = x(:); nu = nu(:); ncp = ncp(:);

%[errorcode,x,nu,ncp] = distchck(3,x,nu,ncp);
%if errorcode > 0
%    error(message('VW:nctcdfVW:InputSizeMismatch'));
%end

% INITIALIZE THE OUTPUT
if isa(x,'single') || isa(nu,'single') || isa(ncp,'single')
    cdf = zeros(size(x),'single');
else
    cdf = zeros(size(x));
end
cdfLower = cdf;
cdfUpper = cdf;

if nargout > 1
    details.x = x;
    details.nu = nu;
    details.ncp = ncp;
    details.cdf_lowerTail = [];
    details.cdf_upperTail = [];
    details.cdf_computed = [];
    details.tail_computed = [];
    details.gammatail_computed = [];
    details.error_upperBound = [];
    details.integration_limits = [];
    details.n_subintervals = [];
    details.method = 'Non-Adaptive-Gauss-Kronod-Quadrature';
end

if nargout > 2
    hplot = [];
end

%% ALGORITHM

todo = true(size(x));
isLowerTail = todo; isLowerGamma = todo;
A = NaN(size(x)); B = A;
ErrBnd = A;
Z = [];

% SPECIAL CASES (nu <=0, x = -Inf, x = 0, x = Inf)
[cdf,isLowerTail,todo] = specialcases(x,nu,ncp,cdf,isLowerTail,todo);

if any(todo)
    % TRANSFORM  (negative  x  < 0  to non-negative x >= 0)
    neg = (todo & (x < 0)); pos = (todo & (x >= 0));
    
    if any(neg)
        x(neg) = -x(neg);
        ncp(neg) = -ncp(neg);
        [isLowerGamma(neg),isLowerTail(neg)] = ...
            chooseTail(x(neg),ncp(neg),isLowerGamma(neg),...
            isLowerTail(neg),true);
    end
    
    if any(pos)
        [isLowerGamma(pos),isLowerTail(pos)] = ...
            chooseTail(x(pos),ncp(pos),isLowerGamma(pos),...
            isLowerTail(pos),false);
    end
    
    % INTEGRATE (by non-adaptive 'Gauss-Kronod' quadrature)
    [cdf(todo),ErrBnd(todo),A(todo),B(todo),Z,F,nSubs] = ...
        integrate(x(todo),nu(todo),ncp(todo),isLowerGamma(todo),nSubs);
end

%% RESULTS

if nargout > 1
    details.cdf_computed = cdf;
    details.tail_computed = isLowerTail;
    details.gammatail_computed = isLowerGamma;
    details.error_upperBound = ErrBnd;
    details.integration_limits = [A B];
    details.n_subintervals = nSubs;
end

cdfLower(isLowerTail) = cdf(isLowerTail);
cdfLower(~isLowerTail) = 1-cdf(~isLowerTail);
cdfUpper(~isLowerTail) = cdf(~isLowerTail);
cdfUpper(isLowerTail) = 1-cdf(isLowerTail);

switch tail
    case 'lower'
        cdf = cdfLower;
    case 'upper'
        cdf = cdfUpper;
end

if nargout > 1
    details.cdf_lowerTail = cdfLower;
    details.cdf_upperTail = cdfUpper;
end

% PLOT | Tool for checking the (last) integrand FUNC and the limits [A,B]
if (nargout > 2 && ~isempty(Z))
    hplot = plot(Z(:),F(:),'.-');
    xlabel('Z')
    ylabel('FUNC')
    title(['Integrand FUNC evaluated for X = ',num2str(x(end)),...
        ', NU = ',num2str(nu(end)),', NCP = ',num2str(ncp(end)),...
        ' over Z \in [',num2str(A(end)),', ',num2str(B(end)),']'])
end

end
%% FUNCTION SPECIALCASES (NU <= 0,  X == -Inf, X == 0, X == Inf)
function [cdf,isLowerTail,todo]=specialcases(x,nu,ncp,cdf,isLowerTail,todo)
%SPECIALCASES sets exact result for special cases of the input parameters
%    (NU <=0, X == -Inf, X == 0, X == Inf)

% (c) Viktor Witkovsky (witkovsky@savba.sk)
% Ver.: 20-May-2013 01:28:00

nuneg = (nu <= 0);
if any(nuneg)
    cdf(nuneg) = NaN;
    isLowerTail(nuneg) = true;
    todo(nuneg) = false;
end

xinf = (x == Inf);
idx = (xinf & ~nuneg);
if any(idx)
    cdf(idx) = 0;
    isLowerTail(idx) = false;
    todo(idx) = false;
end

xinfneg = (x == -Inf) ;
idx = (xinfneg & ~nuneg);
if any(idx)
    cdf(idx) = 0;
    isLowerTail(idx) = true;
    todo(idx) = false;
end

xzero = (x == 0);
ncppos = (ncp >= 0);
if any(ncppos)
    idx = (xzero & ~nuneg & ncppos);
    % cdf(idx) = 0.5 * erfc(ncp(idx)/sqrt(2));
    cdf(idx) = 0.5 * erfc(ncp(idx)*0.7071067811865475244);
    isLowerTail(idx) = true;
    todo(idx) = false;
end

if any(~ncppos)
    idx = (xzero & ~nuneg & ~ncppos);
    cdf(idx) = 0.5 * erfc(-ncp(idx)*0.7071067811865475244);
    isLowerTail(idx) = false;
    todo(idx) = false;
end

end

%% FUNCTION CHOOSETAIL (Choose the optimum tails for integration)
function [isLowerGamma,isLowerTail] = ...
    chooseTail(x,ncp,isLowerGamma,isLowerTail,neg)
%CHOOSETAIL evaluates the appropriate tails for integration

% (c) Viktor Witkovsky (witkovsky@savba.sk)
% Ver.: 20-May-2013 01:28:00

large = (x >= ncp);
if neg
    if any(large)
        isLowerTail(large) = true;
        isLowerGamma(large) = true;
    end
    if any(~large)
        isLowerTail(~large) = false;
        isLowerGamma(~large) = false;
    end
else
    if any(large)
        isLowerTail(large) = false;
        isLowerGamma(large) = true;
    end
    if any(~large)
        isLowerTail(~large) = true;
        isLowerGamma(~large) = false;
    end
end

end

%% FUNCTION INTEGRATE (Vectorized (G7,K15)-Gauss-Kronod quadrature)
function [CDF,ErrBnd,A,B,Z,F,nSubs] = integrate(x,nu,ncp,isLowerGamma,nSubs)
%INTEGRATE: Evaluates the NCT CDF by vectorized NON-adaptive
%           (G7,K15)-Gauss-Kronod quadrature.
%
%   Based on the algorithm QUADVGK by Adam Wyatt, University of Oxford.
%   http://www.mathworks.com/matlabcentral/fileexchange/18801-quadvgk

% (c) Viktor Witkovsky (witkovsky@savba.sk)
% Ver.: 02-Jun-2013 10:53:03

NF = length(x);
NK = 15;

switch nSubs
    case 32
        SUBIND = 1:NK; NSUB = 32;
    case 16
        SUBIND = 2:2:NK; NSUB = 16;
    case 12
        SUBIND = [4 5 8 11 12]; NSUB = 12;
    case 10
        SUBIND = [4 7 9 12]; NSUB = 10;
    case 8
        SUBIND = [6 8 10]; NSUB = 8;
    case 6
        SUBIND = [6 10]; NSUB = 6;
    case 4
        SUBIND = 8; NSUB = 4;
    case 2
        SUBIND = []; NSUB = 2;
    otherwise
        SUBIND = 2:2:NK; NSUB = 16;
        nSubs = 16;
end

NZ = NSUB*NK;
z = zeros(NF,NZ);
halfw = zeros(NF,NSUB);
CDF = zeros(NF,1);

[A,B,MOD] = limits(x,nu,ncp,isLowerGamma,NF);

% First, evaluate CDF outside the integration limits [A,B], i.e.
% CDF = NORMCDF(A) (for 'upper' gamma tail)
if any(~isLowerGamma)
    CDF(~isLowerGamma) = 0.5*erfc(-A(~isLowerGamma)*0.7071067811865475244);
end

% CDF = 1-NORMCDF(B) (for 'lower' gamma tail)
if any(isLowerGamma)
    CDF(isLowerGamma) = 0.5*erfc(B(isLowerGamma)*0.7071067811865475244);
end

% Second, evaluate CDF by integrating between the limits [A,B] by 
% (G7,K15)-Gauss-Kronod (non-adaptive) quadrature over NSUB subintervals
GKnodes; % [XK,WK,WG,G] = GKnodes;

for id = 1:NF
    Subs = GetSubs([A(id) MOD(id); MOD(id) B(id)],XK);
    GetSubs(Subs,XK);
    z(id,:) = Z(:);
    halfw(id,:) = M;
end

% Evaluate FV - the vectorized integrand function FUNC
func; % FV = func(z,x,nu,ncp,isLowerGamma);

Q1 = zeros(NF, NSUB);
Q2 = zeros(NF, NSUB);
o = ones(1,NSUB);

for id=1:NF
    F = reshape(FV(id,:), NK, []);
    Q1(id,:) = halfw(id,:).*sum((WK*o).*F);
    Q2(id,:) = halfw(id,:).*sum((WG*o).*F(G,:));
end

% Finally, evaluate the CDF and the (conservative) estimate of the
% relative error
CDF = CDF + sum(Q1,2);
ErrBnd = sum(abs(Q1-Q2),2);

%% FUNCTION LIMITS (Compute the integration limits)
    function [A,B,MOD] = limits(x,nu,ncp,isLowerGamma,NF)
    %LIMITS Set the optimum integration limits [A,B].
    %       The approximate limits are derived based on the results by
    %       Tadeusz INGLOT (2010). INEQUALITIES FOR QUANTILES OF THE
    %       CHI-SQUARE DISTRIBUTION. PROBABILITY AND MATHEMATICAL
    %       STATISTICS Vol. 30, Fasc. 2 (2010), pp. 339351.
    %       In particular, based on using the lower bound in Eqn. (3.1)
    %       and CHI2-quantile estimator Eqn. (A.3).

    % (c) Viktor Witkovsky (witkovsky@savba.sk)
    % Ver.: 05-Jun-2013 08:01:48
        
        % const = -(log(2)+log(2*pi)/2);
        const = -1.6120857137646180667900353000732139;
        % logRelTolBnd = log(eps); eps = 2.220446049250313e-16;
        logRelTolBnd = -3.604365338911715e+01;
        % zUppBnd > -norminv(eps(0)) =  3.847234634276879e+01
        zUppBnd =  38.5;
        A = zeros(NF,1); B = A; MOD = A; 
        incpt = [1;1;1];
        
        %tUpp = 3.604365338911715e+01; %tUpp = log(1/eps);
        %tLow = 2.220446049250313e-16; %tLow = log(1/(1-eps)) ~ eps;
        tUpp = 7.208730677823431e+01; % tUpp = log(1/eps^2);
        tLow = 4.930380657631324e-32; % tLow = log(1/(1-eps^2)) ~ eps^2;
             
        for i = 1:NF
            X = x(i); NU = nu(i); NUminus2 = max(1,(NU-2)); NCP = ncp(i);
            
            % Estimate the position of the modus MOD of the FUNC
            MOD(i) = (X*sqrt(4*NU*NUminus2 + X*X*(NCP*NCP+4*NUminus2)) ...
                - NCP*(X*X+2*NU))/(2*(X*X+NU));
            dZ = min(0.5*abs(MOD(i) + NCP),0.01);
            dMOD = [-dZ;0;dZ] + MOD(i);
            q = NU*(dMOD+NCP).*(dMOD+NCP)/(X*X);
            % Estimate the value of log(FUNC) around the MOD point
            logfMOD =  const+0.5*(NUminus2*log(q/NU)+NU-q-dMOD.*dMOD);
            
            % For given logRelTolBnd estimate the logAbsTolBnd
            logAbsTolBnd = logfMOD(2) + logRelTolBnd;
                      
            % Estimate the integration limits by quadratic approximation
            abc = [dMOD.*dMOD dMOD incpt]\logfMOD;
            D = sqrt(abc(2)*abc(2) - 4*abc(1)*(abc(3)- logAbsTolBnd));
            C = 2*abc(1);
            A0 = max(-zUppBnd,-abc(2)/C+D/C);
            B0 = max(-zUppBnd,min(zUppBnd,-abc(2)/C-D/C));
            
            % Find zAbsTolBnd by solving: logAbsTolBnd = log(normpdf(z))
            zAbsTolBnd = min(zUppBnd,sqrt( ...
                -1.8378770664093454835606594728112352-2*logAbsTolBnd));
            
            if isLowerGamma(i)
                % Estimate quantile of chi^2 distribution
                % with NU degrees of freedom, see INGLOT (2010, Eqn. A.3)
                if NU > 1
                    QuantUpp = NU + 2*tUpp + 1.62*sqrt(NU*tUpp) + ...
                        0.63012*sqrt(NU)*log(tUpp) - 1.12032*sqrt(NU) - ...
                        2.48*sqrt(tUpp) - 0.65381*log(tUpp) - 0.22872;
                    QuantUpp = max(0,QuantUpp);
                else
                    QuantUpp = 6.739648382445014e+01;
                end
                zQuantUpp = sqrt((QuantUpp/NU)*X*X)-NCP;
                % Conservative estimate of the upper integration limit B:
                % NORMPDF is sufficiently small OR CHI2CDF is close to 1.
                B(i) = min(zAbsTolBnd,zQuantUpp);
                              
                % For large NU we assume approximate symmetry of FUNC
                if (NU > 1e4 && MOD(i) > -zUppBnd && MOD(i) < zUppBnd) 
                    A0 = MOD(i)-(B(i)-MOD(i));
                end
                A(i) = max(-NCP,A0);
            end
            
            if ~(isLowerGamma(i))
                if NU > 1
                    QuantLow = NU + 2*tLow + 1.62*sqrt(NU*tLow) + ...
                        0.63012*sqrt(NU)*log(tLow) - 1.12032*sqrt(NU) - ...
                        2.48*sqrt(tLow) - 0.65381*log(tLow) - 0.22872;
                    QuantLow = max(0,QuantLow);
                    
                else
                    QuantLow = 0;
                end
                zQuantLow = sqrt((QuantLow/NU)*X*X)-NCP;
                A1 = max(-zAbsTolBnd,zQuantLow);
                A1 = max(-NCP,A1);
                A(i) = A1;
                if (NU > 1e4 && MOD(i) > -zUppBnd && MOD(i) < zUppBnd)
                    B0 = MOD(i)+(MOD(i)-A(i));
                end
                B(i) = B0;
            end
        end
    end

%% FUNCTION FUNC (Integrand function for the Gauss-Kronod quadrature)
    function func % FV = func(z,x,nu,ncp,isLowerGamma);
    %FUNC evaluates the vectorized integrand function
    %        Z is assumed to be a row vector,
    %        X, NU, NCP are assumed to be column vectorss of equal size
    %        isLowerGamma is logical vector (indicator of GAMMAINC tail)
    %        of equal size as X, NU, NCP.
    %
    %       In particular, FUNC evaluates the following function
    %       F = gammainc(Q/2, NU/2, tail) * exp(-0.5 * Z^2) / sqrt(2*pi),
    %       where
    %       Q = NU * (Z + NCP)^2 / X^2.

    % (c) Viktor Witkovsky (witkovsky@savba.sk)
    % Ver.: 20-May-2013 01:28:00
        
        const = 0.398942280401432677939946; % 1/sqrt(2*pi)
        FV = zeros(size(z));
        q = bsxfun(@times,bsxfun(@plus,z,ncp).^2,nu ./ (2*x.*x));
        df = repmat(0.5*nu,1,NZ);
        z2 = -0.5*z.*z;
        
        if any(isLowerGamma)
            FV(isLowerGamma,:) = ...
                gammainc(q(isLowerGamma,:),df(isLowerGamma,:),'lower') ...
                .* exp(z2(isLowerGamma,:)) * const;
        end
        
        if any(~isLowerGamma)
            FV(~isLowerGamma,:) = ...
                gammainc(q(~isLowerGamma,:),df(~isLowerGamma,:),'upper') ...
                .* exp(z2(~isLowerGamma,:)) * const;
        end
        
    end

%% FUNCTION GETSUBS (Sub-division of the integration intervals)
    function SUBS = GetSubs(SUBS,XK) 
    %GETSUBS Sub-division of the integration intervals for adaptive
    %        Gauss-Kronod quadrature
    
    % (c) Viktor Witkovsky (witkovsky@savba.sk)
    % Ver.: 20-May-2013 01:28:00
        
        M = 0.5*(SUBS(2,:)-SUBS(1,:));
        C = 0.5*(SUBS(2,:)+SUBS(1,:));
        Z = XK*M + ones(NK,1)*C;
        
        if nargout > 0
            L = [SUBS(1,:); Z(SUBIND,:)];
            U = [Z(SUBIND,:); SUBS(2,:)];
            SUBS = [reshape(L, 1, []); reshape(U, 1, [])];
        end
        
    end

%% FUNCTION GKNODES (Gauss-Kronod nodes and weights)
    function GKnodes    % [XK,WK,WG,G] = GKnodes
    %GKNODES The (7-15) Gauss-Kronod nodes and weights
    
    % (c) Viktor Witkovsky (witkovsky@savba.sk)
    % Ver.: 20-May-2013 01:28:00
        
        nodes = [ ...
            0.2077849550078984676006894; 0.4058451513773971669066064; ...
            0.5860872354676911302941448; 0.7415311855993944398638648;...
            0.8648644233597690727897128; 0.9491079123427585245261897; ...
            0.9914553711208126392068547];
        wt = [ ...
            0.2044329400752988924141620; 0.1903505780647854099132564; ...
            0.1690047266392679028265834; 0.1406532597155259187451896;
            0.1047900103222501838398763; 0.0630920926299785532907007;...
            0.0229353220105292249637320];
        wt7 = [0.3818300505051189449503698; ...
            0.2797053914892766679014678; 0.1294849661688696932706114];
        
        XK = [-nodes(end:-1:1); 0; nodes];
        WK = [wt(end:-1:1); 0.2094821410847278280129992; wt];
        WG = [wt7(end:-1:1); 0.4179591836734693877551020; wt7];
        G = (2:2:15)';
        
    end

end
