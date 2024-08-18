/*入力された年が、閏年かどうかを判断するプログラムを作成し提出せよ。閏年の決め方は以下の通り。
　（閏年の決め方 ）
1.閏年とは：西暦年が４で割り切れる年は閏年
2.閏年の例外：上記、１であっても西暦年が１００で割り切れる場合は、閏年としない。
3.閏年の例外の例外：上記、２であっても西暦年が４００で割り切れる場合は、閏年。
*/
import java.util.Scanner;
public class Report2_2 {

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		System.out.print("年を入力してください：");
		int u = stdIn.nextInt();
		int a = 0;
		if(u%4==0) {
			a=1;
		    if(u%100==0) {
			    a=0;
			    if(u%400==0) {
			    	a=1;
			    }
		    }
		}
		switch(a){
			case 0 :System.out.print("閏年ではありません。");
			        break;
			case 1 :System.out.print("閏年です。");
		}

	}

}
