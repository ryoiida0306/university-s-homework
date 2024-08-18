import java.util.*;

class MinMaxPlayer {
    int depthLimit = 4;

    float maxSearch(World world, int depth) {
        if (isTerminal(world, depth))
            return Eval.shared.value(world);

        List<Move> moves = world.getMoves();
        float v = Float.NEGATIVE_INFINITY;

        for (Move move : moves) {
            World newWorld = world.perform(move);
            v = Math.max(v, minSearch(newWorld, depth + 1));
        }
        return v;
    }

    float minSearch(World world, int depth) {
        if (isTerminal(world, depth))
            return Eval.shared.value(world);

        List<Move> moves = world.getMoves();
        float v = Float.POSITIVE_INFINITY;

        for (Move move : moves) {
            World newWorld = world.perform(move);
            v = Math.min(v, minSearch(newWorld, depth + 1));
        }
        return v;
    }

    boolean isTerminal(World world, int depth) {
        return world.isGoal() || depth > this.depthLimit;
    }
}
