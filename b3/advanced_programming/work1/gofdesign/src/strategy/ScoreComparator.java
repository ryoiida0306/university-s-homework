package strategy;
//ある一つの単位の評価による比較の戦略
//Comparatorを継承することにより、多様性をつくる。
//上のクラスからの比較をゆだねられたクラス
public class ScoreComparator implements Comparator{
	int scoreNo = -1;
	public ScoreComparator(int scoreNo) {
		this.scoreNo = scoreNo;
	}

	public int compare(Human h1,Human h2) {
		if(h1.scores[scoreNo]>h2.scores[scoreNo]) {
			return 1;
		}else if(h1.scores[scoreNo]==h2.scores[scoreNo]) {
			return 0;
		}
		return -1;
	}
}
