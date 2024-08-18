import java.util.Scanner;
public class Report4_3 {

	private static void sepi(int suuzi, int[] b,int ketasuu) {     //演習4-2のsepメソッドを流用、int型版
		for(int i=10,j=0;j<b.length;i*=10,j++) {
			b[b.length-j-1]=(suuzi%i)/(i/10);
		}
	}
	private static void sepl(long suuzi, int[] b,int ketasuu) {    //演習4-2のsepメソッドを流用、long型版
		for(long i=10L, j=0;j<b.length;i*=10,j++) {
			b[(int)(b.length-j-1)]=(int)((suuzi%i)/(i/10));
		}
	}


	private static boolean ad1(int[] z){//adは、all differentの略。配列のすべての要素が違うかを判定するメソッド、1つの配列について
		if(z[0]+z[1]+z[2]+z[3]+z[4]+z[5]+z[6]+z[7]+z[8]+z[9]!=45) return false;
		if(z[0]!=z[1]&&z[0]!=z[2]&&z[0]!=z[3]&&z[0]!=z[4]&&z[0]!=z[5]&&z[0]!=z[6]&&z[0]!=z[7]&&z[0]!=z[8]&&z[0]!=z[9]&&z[1]!=z[2]&&z[1]!=z[3]&&z[1]!=z[4]&&z[1]!=z[5]&&z[1]!=z[6]&&z[1]!=z[7]&&z[1]!=z[8]&&z[1]!=z[9]&&z[2]!=z[3]&&z[2]!=z[4]&&z[2]!=z[5]&&z[2]!=z[6]&&z[2]!=z[7]&&z[2]!=z[8]&&z[2]!=z[9]&&z[3]!=z[4]&&z[3]!=z[5]&&z[3]!=z[6]&&z[3]!=z[7]&&z[3]!=z[8]&&z[3]!=z[9]&&z[4]!=z[5]&&z[4]!=z[6]&&z[4]!=z[7]&&z[4]!=z[8]&&z[4]!=z[9]&&z[5]!=z[6]&&z[5]!=z[7]&&z[5]!=z[8]&&z[5]!=z[9]&&z[6]!=z[7]&&z[6]!=z[8]&&z[6]!=z[9]&&z[7]!=z[8]&&z[7]!=z[9]&&z[8]!=z[9]) {
			return true;
		}else return false;
	}
	private static boolean ad2(int[] x, int[] y) {//2つの配列についてのall different
		if(x[0]+x[1]+x[2]+x[3]+x[4]+y[0]+y[1]+y[2]+y[3]+y[4]!=45) return false;
		if(x[0]!=x[1]&&x[0]!=x[2]&&x[0]!=x[3]&&x[0]!=x[4]&&x[0]!=y[0]&&x[0]!=y[1]&&x[0]!=y[2]&&x[0]!=y[3]&&x[0]!=y[4]&&x[1]!=x[2]&&x[1]!=x[3]&&x[1]!=x[4]&&x[1]!=y[0]&&x[1]!=y[1]&&x[1]!=y[2]&&x[1]!=y[3]&&x[1]!=y[4]&&x[2]!=x[3]&&x[2]!=x[4]&&x[2]!=y[0]&&x[2]!=y[1]&&x[2]!=y[2]&&x[2]!=y[3]&&x[2]!=y[4]&&x[3]!=x[4]&&x[3]!=y[0]&&x[3]!=y[1]&&x[3]!=y[2]&&x[3]!=y[3]&&x[3]!=y[4]&&x[4]!=y[0]&&x[4]!=y[1]&&x[4]!=y[2]&&x[4]!=y[3]&&x[4]!=y[4]&&y[0]!=y[1]&&y[0]!=y[2]&&y[0]!=y[3]&&y[0]!=y[4]&&y[1]!=y[2]&&y[1]!=y[3]&&y[1]!=y[4]&&y[2]!=y[3]&&y[2]!=y[4]&&y[3]!=y[4]) {
			return true;
		}else return false;
	}

	public static void main(String[] args) {
		Scanner stdIn = new Scanner(System.in);
		System.out.print("いくつ列挙しますか？\n数字を入力してください：");
		int a = stdIn.nextInt();
		int counter=0;
		for(int i=10000;counter<a&&i<100000;i++) {
			for(int j=10000;counter<a&&j<100000;j++) {
				long k = (long)i*j;                                //kは10桁なので、long型
				int[] x=new int[5];
				int[] y=new int[5];
				int[] z=new int[10];
				sepi(i,x,5);                                 //x[],y[],z[]にそれぞれi,j,kの各位成分を代入
				sepi(j,y,5);
				sepl(k,z,10);
				if(k>=1000000000L&&ad1(z)&&ad2(x,y)) {        //adメソッドを使って、各位の数字を比較。また、k≧10^10の時に絞る。
				    System.out.println(i+"*"+j+"="+k+"　　　　"+(++counter)+"個目\n");
					//System.out.println(k);
				}
			}
		}
		System.out.print("終了");
	}

}