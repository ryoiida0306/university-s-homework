import java.util.Scanner;
public class Report1_5 {

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		System.out.print("何秒？\n 時間を入力してください：");
		int s = stdIn.nextInt();
		int h = s/3600;
		int m =(s-h*3600)/60;
		System.out.print(h+"時"+m+"分"+s%60+"秒");

		/* 日数と年数も考慮すると、
		int s = stdIn.nextInt();
		int m = (s/60)%60;
		int h =(s/3600)%24;
		int d =((s/3600)/24)%365;
		int y =((s/3600)/24)/365;
		System.out.print(y+"年"+d+"日"+h+"時"+m+"分"+s%60+"秒");
		 */

	}

}
