import java.util.Scanner;
import java.io.*;

// テキストファイルを1行ずつ、読みこんで大文字に変換して出力するクラス
class TextToUpper {
    static void readAndConvert(String filename)  {
        Scanner scanner = new Scanner(new File(filename));while (scanner.hasNextLine()) {
            String line = scanner.nextLine();
            System.out.println(line.toUpperCase());
        }
        scanner.close();
    }
}
