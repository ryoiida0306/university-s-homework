package iterator;
//Aggregateを継承したStudentをまとめるクラス
public class ClassRoom implements Aggregate{

	private Student[] students;
	private int last = 0;

	public ClassRoom(int size) {
		this.students = new Student[size];
	}

	public Student getStudentAt(int index) {
		return students[index];
	}

	//生徒を追加
	public void appendStudent(Student student) {
		this.students[last] = student;
		last++;
	}

	//長さを取得
	public int getLength() {
		return last;
	}

	//インスタンス化して返す
	public Iterator iterator() {
		return new ClassRoomIterator(this);
	}

}
