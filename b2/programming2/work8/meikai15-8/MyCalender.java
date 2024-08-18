// 以下に必要な記述を追加せよ
// カレンダーの表示形式には様々なものが考えられるが
// 代表的なものは以下のものであろう

//       2018. 5
// Su Mo Tu We Th Fr Sa
//        1  2  3  4  5
//  6  7  8  9 10 11 12
// 13 14 15 16 17 18 19
// 20 21 22 23 24 25 26
// 27 28 29 30

public class MyCalender{
    public static int dayOfWeek(int y, int m, int d){
	// 必要であれば曜日を求めるこのメソッドを使用しても良い
	// ツェラーの公式による曜日の計算
	// [明解 Java,  p.322 より]
	if (m == 1 || m == 2){
	    y--;
	    m += 12;
	}
	return (y + y / 4 - y / 100 + y / 400 + (13 * m + 8 ) / 5 + d) % 7;
    }

    public static void printCalenderMonth(int year, int month){
    }
    
    // この他にも必要なメソッドがあれば追加すること
    
    public static void main(String[] args){
	return;
    }
}
