package othello6;

import java.util.*;

public class Move {
    public final static Move PASS = new Move(null, Board.NONE);

    public Position square;
    public int color;

    public Move(Position square, int color) {
        this.square = square;
        this.color = color;
    }

    public int hashCode() {
        return Objects.hash(this.square, this.color);
    }

    public boolean equals(Object obj) {
        if (this == obj)
            return true;
        if (obj == null)
            return false;
        if (getClass() != obj.getClass())
            return false;
        Move other = (Move) obj;
        return Objects.equals(this.square, other.square) && this.color == other.color;
    }

    public String toString() {
        return isPass() ? "pass" : this.square.toString();
    }

    public boolean isPass() {
        return (this.square == null);
    }
}