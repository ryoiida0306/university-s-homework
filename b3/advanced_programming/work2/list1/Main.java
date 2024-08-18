public class Main {
    public static void main(String[] args) {
        long startTime = System.currentTimeMillis();
        boolean clist_active = true;
        boolean isBFS = true;

        Solver solver = new Solver(clist_active,isBFS);
        solver.solve(new State(new World()));
        long endTime = System.currentTimeMillis();

        System.out.println("実行時間："+(endTime-startTime));
        solver.printEvaluation();
        solver.printMaxOpenListSize();
    }
}


// new Solver().solve(new State(new World()));

// Action action = new Action(-1,-1,-1);
// Action action2 = new Action(1,1,1);
// World world = new World();
// World another_world = world.perform(action);
// another_world = another_world.perform(action2);
// System.out.println(world.hashCode());
// System.out.println(another_world.hashCode());
// System.out.println(world.toString());
// System.out.println(another_world.toString());
// System.out.println(world.equals(another_world));