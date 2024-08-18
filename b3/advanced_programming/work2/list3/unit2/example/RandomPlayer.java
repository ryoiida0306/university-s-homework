package example;

import java.util.*;

import othello6.*;

public class RandomPlayer extends Player {
    public RandomPlayer(int color) {
        super("R", color);
    }

    protected Move search(World world) {
        var moves = world.getLegalMoves();
        if (moves.isEmpty())
            return Move.PASS;
        int index = new Random().nextInt(moves.size());
        return moves.get(index);
    }
}