import java.util.*;

public class Solver {
    int evaluation = 0;
    int MaxOpenListSize = 0;
    final boolean clist_active = true;

    

    // void solve(State root){
    //     State goal = this.search(root);
    //     if(goal != null) this.printSolution(goal);
    // }


    int getEvaluation(){
        return this.evaluation;
    }
    int getMaxOpenListSize(){
        return this.MaxOpenListSize;
    }

    State search(State root){
        ArrayList<State> openList = new ArrayList<State>();
        openList.add(root);
        ArrayList<State> CList = new ArrayList<State>();


        while(openList.size() > 0){
            State state = this.get(openList);
            // System.out.println(state.world.toString());
            if(clist_active){
                int isEqual = 0;
                for(State s : CList){
                    if(s.world.equals(state.world)){
                        isEqual = 1;
                        break;
                    }
                }
                if(isEqual == 0){
                    CList.add(state);
                }else{
                    continue;
                }
            }
            evaluation++;
            if(state.isGoal()) return state;
            var children = this.expand(state);
            //評価値の視認
            // if(evaluation%1000 == 0){
            //     System.out.print(state.world.toString());
            //     System.out.println(evaluation);
            // }
            openList = this.concat(openList, children);//BFS
            // openList = this.concat(children, openList);//DFS
            if(evaluation>100000){
                System.out.println(evaluation);
                System.out.println("infinity roop");
                break;
            }
            this.sort(openList);

            if(openList.size()>MaxOpenListSize){
                MaxOpenListSize = openList.size();
            }

        }
        evaluation = Integer.MAX_VALUE;
        return null;
    }

    State get(ArrayList<State> list){
        return list.remove(0);
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

    // void printSolution(State goal){
    //     Stack<State> solution = new Stack<State>();
    //     while(goal != null){
    //         solution.push(goal);
    //         goal = goal.parent;
    //     }
        
    //     kArray.add(solution.size());
    //     if(solution.size()>=31){
    //         System.out.println(solution.pop());
    //     }

    //     // System.out.print("手数：");
    //     // System.out.println(solution.size());

    //     // while(!solution.empty()){
    //     //     System.out.print(solution.pop());
    //     //     System.out.println(" -> ");
    //     // }
    // }

    void printEvaluation(){
        System.out.println("訪問ノード数："+this.evaluation);
    }
    void printMaxOpenListSize(){
        System.out.println("オープンリストの最大長："+getMaxOpenListSize());
    }

}
