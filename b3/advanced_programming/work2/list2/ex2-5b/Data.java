import java.util.*;
import java.io.*;

class Data {
    int index = 100;

    Data(){}
    Data(int index){
        this.index = index;
    }

    ArrayList<World> dataset = new ArrayList<>();
    
    void making(){
        World firstWorld = new World();
        ArrayList<State> openList = new ArrayList<State>();
        openList.add(new State(firstWorld));
        // ArrayList<State> CList = new ArrayList<State>();
        int deleted_data = 0;


        while(openList.size() > 0 && dataset.size() < index){
            State state = openList.remove(0);
            // System.out.println(state.world.toString());
            
            int isEqual = 0;
            for(World w : dataset){
                if(w.equals(state.world)){
                    isEqual = 1;
                    break;
                }
            }
            if(isEqual == 0){
                dataset.add(state.world);
            }else{
                deleted_data++;
                if(openList.size() == 0){
                    System.out.print("the dataset covers all patterns. > ");
                    System.out.println(dataset.size()+"patterns");
                }
                continue;

            }
            var children = this.expand(state);
            openList = this.concat(openList, children);//BFS
            // openList = this.concat(children, openList);//DFS
            this.sort(openList);

            // if(dataset.size()%1000==0){
            //     System.out.println(dataset.size());
            // }
            if(dataset.size()%1000 == 0){
                System.out.print("get"+dataset.size()+"patterns.");
                System.out.print("   openList size : "+openList.size());
                System.out.println("   deleted data : "+deleted_data);
            }
            if(openList.size() == 0){
                System.out.print("the dataset covers all patterns. > ");
                System.out.println(dataset.size()+"patterns");
            }
        }
        System.out.println("datamaking was success.");

    }

    ArrayList<State> expand(State state){
        ArrayList<State> children = new ArrayList<State>();
        for(Action action: state.world.getAllActions()){
            if(state.world.isValid(action)){
                World newWorld = state.world.perform(action);//チェックしてから入れるように変更
                State newState = new State(state, action, newWorld);
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

    void ListWrite(String filename){
        try{
            BufferedReader reader =new BufferedReader(new InputStreamReader(System.in));
            PrintWriter writer = new PrintWriter(new BufferedWriter(new FileWriter(filename)));

            for(World w : this.dataset){
                writer.println(w.toString());
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