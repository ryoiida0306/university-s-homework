package strategy;

public class Main {
	public static void main(String[] args) {
		int[] h1score = { 1, 2, 3, 4, 3 };
		Human h1 = new Human("sato", h1score);
		int[] h2score = { 2, 4, 1, 2, 2 };
		Human h2 = new Human("suzuki", h2score);

		//一つの戦略のインスタンスを作る
		ScoreComparator comparator1 = new ScoreComparator(2);
		//戦略を束ねるクラスMyClassに入れる
		MyClass scoreComparator = new MyClass(comparator1);
		//表示
		System.out.println(scoreComparator.compare(h1, h2));

		GPAComparator comparator2 = new GPAComparator();
		MyClass GPAComparator = new MyClass(comparator2);
		System.out.println(GPAComparator.compare(h1, h2));

		GPTComparator comparator3 = new GPTComparator();
		MyClass GPTComparator = new MyClass(comparator3);
		System.out.println(GPTComparator.compare(h1, h2));

	}

}
