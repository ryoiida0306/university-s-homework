package strategy;
//ある人の5つの単位の取得とその評価。
//5つの評価は配列に入れて使う。
public class Human {
	String name;
	int[] scores =new int[5];

	public Human(String name, int[] scores) {
		for(int i = 0;i<scores.length;i++) {
			if(scores[i]<0){
				System.out.println("評価が負の教科があります。");
				break;
			}
			this.scores[i] = scores[i];
		}
	}

	public int[] getScores() {
		return scores;
	}
}
