// import java.util.ArrayList;
import java.io.*;

public class Main {
    public static void main(String[] args){
        Data dataset = new Data(2000000);
        dataset.making();
        dataset.ListWrite("Dataset.txt");
        
        // for(World w : dataset.dataset){
        //     Solver solver = new Solver();
        //     solver.solve(new State(w));
        //     // solver.printEvaluation();
        // }
        // kArray.printK();
        

    }
}
