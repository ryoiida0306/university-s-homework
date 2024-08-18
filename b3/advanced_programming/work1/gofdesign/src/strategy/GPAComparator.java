package strategy;
//GPAで比べる戦略
//Comparatorを継承することにより、多様性をつくる。
//上のクラスからの比較をゆだねられたクラス
public class GPAComparator implements Comparator {

	double GPACalc(int[] scores) {
		double GPA = 0;
		double subLen = 0;
		for(int i= 0;i<scores.length;i++) {
			if(scores[i]>0) {
				GPA+=scores[i];
				subLen++;
			}
		}
	return GPA/=subLen;
	}



	public int compare(Human h1, Human h2) {
		double h1GPA = GPACalc(h1.getScores());
		double h2GPA = GPACalc(h2.getScores());

		if (h1GPA > h2GPA) {
			return 1;
		} else if (h1GPA == h2GPA) {
			return 0;
		}
		return -1;
	}

}
