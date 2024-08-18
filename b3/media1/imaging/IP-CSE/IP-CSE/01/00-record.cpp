// 画像の録画
// q が押されるとプログラムが終了する
// w が押されると5秒分（150frame）の画像を保存

#include <iostream>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include "camera.h"
#include "pixel.h"

using namespace std;
using namespace cv;

int main(int argc, char** argv) {
  cv::Mat frame; // 画像表現のためのクラス，詳しくは copy.cpp 参照
  int process = '0'; // 画像処理の種類を指定する，デフォルトは'0'
  int record = 0;

  openCamera();
    
  // 1枚取り込み
  frame = getImage();

  if (!frame.data) {
    printf("No iamge data\n");
    return -1;
  }

  namedWindow("video", 1); // 画像表示 Window 作成

  while (1) {
    frame = getImage();
    imshow("video", frame); // 取り込んだ画像を表示する

    char key = waitKey(30); // 押されたキーにより処理を変更する

    if (key == 'w') {
      // w が押された場合画像保存スタート
      cout << "Image recording start." << endl;
      record = 1;
    }

    if (record){
      record = recordImage(frame);
      if (!record)
	cout << "Image recording end." << endl;
    }else if (key == 'q') {
      // q が押された場合終了
      break;
    }
  }
    

  return 0;
}
