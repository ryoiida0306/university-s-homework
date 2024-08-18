import java.util.Scanner;
public class Report1_2 {

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		System.out.print("一つ目の値：");
		int x = stdIn.nextInt();
		System.out.print("二つ目の値：");
		int y = stdIn.nextInt();
		System.out.println("足し算:"+(x+y));
		System.out.println("引き算:"+(x-y));
		System.out.println("掛け算:"+(x*y));
		System.out.println("割り算:"+(x/y));

	}

}