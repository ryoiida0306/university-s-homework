package iterator;

public class Main {

	public static void main(String[] args) {
		ClassRoom classRoom = new ClassRoom(2);
		classRoom.appendStudent(new Student(32114001,"sato",3,"情報工学科"));
		classRoom.appendStudent(new Student(32114002,"suzuki",3,"情報工学科"));

		//classRoomのイテレータの員スタンを作成
		Iterator iterator = classRoom.iterator();

		//次があれば名前を表示、の動作を繰り返す
		while(iterator.hasNext()) {
			Student student = (Student)iterator.next();
			System.out.println(student.getName());
		}

		iterator.itrReset();

		System.out.println("\n学籍番号|氏名|学年|学科");
		while(iterator.hasNext()) {
			Student student = (Student)iterator.next();
			System.out.println(student.toString());
		}



	}

}
