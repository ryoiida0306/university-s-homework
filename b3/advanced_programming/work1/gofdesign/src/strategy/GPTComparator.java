package strategy;
//GPTで比べる戦略
//Comparatorを継承することにより、多様性をつくる。
//上のクラスからの比較をゆだねられたクラス
public class GPTComparator implements Comparator{

	double GPTCalc(int[] scores) {
		double GPT = 0;
		for(int i =0;i<scores.length;i++) {
			GPT+= scores[i];
		}
		return GPT;
	}

	public int compare(Human h1, Human h2) {
		double h1GPT = GPTCalc(h1.getScores());
		double h2GPT = GPTCalc(h2.getScores());

		if (h1GPT > h2GPT) {
			return 1;
		} else if (h1GPT == h2GPT) {
			return 0;
		}
		return -1;
	}
}
