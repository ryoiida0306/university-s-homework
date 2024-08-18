package iterator;

public class Student {
	int studentNum;//学籍番号
	String name;//名前
	int grade;//学年
	String department;//学科

	//コンストラクタ
	public Student(int num, String name, int grade, String dep) {
		this.studentNum = num;
		this.name = name;
		this.grade = grade;
		this.department = dep;
	}

	//名前を取得
	public String getName() {
		return name;
	}

	//全ての情報を表示
	public String toString() {
		return studentNum + "|" + name + "|" + grade + "|" + department;
	}

}
