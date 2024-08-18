package othello6;

import java.util.*;

public class World implements Cloneable {
    public final static int BLACK = Board.BLACK;
    public final static int WHITE = Board.WHITE;
    public final static int NONE = Board.NONE;

    Board board;

    int lastTurn = NONE;
    Move lastMove;

    public World() {
        this.board = new Board();
        this.getBoard().init();
    }

    public World(World world) {
        this.lastTurn = world.lastTurn;
        this.lastMove = world.getLastMove();
        this.board = world.getBoard().clone();
    }

    public Board getBoard() {
        return this.board;
    }

    public Move getLastMove() {
        return this.lastMove;
    }

    public String toString() {
        return this.getBoard().toString();
    }

    public boolean equals(Object otherObj) {
        if (otherObj instanceof World) {
            World other = (World) otherObj;
            return this.getBoard().equals(other.getBoard());
        }
        return false;
    }

    public World clone() {
        World other = new World();
        other.lastTurn = this.lastTurn;
        other.lastMove = this.getLastMove();
        other.board = this.getBoard().clone();
        return other;
    }

    public boolean isGoal() {
        return this.getBoard().getLegalMoves(BLACK).size() == 0 &&
                this.getBoard().getLegalMoves(WHITE).size() == 0;
    }

    public World perform(Move move) {
        World newWorld = new World(this);
        newWorld.lastTurn = getNextTurn();
        newWorld.lastMove = move;
        if (move.isPass())
            newWorld.getBoard().pass();
        else
            newWorld.getBoard().place(move);
        return newWorld;
    }

    boolean isValid() {
        return true;
    }

    public List<Move> getLegalMoves() {
        return this.getBoard().getLegalMoves(getNextTurn());
    }

    public int getScore() {
        return this.getBoard().getCount(BLACK) - this.getBoard().getCount(WHITE);
    }

    public int getWinner() {
        int score = this.getScore();
        return score == 0 ? NONE : (score > 0 ? BLACK : WHITE);
    }

    public int getPrevTurn() {
        return this.lastTurn;
    }

    public int getNextTurn() {
        return this.lastTurn == NONE ? BLACK : -this.lastTurn;
    }

    public void flip() {
        this.lastTurn *= -1;
        this.getBoard().flip();
    }
}
