import java.util.*;
import java.util.stream.*;

class Move {
    String name;

    Move(String name) {
        this.name = name;
    }

    public String toString() {
        return this.name;
    }
}

class World {
    Map<String, Float> nodes = Map.of(// map(key,value)
            "A", 0f,
            "B", 0f,
            "C", 0f,
            "D", 3.0f,
            "E", 2.0f,
            "F", 1.0f,
            "G", 4.0f);

    Map<String, List<String>> children = Map.of(
            "A", List.of("B", "C"),
            "B", List.of("D", "E"),
            "C", List.of("F", "G"));

    String current;

    World(String current) {
        this.current = current;
    }

    public String toString() {
        return this.current.toString();
    }

    boolean isGoal() {
        return getMoves().isEmpty();
    }

    List<Move> getMoves() {
        var list = this.children.getOrDefault(this.current, new ArrayList<>());
        // getofdefault:指定されたキーがマップされている値を返します。このマップにそのキーのマッピングが含まれていない場合はdefaultValueを返します。
        return list.stream().map(c -> new Move(c)).collect(Collectors.toList());
        //
    }

    World perform(Move move) {
        return new World(move.name);
    }

}

class Eval {
    static Eval shared = new Eval();

    float value(World world) {
        return world.nodes.get(world.current);
    }
}