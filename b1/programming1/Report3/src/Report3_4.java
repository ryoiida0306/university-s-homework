import java.util.Scanner;
public class Report3_4 {

	public static void main(String[] args) {
		Scanner stdIn=new Scanner(System.in);
		System.out.println("ax^2+bx+c=0の時");
		float a,b,c;
		do {
			System.out.print("a=");         //a,b,cの入力
			a = stdIn.nextFloat();
			System.out.print("b=");
			b = stdIn.nextFloat();
			System.out.print("c=");
			c = stdIn.nextFloat();
			if(b*b-4*a*c<0) {        //判別式を満たすか判定
				System.out.println("解がありません。もう一度入力してください");
			}
		}while(b*b-4*a*c<0);
		double x=0;
		while(!(Math.abs(a*x*x+b*x+c)<=1.602176634*Math.pow(10,-19))) {
			x-=(a*x*x+b*x+c)/(2*a*x+b);
			System.out.println(x);
		}
		System.out.print("近似値は"+x);
	}

}
