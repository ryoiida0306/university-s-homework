// 以下に必要な記述を追加せよ
// 以下の記述は例であるため，変更してもよい

import java.util.Scanner;
import java.io.File;

class Dictionary{
    private int wordNum = 46725;
    // 辞書に含まれる行数

    // 他に課題で必要なフィールドを追加すること

    public Dictionary(String filename){
	// 講義資料に記載されているものと同じである．
	// 適宜記述を追加すること
	try{
	    Scanner scan = new Scanner(new File(filename));
	    for (int i=0;i<wordNum;i++){
		if (!scan.hasNextLine()){
		    // 次の行が読み込めない場合の処理
		    // 辞書ファイルが想定よりも短い場合に実行
		    // 通常は実行されない
		    break;
		}
		String line = scan.nextLine();
		// line には1行全ての文字が含まれるため
		// 英単語と和訳に適切に分割して格納すること
		// 以下に記述を追加

		// これは行が読み込めているかどうかを確認するための表示
		// 不要なので実際の処理では削除すること
		System.out.println(line);

	    }
	}catch(java.io.FileNotFoundException e){
	    System.out.println(e);
	    System.exit(0);
	}
    }
    // 以下に Dictionary クラスで指定されたメソッドを追加すること
}

public class DictionaryTester{
    public static void main(String[] args){
	return;
    }
}
