// 以下に必要な記述を追加せよ
import java.util.*;
import java.io.*;

class Edge{
    private int to;
    Edge(int to){this.to = to;}
    int To(){return to;}
}

class Node{
    int id;
    ArrayList<Edge> list;
    Node(int id){
	// 適切に記述
    }
    void addToList(int nid){
	// 適切に記述
    }
    ArrayList<Edge> getList(){
	// 適切に記述，下記も変更の必要あり
	return null;
    }
    // その他必要なものがあれば適当に作成
}

public class Graph{
    // 頂点のリスト
    // 配列であれば
    int num;
    Node [] nodes;
    
    // 可変長リストであれば
    //ArrayList<Node> nodes;
    
    void printGraph(){
	// Graph を表示
    }

    void loadGraph(String filename){
	// グラフを詠み込み
	// コンストラクタで使用
    }
    
    Graph(String filename){
    }
}

