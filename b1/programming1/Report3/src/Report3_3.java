import java.util.Scanner;
public class Report3_3 {

	public static void main(String[] args) {
		Scanner stdIn= new Scanner(System.in);
		System.out.print("nを入力してください:");
		int n = stdIn.nextInt();
		System.out.print("  i  j  k\n");
		for(int i=1;i<=n-2;i++) {
			for(int j=1,k=n-i-1;k>=1;j++,k--) {     //for文の入れ子
				if(i<10&&j<10&&k<10) {
					System.out.printf("%3d",i);
					System.out.printf("%3d",j);
					System.out.printf("%3d\n",k);
				}
			}
		}
	}

}
