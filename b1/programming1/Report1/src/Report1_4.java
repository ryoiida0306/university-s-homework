import java.util.Scanner;
public class Report1_4 {

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		System.out.print("一つ目の値：");
		float x = stdIn.nextFloat();
		System.out.print("二つ目の値：");
		float y = stdIn.nextFloat();
		System.out.println("足し算:"+(x+y));
		System.out.println("引き算:"+(x-y));
		System.out.println("掛け算:"+(x*y));
		System.out.println("割り算:"+(x/y));

	}

}
