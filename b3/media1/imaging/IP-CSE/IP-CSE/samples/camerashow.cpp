#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;

// OpenCV を利用してカメラから画像を取得して表示するサンプルプログラム

int main(int argc, char** argv) {
  VideoCapture cap; // カメラから画像を取得するためのクラス

  if(argc > 1) // デバイスが指定されている場合はそのカメラをオープン
    cap.open(string(argv[1]));
  else
    cap.open(0);

  Mat frame; // 画像表現のためのクラス，詳しくは copy.cpp 参照

  cout << " q: quit" << endl;
  cout << " w: save image" << endl;

  namedWindow("video", 1); // 画像表示 Window 作成
  for(;;) {
    cap >> frame; // 画像をカメラから1枚取り込む

    if(!frame.data) // 取り込みに失敗した場合は終了する
      break;

    imshow("video", frame); // 取り込んだ画像を表示する

    char key = waitKey(30);// 30msの間に何かキーが押されるのを待つ

    if (key == 'q') // q の場合は終了
      break;
    if (key == 'w') // w の場合は画像保存
      imwrite("result.png", frame);

  }
  return 0;
}
