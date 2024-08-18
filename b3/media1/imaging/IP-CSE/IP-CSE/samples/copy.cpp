// 画像のコピーを行うサンプルプログラム

#include <stdio.h>
#include <opencv2/opencv.hpp>

// java の import に近い命令
// あらかじめこれを指定することで opencv のクラスをそのまま使用できる
// これを書かない場合は，cv::Mat のように書く必要がある
// java の import.util.* に似たものだと思えば良い
// 興味があれば詳細は各自で調べること
using namespace cv; 


int main(int argc, char** argv){
  Mat_<Vec3b> image, output(cv::Size(640,480),0);
  // Mat は opencv における行列を表現するクラス
  // Mat_<xxx> の xxx の部分を変化させることで様々な行列を使用可能
  // 今回は Vec3b型（Byte型の3つの配列）の行列を確保
  // 画像を使用する場合はだいたいこれでOK

  // 画像の読み込み result.png を読み込む
  image = imread("./result.png",1);

  // 読み込み失敗の場合はエラーを表示して終了
  if ( !image.data ){
    printf("No image data.\n");
    return -1;
  }

  // 読み込んだ画像と同じサイズの画像を作成する
  // Mat_<Vec3b> で Vec3b の行列を作成
  // コンストラクタは Mat_<Vec3b>(画像サイズ, 初期値)
  // 画像サイズは cv::size  クラスにより表現

  // たとえば、640,480 のサイズの画像をつくる場合は以下の通り
  // Mat_<Vec3b> img(cv::size(640,480), 0);

  // あるいは
  // Mat_<vec3b> img;
  // img = Mat_<Vec3b>(cv::size(640,480), 0)
  
  output = Mat_<Vec3b>(cv::Size(image.size().width, image.size().height));
  // image.size() により画像サイズを取得可能
  // cv::size 構造体は width, height の2要素を持つ
  // cv::size.width: 画像の横幅
  // cv::size.height: 画像の縦幅

  //output = Mat_<Vec3b>(image.size(), 0);
  // ホントはこれでかまわないが、例のために上のように記述
  
  for(int y=0; y<image.size().height; y++){
    for(int x=0; x<image.size().width; x++){
      for(int c=0; c<image.channels(); c++){
	// 座標、(x,y), channel c(=0,1,2) のデータ位地を計算
	int src =
	  y * output.step + // 画像における横一列のデータ位地
	  x * output.elemSize() + // 一列中のデータ位地
	  c;
	// データを同じ座標にコピー
	int dst =
	  y * output.step + // 画像における横一列のデータ位地
	  x * output.elemSize() + // 一列中のデータ位地
	  c;

	output.data[dst] = image.data[src];

	// 画像はを左右反転する場合は以下のようになる
	/*
	int dst =
	  y * output.step +
	  (output.cols - x) * elemSize() +
	  c;
	*/

	// RGB -> BGR
	/* RGB 画像を BGR 画像に変換する場合は以下の通り
	int dst = 
	  y * output.step +
	  x * elemSize() +
	  2 - c;
	*/ 
	
      }
    }
  }

  // 画像を表示
  // まずは  Window を作成
  namedWindow("Display Image1",WINDOW_AUTOSIZE);
  // 作成したウィンドウに入力画像を表示
  imshow("Display Image1", image);

  // 結果画像表示用 Window
  namedWindow("Display Image2",WINDOW_AUTOSIZE);
  // 結果を表示
  imshow("Display Image2", output);
  waitKey(0);

  // 結果を画像に保存
  // imwrite(ファイル名, 保存したい行列);
  imwrite("copy.png", output);

  return 0;
}
