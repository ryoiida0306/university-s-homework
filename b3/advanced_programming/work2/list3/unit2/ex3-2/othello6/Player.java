package othello6;

public class Player {
    static float POSITIVE_INFINITY = Float.POSITIVE_INFINITY;
    static float NEGATIVE_INFINITY = Float.NEGATIVE_INFINITY;

    protected String name;
    protected int color;

    public Player(int color) {
        this("----", color);
    }

    public Player(String name, int color) {
        this.name = name;
        this.color = color;
    }

    public int getColor() {
        return this.color;
    }

    final public String toString() {
        return this.name;

    }

    public Move think(World world) {
        if (this.color == World.WHITE)
            world.flip();
        Move move = search(world);
        if (this.color == World.WHITE)
            move.color = World.WHITE;
        return (move != null ? move : Move.PASS);
    }

    protected Move search(World world) {
        var moves = world.getLegalMoves();
        if (moves.isEmpty())
            return Move.PASS;
        return moves.get(0);
    }
}