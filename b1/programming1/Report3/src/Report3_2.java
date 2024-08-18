//1972年5月1日は月曜日
import java.util.Scanner;
public class Report3_2 {

	private static int uruu(int u) {    //閏年かを判断するメソッド
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
		return a;
	}
	private static int md(int m,int year) {
		int y=0;
		switch(m) {              //月によって変わる日数を出力するメソッド
		case 1:
		case 3:
		case 5:
		case 7:
		case 8:
		case 10:
		case 12:y+=31;break;
		case 4:
		case 6:
		case 9:
		case 11:y+=30;break;
		case 2:if(uruu(year)==1) {
			y+=29;
		}else {
			y+=28;
		}

		}
		return y;
	}

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		System.out.print("年を入力してください：");    //年、月の入力
		int year = stdIn.nextInt();
		System.out.print("月を入力してください：");
		int month = stdIn.nextInt();
		//以下2つの失敗作
		/*int d=0;
		  if(year>1972) {
			d+=3+2+3+3+2+3+2+3;      //失敗作１
			int ud = 0;
			for(int i=1973;i<year;i++) {
				ud+=uruu(i);
			}
			d+=(year-1973+ud);
			if(month>2) {
				d+=uruu(month);
			}
			for(int i=1;i<month;i++) {
				d+=md(i);
			}
			d%=7;
		}
		System.out.print(d);*/

		/*int d=6;
		  int ud = 0;
		for(int i=1;i<year;i++) {
			System.out.println(i+" "+uruu(i));     //失敗作２
			ud+=uruu(i);
		}
		d+=year-1+ud;
		if(month>2) {
			d+=uruu(year);
		}
		int a = 0;
		for(int i=1;i<month;i++) {
			d+=md(i);
			a+=md(i);
		}
		d=d%7;
		System.out.println(a);
		System.out.println(uruu(year));
		System.out.println(ud);
		System.out.print(d);*/
		//失敗作終わり
		int C =year/100;
		int Y =year%100;
		int Ganma=0;               //ツェラーの公式を適用
		if(1582<=year)Ganma=5*C+(C/4);
		else if(4<=year)Ganma=6*C+5;
		int h = ((1+((26*(month+1))/10)+Y+(Y/4)+Ganma+5)%7+1)%7;
		//System.out.println(h);

		System.out.println(year+"年"+month+"月のカレンダー");
		String[] h2= {"S","M","Tu","W","Th","F","S"};           //曜日の入力
		for(int i=0;i<7;i++){
		System.out.printf("%3s",h2[i]);                       //曜日の出力
		}
		System.out.print("\n");
		for(int i=0;i<h;i++) {
			System.out.print("   ");                 //空白の出力
		}
		int[] number=new int[md(month,year)];      //number配列に数字を代入
		for(int i=0;i<number.length;i++) {
			number[i]=i+1;
		}
		for(int i=0;i<number.length;i++) {                      //日付の出力
			System.out.printf("%3d",number[i]);
			if((h+number[i])%7==0)System.out.print("\n");   // 折り返す条件
		}

	}
}
