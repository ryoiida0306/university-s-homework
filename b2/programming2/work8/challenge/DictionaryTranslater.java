// 以下に必要な記述を追加せよ
// html のヘッダ部分とフッタ部分の出力には
// printHTMLHeader と printHTMLFotter を使用してもよい
// iframe 内への表示については sample.html を参考にすること

public class DictionaryTranslater{
    static void printHTMLHeader(){
	// HTML のヘッダ部分
	System.out.println("<!DOCTYPE html>\n"+
			   "<html lang=\"ja\">\n"+
			   "<head>\n"+
			   "<meta charset=\"UTF-8\">\n"+
			   "<title>DictionaryTranslater</title>\n"+
			   "</head>\n"+
			   "<body>\n"+
			   "<iframe name=\"iframe\">"+
			   "</iframe>");
    }

    static void printHTMLFooter(){
	System.out.println("</body>\n"+
			   "</html>");
    }

    public static void main(String[] args){
	printHTMLHeader();
	printHTMLFooter();
	return;
    }
}
