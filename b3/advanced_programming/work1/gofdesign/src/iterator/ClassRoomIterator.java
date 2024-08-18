package iterator;

public class ClassRoomIterator implements Iterator {

	private ClassRoom classRoom;
	private int index;

	//コンストラクタ
	public ClassRoomIterator(ClassRoom classRoom) {
		this.classRoom = classRoom;
		this.index = 0;//indexを動かすことによりイテレータの役割を果たす。
	}

	//次があるかを見る
	public boolean hasNext() {
		if (index < classRoom.getLength()) {
			return true;
		} else {
			return false;
		}
	}

	//次のオブジェクトを返す
	public Object next() {
		Student student = classRoom.getStudentAt(index);
		index++;
		return student;
	}

	//indexの値をリセットする
	public void itrReset() {
		index = 0;
	}
}
