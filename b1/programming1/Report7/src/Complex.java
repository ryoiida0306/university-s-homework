
public class Complex {
	private double Re;
	private double Im;

	Complex(double Re,double Im){
		this.Re = Re;
		this.Im = Im;
	}
	double Re() { return Re;}
	double Im() { return Im;}
	void toStr() { System.out.println(Re+"+"+Im+"i");}
	void add(double x,double y) {
		Re += x;
		Im += y;
	}
	void sub(double x,double y) {
		Re -= x;
		Im -= y;
	}
	void mul(double x,double y) {
		Re *= x;
		Im *= y;
	}
	void dvi(double x,double y) {
		Re /= x;
		Im /= y;
	}
	void conj() { System.out.println(Re+"-"+Im+"i");}
	double abs()  { return Math.sqrt(Re*Re+Im*Im);}
}
