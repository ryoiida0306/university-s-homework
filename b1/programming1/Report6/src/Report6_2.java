import java.util.Random;

public class Report6_2 {
	//MakePointAndJudgeメソッド
	public static int MPAJ() {
		Random rand = new Random();
		double x = rand.nextDouble();
		double y= rand.nextDouble();
		if(x*x+y*y<=1)
			return 1;
		return 0;
	}

	public static double Judge50() {
		double sum = 0;
		for (int i = 0; i < 50; i++) {
			sum += MPAJ();
		}
		return sum;
	}

	public static void ast50(double sum, int orbit) {//orbitは何巡目か を表す
		double PiDelta = sum/(orbit*50)*4-3.14159265;
		if (PiDelta<0)
			PiDelta=-PiDelta;//PiDeltaを絶対値に変換
		for (int i = 0; i < PiDelta*100; i++) {//精度:100
			System.out.print('*');
		}
		System.out.println();

	}
	public static void main(String[] args) {
		double sum = 0;
		for (int i = 0; i < 1000/50; i++) {
			sum+=Judge50();
			ast50(sum,i+1);
		}
		System.out.print(sum*4/1000);
	}

}
