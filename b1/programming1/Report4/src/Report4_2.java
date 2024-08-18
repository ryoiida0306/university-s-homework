import java.util.Scanner;
public class Report4_2 {
	private static int ketahantei(int suuzi) {  //桁数を判定するメソッド
		int ketasuu=0;
		int suuzi2=suuzi;
		while(suuzi2!=0) {
			suuzi2/=10;
			ketasuu++;
		}
		return ketasuu;
	}
	private static void sep(int suuzi, int[] b,int ketasuu) {  //与えられた数字の各位の数字を分けて配列に代入するメソッド
		for(int i=10,j=0;j<b.length;i*=10,j++) {
			b[b.length-j-1]=(suuzi%i)/(i/10);
		}
	}
	private static void marking(String[][] x) {    //配列のi（番号）の、上からj行目の*の配置を割り振りを代入するメソッド
		x[0][0]=x[0][6]=x[2][0]=x[2][3]=x[2][6]=x[3][0]=x[3][3]=x[3][6]=x[4][3]=x[5][0]=x[5][3]=x[5][6]=x[6][0]=x[6][3]=x[6][6]=x[7][0]=x[8][0]=x[8][3]=x[8][6]=x[9][0]=x[9][3]=x[9][6]="＊＊＊＊＊　";
		x[0][1]=x[0][2]=x[0][3]=x[0][4]=x[0][5]=x[4][0]=x[4][1]=x[4][2]=x[6][4]=x[6][5]=x[7][1]=x[7][2]=x[7][3]=x[8][1]=x[8][2]=x[8][4]=x[8][5]=x[9][1]=x[9][2]="＊　　　＊　";
		x[2][4]=x[2][5]=x[5][1]=x[5][2]=x[6][1]=x[6][2]="＊　　　　　";
		x[1][0]=x[1][1]=x[1][2]=x[1][3]=x[1][4]=x[1][5]=x[1][6]=x[2][1]=x[2][2]=x[3][1]=x[3][2]=x[3][4]=x[3][5]=x[4][4]=x[4][5]=x[4][6]=x[5][4]=x[5][5]=x[7][4]=x[7][5]=x[7][6]=x[9][4]=x[9][5]="　　　　＊　";
	}

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		System.out.print("数字を入力してください：");
		int x = stdIn.nextInt();
		int ketasuu=ketahantei(x);             //桁判定を行う
		int[] y=new int[ketasuu];
		sep(x,y,ketasuu);                       //各位の数字を分けてy[]に代入
		/*for(int i=0;i<ketasuu;i++) {
		System.out.println(y[i]);
		}*/
		String[][] ast;
		ast = new String[10][7];
		marking(ast);                           //ast[][]に代入
		/*for(int i=0;i<10;i++) {
			for(int j=0;j<7;j++) {
				System.out.println(ast[i][j]);
			}
			System.out.println();
		}*/
		for(int i=0;i<7;i++){                   //行
			for(int j=0;j<ketasuu;j++) {
				System.out.print(ast[y[j]][i]); //数字
			}
			System.out.print("\n");
		}
	}

}
