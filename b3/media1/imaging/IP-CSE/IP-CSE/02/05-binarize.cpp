// 画像の2値化処理（pp.8-9）
// 濃度変換と同様にキーによってしきい値を変動させられる
// 変化がわかりやすい

// q が押されるとプログラムが終了する
// w が押されると画像を保存

#include <iostream>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include "camera.h"
#include "pixel.h"

using namespace std;
using namespace cv;

static const string ResultFile("binarize-");

double binariFunction(double z, double thre){
  if(z<thre){return 255;}
  return 0;
}

void binarize_transformation(Mat& input, Mat& output,int thre){

  for(int x = 0;x < input.size().width;x++){
    for(int y = 0; y<input.size().height;y++){
      char g1 = getPixel(input,x,y,0);
      char g2 = getPixel(input,x,y,1);
      char g3 = getPixel(input,x,y,2);
      for(int c = 0; c<input.channels();c++){
        setPixel(output,x,y,c,binariFunction(0.114*g1+0.586*g2+0.298*g3,thre));
      }
    }
  }

}


int image_process(Mat &input, Mat &output,int process, int key){
  // 画像処理本体を記述
  // 押されたキーにしたがって異なる処理を実行する

  // しきい値の値，デフォルトは中間値の128とする
  static int thre = 128;

  // キー操作によりしきい値を変化
  switch(key){
  case 'z':
    thre ++;
    if (thre > 255) thre = 255;
    break;
  case 'a':
    thre --;
    if (thre < 0) thre = 0;
  }
  

  switch(process){
  case '1':
    // 1が押された場合の処理
    break;
  default:
  case '0':
    // 0が押された場合 or それ以外の処理
    binarize_transformation(input,output,thre);
    break;
    
  }
  return 0;
}

int main(int argc, char** argv) {
  cv::Mat frame; // 画像表現のためのクラス，詳しくは copy.cpp 参照
  cv::Mat output; // 処理結果を格納
  int process = '0'; // 画像処理の種類を指定する，デフォルトは'0'
  int image_num = 0;

  // カメラから画像の取り込みの場合
  if (argc > 1)
    openCamera(argv[1]); // camera open
  else
    openCamera();
    
  // 1枚取り込み
  frame = getImage();

  if (!frame.data) {
    printf("No iamge data\n");
    return -1;
  }

  // 同サイズの画像を生成（必要があれば変更してよい）
  output = Mat_<Vec3b>(frame.size(), 0);

  namedWindow("video", 1); // 画像表示 Window 作成
  namedWindow("result", 1); // 結果画像表示 Window 作成

  while (1) {
    frame = getImage();
    imshow("video", frame); // 取り込んだ画像を表示する

    char key = waitKey(30); // 押されたキーにより処理を変更する

    // 処理の切り替え
    // 数字の 0 - 9 が押された場合は処理(process)を切り替える
    if (key >= '0' && key <='9')
      process = key;
      
    // 画像処理を行う
    image_process(frame, output, process, key);
    imshow("result", output); // 処理結果を表示する

    if (key == 'w') {
      // w が押された場合画像保存
      saveImage(ResultFile, output, frame);
    }
    else if (key == 'q') {
      // q が押された場合終了
      break;
    }
  }
    

  return 0;
}
