public class Report5_2 {

	public static void main(String[] args) {
		/*int num =1;
		for(int i = 2;i<=100;i++) {
			for(int j = 1;j<=i;j++) {
				num *=j;

			}
			System.out.println(i+"!="+num);
			num=1;
		}
		*/
		int [] num = new int [200];
		for(int i=0;i<200;i++) {
			num[i] = 0;
		}
		num[0] = 1;


		for(int i=2;i<=100;i++) {
			//各位に掛け算
			for(int j=0;j<199;j++) {
				num[j]*=i;
			}
			//繰り上げ
			for(int j=0;j<199;j++) {
				num[j+1]+=num[j]/10;

				if(num[j]/10!=0) {
					num[j]%=10;
				}
			}
			//高い位の0を除く（例えば、2!=00・・・002  となるのを防ぐ）
			int zerosum =0;
			for(int j=199;num[j]==0;j--) {
				zerosum++;
			}

			//表示
			System.out.print(i+"!=");
			for(int j=199-zerosum;j>=0;j--) {
				System.out.print(num[j]);
			}
			//改行
			System.out.println();
		}


	}

}
