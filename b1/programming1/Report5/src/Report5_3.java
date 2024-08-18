public class Report5_3 {
	//演算子配列はその数字の後ろのやつ
	//階層は1が1階層、enzan3()に最初に入ったときには2階層
	private static void enzan3(int totalnum,int kaisou,String[] enzansi) {

		if(kaisou<=9) {
			//+の通り道
			totalnum+=kaisou;
			enzansi[kaisou-2]="+";
			enzan3(totalnum,kaisou+1,enzansi);
			totalnum-=kaisou;
			//-の通り道
			totalnum-=kaisou;
			enzansi[kaisou-2]="-";
			enzan3(totalnum,kaisou+1,enzansi);
			totalnum+=kaisou;
			//*の通り道
			totalnum*=kaisou;
			enzansi[kaisou-2]="*";
			enzan3(totalnum,kaisou+1,enzansi);
			totalnum/=kaisou;
			//何も入れないの通り道
			if(kaisou<=8) {
				//+の通り道
				totalnum+=11*kaisou+1;
				enzansi[kaisou-2]="+";
				enzansi[kaisou-1]="";
				enzan3(totalnum,kaisou+2,enzansi);
				totalnum-=11*kaisou+1;
				//-の通り道
				totalnum-=11*kaisou+1;
				enzansi[kaisou-2]="-";
				enzansi[kaisou-1]="";
				enzan3(totalnum,kaisou+2,enzansi);
				totalnum+=11*kaisou+1;
				//*の通り道
				totalnum*=11*kaisou+1;
				enzansi[kaisou-2]="*";
				enzansi[kaisou-1]="";
				enzan3(totalnum,kaisou+2,enzansi);
				totalnum/=11*kaisou+1;
			}

		}else {
			if(totalnum==100) {
				//表示

				//'('の数を決める。
				//なお、1と2の間のみ'('は必要ないため、i=1からにする。
				for(int i=1;i<8;i++) {
					if(enzansi[i].equals("*")) {
						System.out.print("(");
					}
				}
				System.out.print("1"+enzansi[0]+"2");

				//演算子が＊の時、その前に')'をつける
				for(int i=1;i<8;i++) {
					if(enzansi[i].equals("*")) {
						System.out.print(")");
					}
					System.out.print(enzansi[i]+(i+2));
				}
				System.out.println("=100");
			}
		}
	}
	public static void main(String[] args) {

		int totalnum=1;
		String[] enzansi = new String[8];
		enzan3(totalnum,2,enzansi);

	}


}
