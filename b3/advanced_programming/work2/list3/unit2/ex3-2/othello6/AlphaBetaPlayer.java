package othello6;

import java.util.*;
import othello6.*;

public class AlphaBetaPlayer extends Player {
    Eval eval;
    int depthLimit;
    Move move;

    public AlphaBetaPlayer(int color) {
        this("AB", color, new Eval(), Integer.MAX_VALUE);
    }

    public AlphaBetaPlayer(String name, int color, Eval eval, int depthLimit) {
        super(name, color);
        this.eval = eval;
        this.depthLimit = depthLimit;
    }

    public AlphaBetaPlayer(String name, int color, int depthLimit) {
        this(name, color, new Eval(), depthLimit);
    }

    protected Move search(World world) {
        this.move = null;
        maxSearch(world, Float.NEGATIVE_INFINITY, Float.POSITIVE_INFINITY, 0);
        return this.move;
    }

    float maxSearch(World world, float alpha, float beta, int depth) {
        if (isTerminal(world, depth))
            return this.eval.value(world);

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
            return this.eval.value(world);

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
}