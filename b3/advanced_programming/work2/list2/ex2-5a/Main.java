// import java.util.ArrayList;

public class Main {
    public static void main(String[] args){

        int index_size = Integer.parseInt(args[0]);

        long startTime = System.currentTimeMillis();

        Data dataset = new Data(index_size);
        dataset.making();
        dataset.printKArray();
        dataset.ListWrite("dataset.txt");
        // for(World w : dataset.dataset){
        //     Solver solver = new Solver();
        //     solver.solve(new State(w));
        //     // solver.printEvaluation();
        // }
        // kArray.printK();

        long endTime = System.currentTimeMillis();
        System.out.println("実行時間：" + (endTime-startTime)+"ms");
        System.out.println("メモリ使用量："+(Runtime.getRuntime().totalMemory() - Runtime.getRuntime().freeMemory()));

    }
}
