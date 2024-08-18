// 画像の濃度変換（テキストpp.7-8）
// 押されたキーによって明るさの範囲を変動させるなどできるようにすると
// どのような変化が発生するかが確認しやすくなる

// q が押されるとプログラムが終了する
// w が押されると画像を保存

#include <iostream>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include "camera.h"
#include "pixel.h"

using namespace std;
using namespace cv;


static const string ResultFile("contrast-");
double linearFunction(double z,double a,double b,double zm){
  if(z<a){return 0;}
  if(b<z){return zm;}
  return (z-a)/(b-a)*zm;
}
void linearContrast_transformation(Mat& input, Mat& output,double a,double b ,double zm){

  for(int x = 0;x < input.size().width;x++){
    for(int y = 0; y<input.size().height;y++){
      for(int c = 0; c<input.channels();c++){
        setPixel(output,x,y,c,linearFunction(getPixel(input,x,y,c),a,b,zm));
      }
    }
  }

}

double not_linearFunction(double z,double gamma,double zm){
  
  return zm*pow(z/zm,gamma);
}

void not_linearContrast_transformation(Mat& input, Mat& output,double gamma ,double zm){

  for(int x = 0;x < input.size().width;x++){
    for(int y = 0; y<input.size().height;y++){
      for(int c = 0; c<input.channels();c++){
        setPixel(output,x,y,c,not_linearFunction(getPixel(input,x,y,c),gamma,zm));
      }
    }
  }

}

int image_process(Mat &input, Mat &output,int process, int key){
  // 画像処理本体を記述
  // 押されたキーにしたがって異なる処理を実行する
  switch(process){
  case '1':
    // 1が押された場合の処理
    not_linearContrast_transformation(input,output,100,255);

    break;
  default:
  case '0':
    // 0が押された場合 or それ以外の処理
    linearContrast_transformation(input,output,150,250,60);
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
      saveImage(ResultFile, output,frame);
    }
    else if (key == 'q') {
      // q が押された場合終了
      break;
    }
  }
    

  return 0;
}
