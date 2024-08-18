//(クラス名).とthis.に違いはあるのか
//結論：this.が使えない（笑）
public class Experiment01 {
	static int x = 700;

	static void printX() {
		System.out.println("x=" + x);
	}

//	static void printThisX() {
//		System.out.println("x=" + x);
//		System.out.println("this.x=" + this.x);
//		System.out.println("x=" + x);
//
//	}

	public static void main(String[] args) {
		System.out.println("x=" + x);
		int x = 800;
		System.out.println("x=" + x);

		System.out.println("Experiment01.x = " + Experiment01.x);

		printX();
	}

}
