#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;

// 画像を取り込んで保存するプログラム
// 保存ファイルのデフォルト名
std::string DefName("result.png");

int main(int argc, char **argv){
  VideoCapture capture(0); // カメラから画像を取り込むクラス
  Mat readImg; // 取り込んだ画像を保持するクラス

  do{
    capture >> readImg; // 画像を取り込んで
    imshow("Captured Image",readImg); // 表示
  }while(waitKey(30)>=0); // 何かキーが押されるまで待つ

  if (argc>1)
    imwrite(argv[1],readImg); // ファイル名が指定されている場合はそれで保存
  else
    imwrite(DefName,readImg); // なければ result.jpg で保存

  return 0;
}
