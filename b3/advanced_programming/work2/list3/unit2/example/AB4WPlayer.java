package example;

public class AB4WPlayer extends othello6.EX37AlphaBetaPlayer {
    float[][] W = {{1,0,0,0,0},{1,0,0,0,0},{1,0,0,0,0}};
    public AB4WPlayer(int color) {
        super("AB4W", color, 4);
        setW();
    }
    void setW(){
        super.setW(this.W);
    }
}
