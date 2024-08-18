import java.util.*;
import java.util.concurrent.*;

import example.*;
import league.*;
import othello6.*;
import othello6.Move;
// import unit2.othello6.Move;

import static othello6.World.*;

public class Main {
    public static void main(String[] args) throws Exception {
        // play();
        league();
    }

    static void play() {
        var ps = List.of(
                new Nega4Player(BLACK),
                new AB4Player(WHITE));

        var players = Map.of(BLACK, ps.get(0), WHITE, ps.get(1));
        var world = new World();

        boolean pass = false;

        // play this game
        while (world.isGoal() == false) {
            Player player = players.get(world.getNextTurn());
            World copy = new World(world);
            Move move = player.think(copy);

            world = world.perform(move);

            if (pass && move.isPass())
                break;
            pass = move.isPass();

            System.out.println(world);
            System.out.println();
        }
    }

    static void league() throws Exception {
        var players = List.of(
                AB4WPlayer.class,
                AB4Player.class);
                // RandomPlayer.class);
        var league = new League(players);
        league.perform(3, 5, TimeUnit.SECONDS);
    }
}