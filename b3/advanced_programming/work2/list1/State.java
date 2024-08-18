class State {
    State parent;
    Action action;
    World world;

    State(World world) {
        this.parent = null;
        this.world = world;
    }

    State(State parent, Action action, World nextWorld) {
        this.parent = parent;
        this.action = action;
        this.world = nextWorld;
    }

    public String toString() {
        return this.world.toString();
    }

    boolean isGoal() {
        return this.world.isGoal();
    }
}
