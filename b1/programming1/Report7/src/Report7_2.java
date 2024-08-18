import java.util.Scanner;

public class Report7_2 {
	static void Digit(int x, int[] digit) {

		for (int i = 0; digit.length > i; i++) {
			digit[i] = (x >>> i & 1) == 1 ? 1 : 0;
		}

	}

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		System.out.print("一つ目の値を入力してください:");
		int x = stdIn.nextInt();
		System.out.print("二つ目の値を入力してください:");
		int y = stdIn.nextInt();
		double sum = 0;
		int[] digit = new int[31];
		Digit(y, digit);
		for (int i = 0; digit.length > i; i++)
			if (digit[i] == 1)
				sum += x << i;
		System.out.println(sum);
	}
}
