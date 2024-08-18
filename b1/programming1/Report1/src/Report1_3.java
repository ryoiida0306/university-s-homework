import java.util.Scanner;
public class Report1_3 {

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		System.out.print("三角形の面積を求める。\n 底辺の長さ：");
		int x = stdIn.nextInt();
		System.out.print("高さ：");
		int y = stdIn.nextInt();
		System.out.println("（三角形の面積）＝"+x*y/2);
		System.out.print("次に四角形の面積を求める。\n 縦の長さ:");
		int a =stdIn.nextInt();
		System.out.print("横の長さ:");
		int b = stdIn.nextInt();
		System.out.println("（四角形の面積）＝"+(a*b));
		System.out.print("次に台形の面積を求める。\n上底の長さ：");
		int c =stdIn.nextInt();
		System.out.print("下底の長さ：");
		int d = stdIn.nextInt();
		System.out.print("高さの長さ：");
		int e = stdIn.nextInt();
		System.out.println("（台形の面積）＝"+(c+d)*e/2);
		System.out.print("最後に円の面積を求める。\n 半径の長さ:");
		int f = stdIn.nextInt();
		System.out.println("（円の面積）＝"+f*f*3.1415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679);



	}

}
