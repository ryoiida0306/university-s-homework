import java.util.Scanner;
public class Report2_challenge {

	public static void main(String[] args) {
		System.out.println("使い方\n①　演算子の前と後にenterキーを押してください\n②　メモリーを呼び出すときはMRCと入力してください");
		Scanner stdIn = new Scanner(System.in);
		int i = 0;
		float memory = 0;
		float M = 0;
		while(i==0) {
		System.out.println("------------------------------------\n計算を始めます。値を入力してください");
		float result = stdIn.nextFloat();
		String o = stdIn.next();
		float a = 0;
		String b ;
		while(!(o.equals("="))) {
			switch(o) {
			case "+" :b = stdIn.next();
			          if(b.equals("MRC")){
			        	  a=memory;
			          }else {
			        	  a = Float.parseFloat(b);
			          }
			          result += a;
			          break;
			case "-" :b = stdIn.next();
	                  if(b.equals("MRC")){
	        	      a=memory;
	                  }else {
	             	  a = Float.parseFloat(b);
	                  }
	                  result -= a;
	                  break;
			case "*" :b = stdIn.next();
	                 if(b.equals("MRC")){
	        	     a=memory;
	                 }else {
	        	     a = Float.parseFloat(b);
	                 }
	                 result =result*a;
	                 break;
			case "/" :b = stdIn.next();
	                 if(b.equals("MRC")){
	        	     a=memory;
	                 }else {
	        	     a = Float.parseFloat(b);
	                 }
	                 result =result/a;
	                 break;
			default  :System.out.println("演算子を入力してください");
			}
		o = stdIn.next();

		}
		System.out.println(result);
		System.out.println("M+、M-,メモリーをクリアするときMRCを入力、そうでないときnoを入力してください");
		String m = stdIn.next();
		switch(m) {
		case "M+" : memory+=result;
		            break;
		case "M-" : memory-=result;
		            break;
		case"MRC" : memory=0;
		            break;
		}
		}

	}

}
