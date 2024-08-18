package othello6;

import java.util.*;
import othello6.*;

public class EX38AlphaBetaPlayer extends Player {
    Eval eval;
    int depthLimit;
    Move move;

    public EX38AlphaBetaPlayer(int color) {
        this("AB", color, new Eval(), Integer.MAX_VALUE);
    }

    public EX38AlphaBetaPlayer(String name, int color, Eval eval, int depthLimit) {
        super(name, color);
        this.eval = eval;
        if(depthLimit > 4){
            this.depthLimit = 4;
        }else{
            this.depthLimit = depthLimit;
        }
    }

    public EX38AlphaBetaPlayer(String name, int color, int depthLimit) {
        this(name, color, new Eval(), depthLimit);
    }

    protected Move search(World world) {
        this.move = null;
        if(world.lastTurn != World.NONE ){
            // maxSearch(world, Float.NEGATIVE_INFINITY, Float.POSITIVE_INFINITY, 0);
            NegaMaxSearch(world,Float.POSITIVE_INFINITY, Float.POSITIVE_INFINITY,0);
        }else{
            randomSearch(world);
        }
        return this.move;
    }

    void randomSearch(World world){
        Random random = new Random();
        var moves = world.getLegalMoves();
        this.move = moves.get(random.nextInt(moves.size()-1));
    }

    float NegaMaxSearch(World world, float alpha, float beta, int depth){
        if(isTerminal(world, depth)){
            return this.eval(world);
        }

        var moves = world.getLegalMoves();
        if(moves.isEmpty()){
            moves.add(Move.PASS);
        }

        for(Move move : moves){
            World newWorld = world.perform(move);
            float v = -1*NegaMaxSearch(newWorld, alpha, beta, depth+1);
            if(alpha > v){
                alpha = v;
                if(depth == 0){
                    this.move = move;
                }
            }
            if(beta > v){
                beta = v;
                if(depth == 0){
                    this.move = move;
                }
            }
            if(beta>=-alpha){break;}
        }
        if(depth%2 == 0){return alpha;}
        else{return beta;}

    }


    float maxSearch(World world, float alpha, float beta, int depth) {
        if (isTerminal(world, depth))
            // return this.eval.value(world);
            return this.eval(world);

        var moves = world.getLegalMoves();
        if (moves.isEmpty())
            moves.add(Move.PASS);

        moves = order(moves);

        for (Move move : moves) {
            World newWorld = world.perform(move);
            float v = minSearch(newWorld, alpha, beta, depth + 1);

            if (v > alpha) {
                alpha = v;
                if (depth == 0)
                    this.move = move;
            }
            if (alpha >= beta)
                break;
        }

        return alpha;
    }

    float minSearch(World world, float alpha, float beta, int depth) {
        if (isTerminal(world, depth))
            // return this.eval.value(world);
            return this.eval(world);

        var moves = world.getLegalMoves();
        if (moves.isEmpty())
            moves.add(Move.PASS);

        moves = order(moves);

        for (Move move : moves) {
            World newWorld = world.perform(move);
            float v = maxSearch(newWorld, alpha, beta, depth + 1);
            beta = Math.min(beta, v);
            if (alpha >= beta)
                break;
        }

        return beta;
    }

    boolean isTerminal(World world, int depth) {
        return world.isGoal() || depth > this.depthLimit;
    }

    List<Move> order(List<Move> moves) {
        Collections.shuffle(moves);
        return moves;
    }

    float eval(World world){
        int Lblack;
        int Lwhite;
        int Nblack;
        int Nwhite;
        
        Nblack = world.getBoard().getCount(World.BLACK);
        Nwhite = world.getBoard().getCount(World.WHITE);

        if(world.getNextTurn() == World.BLACK){
            Lblack = world.getLegalMoves().size();
            world = world.perform(Move.PASS);
            Lwhite = world.getLegalMoves().size();
        }else{
            Lwhite = world.getLegalMoves().size();
            world = world.perform(Move.PASS);
            Lblack = world.getLegalMoves().size();
        }

        // System.out.println("Lblack = "+Lblack);
        // System.out.println("Lwhite = "+Lwhite);
        // System.out.println("Nblack = "+Nblack);
        // System.out.println("Nwhite = "+Nwhite);

        float w1;
        float w2;
        float w3;
        float w4;
        float w5;

        int N = world.getBoard().getCount(World.BLACK)+world.getBoard().getCount(World.WHITE)-4;

        if(N<8){//first tractice
            w1 = 1;
            w2 = 0;
            w3 = 0;
            w4 = 0;
            w5 = 0;
        }else if(N<21){//second tractice
            w1 = 1;
            w2 = 0;
            w3 = 0;
            w4 = 0;
            w5 = 0;
        }else{//tired tractice
            w1 = 1;
            w2 = 0;
            w3 = 0;
            w4 = 0;
            w5 = 0;
        }

        return w1*this.eval.value(world)+w2*Lblack+w3*Lwhite+w4*Nblack+w5*Nwhite;
    }
}