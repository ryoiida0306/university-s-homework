class AlphaBetaPlayer {
    int depthLimit = 4;

    float maxSearch(World world, float alpha, float beta, int depth) {
        if (isTerminal(world, depth))
            return Eval.shared.value(world);

        var moves = world.getMoves();

        for (Move move : moves) {
            World newWorld = world.perform(move);
            float v = minSearch(newWorld, alpha, beta, depth + 1);
            alpha = Math.max(alpha, v);
            if (alpha >= beta)
                break;
        }

        return alpha;
    }

    float minSearch(World world, float alpha, float beta, int depth) {
        if (isTerminal(world, depth))
            return Eval.shared.value(world);

        var moves = world.getMoves();

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
}