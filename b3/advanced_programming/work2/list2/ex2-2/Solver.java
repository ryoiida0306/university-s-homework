import java.util.*;

public class Solver {
    int evaluation = 0;
    int MaxOpenListSize = 0;

    void solve(State root){
        State goal = this.search(root);
        if(goal != null) this.printSolution(goal);
    }

    int getEvaluation(){
        return this.evaluation;
    }

    int getMaxOpenListSize(){
        return this.MaxOpenListSize;
    }

    State search(State root){
        ArrayList<State> openList = new ArrayList<State>();
        openList.add(root);
        // ArrayList<State> CList = new ArrayList<State>();


        while(openList.size() > 0){
            State state = this.get(openList);
            evaluation++;
            if(state.isGoal()) return state;
            var children = this.expand(state);
            openList = this.concat(openList, children);
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
            World newWorld = state.world.perform(action);
            if(newWorld.isValid()){
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
        list.sort(Comparator.comparing(x -> x.f()));
    }

    void printSolution(State goal){
        while(goal != null){
            System.out.print(goal);
            System.out.print(" <- ");
            goal = goal.parent;
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
