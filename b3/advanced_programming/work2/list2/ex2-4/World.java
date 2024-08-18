import java.util.*;

class World implements Cloneable{
    ArrayList<Integer> board = new ArrayList<Integer>();

    World(){
        int[] firstboard = {
            8,6,7,2,5,4,3,0,1
        };
        for(int pannel : firstboard){
            board.add(pannel);
        }
    }

    public String toString(){
        return String.format(
            "%d %d %d \n%d %d %d \n%d %d %d\n",
            this.board.get(0),this.board.get(1),this.board.get(2),
            this.board.get(3),this.board.get(4),this.board.get(5),
            this.board.get(6),this.board.get(7),this.board.get(8)
            );
    }

    public boolean equals(Object otherObj){
        if(otherObj instanceof World){
            World other = (World)otherObj;
            int ans = 1;
            for(int i = 0; i<other.board.size();i++){
                if(this.board.get(i) != other.board.get(i)) ans*=0;
            }
            if(ans == 1) return true;
        }
        return false;
    }

    public World clone() {
        World another = new World();
        for(int i = 0;i<another.board.size();i++){
            another.board.set(i,this.board.get(i));
        }
        return another;
    }

    public ArrayList<Integer> change_element(ArrayList<Integer> board,int[] change_index){
        int tmp = -1;
        tmp = board.get(change_index[0]);
        board.set(change_index[0],board.get(change_index[1]));
        board.set(change_index[1],tmp);
        return board;
    }

    boolean isGoal() {
        int ans = 1;
        for(int i = 0; i<this.board.size();i++){
            if(this.board.get(i) != (i+1)%9) ans = 0;
        }
        if (ans == 1) return true;
        return false;
    }

    List<Action> getAllActions(){
        return new ArrayList<>(Action.allActions);
    }
    

    World perform(Action action){
        World newWorld = this.clone();
        newWorld.board = this.change_element(newWorld.board,action.change_index);
        return newWorld;
    }

    boolean isValid(Action action){
        //どちらにも0がなければaction出来ない
        if(this.board.get(action.change_index[0])*this.board.get(action.change_index[1]) > 0){
            return false;
        }
        return true;
    }

    int estimate(){
        int manhattan_distance = 0;
        //各数字においてマンハッタン距離の記すテーブルを作る
        int[][] m_table = {{
            //1
            0, 1, 2,
            1, 2, 3,
            2, 3, 4
        },{
            //2
            1, 0, 1,
            2, 1, 2,
            3, 2, 3
        },{
            //3
            2, 1, 0,
            3, 2, 1,
            4, 3, 2
        },{
            //4
            1, 2, 3,
            0, 1, 2,
            1, 2, 3
        },{
            //5
            2, 1, 2,
            1, 0, 1,
            2, 1, 2
        },{
            //6
            3, 2, 1,
            2, 1, 0,
            3, 2, 1
        },{
            //7
            2, 3, 4,
            1, 2, 3,
            0, 1, 2
        },{
            //8
            3, 2, 3,
            2, 1, 2,
            1, 0, 1
        }
        };
        
        for(int i = 0; i<m_table.length;i++){
            if(this.board.get(i) == 0){continue;}
            manhattan_distance += m_table[this.board.get(i)-1][i];
        }

        return manhattan_distance;
    }
}

class Action {
    int[] change_index = new int[2];

    Action(int change_index_left, int change_index_right) {
        this.change_index[0] = change_index_left;
        this.change_index[1] = change_index_right;
    }

    int cost(){
        return 1;
    }

    static List<Action> allActions = Arrays.asList(
            new Action(0, 1),
            new Action(1, 2),
            new Action(0, 3),
            new Action(1, 4),
            new Action(2, 5),
            new Action(3, 4),
            new Action(4, 5),
            new Action(3, 6),
            new Action(4, 7),
            new Action(5, 8),
            new Action(6, 7),
            new Action(7, 8)
    );
}