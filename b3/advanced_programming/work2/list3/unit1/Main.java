public class Main {
    public static void main(String[] args) {
        minMax();
        alphaBeta();
    }

    static void minMax() {
        MinMaxPlayer player = new MinMaxPlayer();
        World world = new World("A");
        double value = player.maxSearch(world, 0);
        System.out.println(value);
    }

    static void alphaBeta() {
        AlphaBetaPlayer player = new AlphaBetaPlayer();
        World world = new World("A");
        float alpha = Float.NEGATIVE_INFINITY;
        float beta = Float.POSITIVE_INFINITY;
        float value = player.maxSearch(world, alpha, beta, 0);
        System.out.println(value);
    }
}