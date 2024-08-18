import java.util.Scanner;

public class Report6_3 {

	public static String translate(int x) {
		String a = null;
		switch(x){
			case -1: a="左";
			break;
			case 0 : a="中";
			break;
			case 1 : a="右";
			break;
		}
		return a;

	}

	public static int translate(String x) {
		int a =0;
		switch(x){
			case "左": a=-1;
			break;
			case "中": a=0;
			break;
			case "右": a=1;
			break;
		}
		return a;

	}
	public static void hanoi(int x,int y,int layer) {
		if(layer==1)
			System.out.println(translate(x)+"にある一番上の円盤を"+translate(y)+"へ移動させる");
		else {
			hanoi(x,-(x+y),layer-1);
			System.out.println(translate(x)+"にある一番上の円盤を"+translate(y)+"へ移動させる");
			hanoi(-(x+y),y,layer-1);
		}
	}
	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		System.out.println("ハノイの塔を解きます。");
		System.out.println("どこからどこへ移しますか?");
		System.out.println("どこから?");
		System.out.print("左、中、右のどれかを入力してください:");
		String x = stdIn.next();
		System.out.println("どこへ?");
		System.out.print("左、中、右のどれかを入力してください:");
		String y = stdIn.next();
		System.out.println("何層のを解きますか?");
		System.out.print("数字を入力して下さい:");
		int layer = stdIn.nextInt();

		System.out.println("手順数は"+(int)(Math.pow(2,layer)-1)+"です。");
		hanoi(translate(x),translate(y),layer);

	}

}
