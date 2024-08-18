public class Main {
    public static void main(String[] args){
        long startTime = System.currentTimeMillis();
        Solver solver = new Solver();
        solver.solve(new State(new World()));
        solver.printEvaluation();
        long endTime = System.currentTimeMillis();
        System.out.println("実行時間：" + (endTime-startTime)+"ms");
        System.out.println("メモリ使用量："+(Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory()));
    }
}
