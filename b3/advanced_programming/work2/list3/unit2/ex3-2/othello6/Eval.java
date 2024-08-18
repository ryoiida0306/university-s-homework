package othello6;

import othello6.*;

public class Eval {
    static float[][] M = {
            { 100, -10, 20, 20, -10, 100 },
            { -10, -50, 1, 1, -50, -10 },
            { 20, 1, 1, 1, 1, 20 },
            { 20, 1, 1, 1, 1, 20 },
            { -10, -50, 1, 1, -50, -10 },
            { 100, -10, 20, 20, -10, 100 },
    };

    public float value(World world) {
        if (world.isGoal())
            return 1000000 * world.getWinner() + world.getScore();

        float score = 0;
        for (Position p : Position.all) {
            int disc = world.getBoard().get(p);
            score += disc * M[p.getRow()][p.getCol()];
        }
        return score;
    }
}
