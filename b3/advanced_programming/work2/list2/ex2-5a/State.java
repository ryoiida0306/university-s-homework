import java.util.Objects;

class State {
    State parent;
    Action action;
    World world;
    int cost;

    int depth;

    State(World world){
        this.parent = null;
        this.world = world;
        this.cost = 0;
        this.depth = 0;
    }

    State(State parent, Action action, World nextWorld){
        this.parent = parent;
        this.action = action;
        this.world = nextWorld;
        this.cost = action.cost() + parent.cost;
        this.depth = parent.getDepth() + 1;
    }

    public int getDepth(){
        return this.depth;
    }

    public int hashCode(){
        return Objects.hash(action, cost, parent, world);
    }

    public boolean equals(Object obj){
        if(obj instanceof State){
            State other = (State)obj;
            return this.world.equals(other.world);
        }
        return false;
    }

    public String toString(){
        return this.world.toString() + "@" + cost + "\n";
    }

    boolean isGoal(){
        return this.world.isGoal();
    }

    int f(){
        return this.g() + this.h();
    }
    
    int g(){
        return this.cost;
    }

    int h(){
        return this.world.estimate();
    }
}
