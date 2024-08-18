// フレーム間差分処理

// q が押されるとプログラムが終了する
// w が押されると画像を保存

#include <iostream>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include "camera.h"
#include "pixel.h"

using namespace std;
using namespace cv;

static const string ResultFile("frame-");

void frame_transformation(Mat& input,Mat& prev, Mat& output){

  for(int x = 0;x < input.size().width;x++){
    for(int y = 0; y<input.size().height;y++){
      for(int c = 0; c<input.channels();c++){
        setPixel(output,x,y,c,abs(getPixel(prev,x,y,c)-getPixel(input,x,y,c)));
      }
    }
  }

}

int image_process(Mat &input, Mat &prev, Mat &output,int process){
  // 画像処理本体を記述
  // prev は前フレームの画像
  // 押されたキーにしたがって異なる処理を実行する
  switch(process){
  case '1':
    // 1が押された場合の処理
    break;
  default:
  case '0':
    // 0が押された場合 or それ以外の処理
    frame_transformation(input,prev,output);
    break;
    
  }
  return 0;
}

int main(int argc, char** argv) {
  Mat frame; // 画像表現のためのクラス，詳しくは copy.cpp 参照
  Mat framePrev;; 
  Mat output; // 処理結果を格納
  int process = '0'; // 画像処理の種類を指定する，デフォルトは'0'
  int image_num = 0;

  // カメラから画像の取り込みの場合
  if (argc > 1)
    openCamera(argv[1]); // camera open
  else
    openCamera();
    
  // 1枚取り込み
  frame = getImage();
  framePrev = frame.clone();

  if (!frame.data) {
    printf("No iamge data\n");
    return -1;
  }

  // 同サイズの画像を生成（必要があれば変更してよい）
  output = Mat_<Vec3b>(frame.size(),0);
  
  namedWindow("video", 1); // 画像表示 Window 作成
  namedWindow("result", 1); // 結果画像表示 Window 作成

  while(1){
    // 画像を1枚取り込み
    frame = getImage();
    imshow("video", frame); // 取り込んだ画像を表示する
    
    char key = waitKey(30); // 押されたキーにより処理を変更する
    
    // 処理の切り替え
    // 数字の 0 - 9 が押された場合は処理(process)を切り替える
    if (key >= '0' && key <='9')
      process = key;
      
    // 画像処理を行う
    image_process(frame,framePrev,output,process);
    imshow("result", output); // 処理結果を表示する

    // 現在の画像を次のループの前フレーム画像として保存
    framePrev = frame.clone();
    
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
