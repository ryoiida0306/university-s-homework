import java.util.*;

class Solver {
    //この機械の評価値。小さいほど良い
    int evaluation = 0;
    int MaxOpenListSize = 0;
    boolean clist_active = true;
    boolean isBFS = true;

    Solver(boolean clist_active, boolean isBFS){
        this.clist_active = clist_active;
        this.isBFS = isBFS;
    }

    int getEvaluation(){
        return this.evaluation;
    }

    int getMaxOpenListSize(){
        return this.MaxOpenListSize;
    }


    void solve(State root){
        State goal = this.search(root);
        if(goal != null){
            this.printSolution(goal);
        }
    }

    //解が見つかればその状態を返し、見つからなければnullを返す。
    State search(State root){
        ArrayList<State> openList = new ArrayList<State>();
        openList.add(root);
        ArrayList<State> CList = new ArrayList<State>();
        

        //指導所の内容の場所
        while(openList.size() > 0){
            State state = this.get(openList);
            if(clist_active){
                int isEqual = 0;
                for(State s : CList){
                    if(s.world.hashCode() == state.world.hashCode()){
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
            if(state.isGoal()){
                return state;
            }
            ArrayList<State> children = this.expand(state);
            //評価値の視認
            // if(evaluation%1000 == 0){
            //     System.out.print(state.world.toString());
            //     System.out.println(evaluation);
            // }
            if(this.isBFS)
                openList = this.concat(openList,children);//BFS
            else
                openList = this.concat(children,openList);//DFS

            if(openList.size()>MaxOpenListSize){
                MaxOpenListSize = openList.size();
            }

            if(evaluation>150000){
                System.out.println(evaluation);
                System.out.println("infinity roop. falue");
                break;
            }
        }
        evaluation = Integer.MAX_VALUE;
        return null;
    }

    State get(ArrayList<State> list) {
        return list.remove(0);
    }

    ArrayList<State> expand(State state) {
        ArrayList<State> children = new ArrayList<State>();
        for(Action action: state.world.getAllActions()) {
            World newWorld = state.world.perform(action);
            if(newWorld.isValid()) {
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

    //goalから逆向きにたどって表示するプログラム
    void printSolution(State goal){
        Stack<State> solution = new Stack<State>();
        while(goal != null){
            solution.push(goal);
            goal = goal.parent;
        }
        while(!solution.empty()){
            System.out.print(solution.pop());
            System.out.print(" -> ");
        }
        System.out.println();
    }

    void printEvaluation(){
        System.out.println("訪問ノード数："+getEvaluation());
    }

    void printMaxOpenListSize(){
        System.out.println("オープンリストの最大長："+getMaxOpenListSize());
    }
}