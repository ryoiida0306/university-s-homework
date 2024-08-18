import java.util.*;
import java.io.*;

class Data {
    int index_size = 100;

    Data(){}
    Data(int index_size){
        this.index_size = index_size;
    }

    ArrayList<World_and_counter> dataset = new ArrayList<>();
    
    void making(){
        World firstWorld = new World();
        ArrayList<State> openList = new ArrayList<State>();
        openList.add(new State(firstWorld));
        // ArrayList<State> CList = new ArrayList<State>();


        while(openList.size() > 0 && dataset.size() < index_size){
            State state = openList.remove(0);
            // System.out.println(state.world.toString());

            // stateのworldがdataset.getworld()と一つでも同じになってたらbreakする。
            // stateのdepthがdataset.getcounter()と同じのところのみを探索する。←間違えたので訂正
            // stateのdepthはstate内で定義した。
            int isEqual = 0;
            for(World_and_counter d : dataset){
                World w = d.getWorld();
                // int   c = d.getCounter();

                // if(state.getDepth() != c){continue;}

                if(w.equals(state.world)){
                    isEqual = 1;
                    break;
                }

            }
            if(isEqual == 0){
                World_and_counter newWaC  = new World_and_counter(state.world,state.depth);
                dataset.add(newWaC);
            }else{
                continue;
            }
            var children = this.expand(state);
            openList = this.concat(openList, children);//BFS
            // openList = this.concat(children, openList);//DFS
            this.sort(openList);

            if(dataset.size()%1000==0){
                System.out.println(dataset.size());
            }

        }
        System.out.println("datamaking was success.");
        if(openList.size() == 0){System.out.println("this made data cover all patterns.");}
    }

    ArrayList<State> expand(State state){
        ArrayList<State> children = new ArrayList<State>();
        for(Action action: state.world.getAllActions()){
            if(state.world.isValid(action)){
                World newWorld = state.world.perform(action);//チェックしてから入れるように変更
                State newState = new State(state, action, newWorld);
                if(state.equals(newState)){continue;}//追加
                children.add(newState);
            }
        }
        return children;
    }

    ArrayList<State> concat(ArrayList<State> xs, ArrayList<State> ys){
        ArrayList<State> list = new ArrayList<State>(xs);
        list.addAll(ys);
        return list;
    }

    void sort(ArrayList<State> list){
        list.sort(Comparator.comparing(x -> x.g()));
    }

    void printKArray(){
        System.out.println(" k | |A_k|");
        for(int k = 0 ;;k++){
            int kCounter = 0;
            for(World_and_counter d : dataset){
                if(d.getCounter() == k){kCounter++;}
            }
            System.out.printf("%2d | %d\n",k,kCounter);
            if(kCounter == 0){break;}
        }
    }

    void ListWrite(String filename){
        try{
            BufferedReader reader =new BufferedReader(new InputStreamReader(System.in));
            PrintWriter writer = new PrintWriter(new BufferedWriter(new FileWriter(filename)));

            writer.println(" k | |A_k|");
            for(int k = 0 ;;k++){
                int kCounter = 0;
                for(World_and_counter d : dataset){
                  if(d.getCounter() == k){kCounter++;}
                }
                writer.printf("%2d | %d\n",k,kCounter);
                if(kCounter == 0){break;}
            }

            for(World_and_counter d : this.dataset){
                writer.println(d.toString());
            }
            
            // String line;
            // int i = 0;
            // while((line = reader.readLine()) != null && i<3){
            //     writer.println(line);
            //     System.out.println(line);
            //     i++;
            // }
            reader.close();
            writer.close();
        }catch(IOException e){
            System.out.println(e);
        }
        System.out.println("dataset was written.");
    }


}

class World_and_counter {
    World world;
    int counter;

    World_and_counter(World world , int counter){
        this.world = world;
        this.counter = counter;
    }

    World getWorld(){
        return this.world;
    }

    int getCounter(){
        return this.counter;
    }

    public String toString(){
        return this.world.toString()+"    |  "+ this.counter;
    }

}