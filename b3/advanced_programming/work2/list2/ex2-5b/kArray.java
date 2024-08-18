// import java.util.*;

public class kArray{
    static int K[] = new int[100];
    static int kCounter = 0;

    static void add(int k){
        K[k]++;
        kCounter++;
        if(kCounter %100 == 0){
            System.out.println(kCounter + "problems was solved.");
        }
    }

    static void printK(){
        for(int k : K){
            System.out.print(k+" ");
        }
    }
}