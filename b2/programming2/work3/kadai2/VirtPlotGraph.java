// VirtPlotGraphクラスを書く

public class VirtPlotGraph{

	public static final int Y_MAX = 10;
	public static final int Y_MIN = - Y_MAX;

	private static int x = 0;

	private static char buffer[] = new char[??? - ??? + 1];
	
	public static int getX(){ ??? }
	public static void setX(int i){ x = i; } // thisは使えない

	public static void clear(){
		for(int y = 0;y < buffer.???;y++) buffer[???] = ' ';
	}

	public static void println(){  System.out.println(new String(buffer)); }

	public void plot(){
		int y = this.y;
		if(y < ???) y = Y_MIN;
		if(??? > ???) ???;
		buffer[y - ???] = symbol;
	}

	private char symbol;	
	private int y = 0;

	public VirtPlotGraph(char symbol){ ??? = symbol; }

	public int getY(){ ??? }
	public void setY(???){ ??? }

	public void computeY(){ setY(y); }

}
