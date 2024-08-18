// 画像の平滑化（テキストpp.6-7）
// q が押されるとプログラムが終了する
// w が押されると画像を保存

#include <iostream>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include "camera.h"
#include "pixel.h"

using namespace std;
using namespace cv;

static const string ResultFile("smooth-");


//h_patternが0なら移動平均フィルタ、1ならガウシアンフィルタ
void smoothing_transformation(Mat& input, Mat& output,int h_pattern,int degree){

  if(degree%2 == 0){
     cout << "degree is even." << endl;
     exit(1);
  }
  double h[degree][degree];

  for(int i = 0;i<degree;i++){
    for(int j = 0;j<degree;j++){
      h[i][j] = 0;
    }
  }



  switch (h_pattern)
  {
  case 0://移動平均フィルタ
    for(int i = 0;i<degree;i++){
      for(int j = 0;j<degree;j++){
        h[i][j] = 1;
        h[i][j] /= degree*degree;
      }
    }
  break;
  case 1://ガウシアンフィルタ
  switch(degree){
    case 3:{
    double tmp_h[3][3] = 
    {{(double)1/16,(double)2/16,(double)1/16},
    {(double)2/16,(double)4/16,(double)2/16},
    {(double)1/16,(double)2/16,(double)1/16}};
    for(int i = 0;i<degree;i++){
      for(int j = 0;j<degree;j++){
        h[i][j] = 0;
        h[i][j] = tmp_h[i][j];
      }
    }
    break;
    }
    case 5:{
    double tmp_h[5][5] = 
    {{(double)1/256,(double)4/256,(double)6/256,(double)4/256,(double)1/256},
    {(double)4/256,(double)6/256,(double)24/256,(double)6/256,(double)4/256},
    {(double)6/256,(double)24/256,(double)36/256,(double)24/256,(double)6/256},
    {(double)4/256,(double)6/256,(double)24/256,(double)6/256,(double)4/256},
    {(double)1/256,(double)4/256,(double)6/256,(double)4/256,(double)1/256}};
    for(int i = 0;i<degree;i++){
      for(int j = 0;j<degree;j++){
        h[i][j] = 0;
        h[i][j] = tmp_h[i][j];
      }
    }
    break;
    }
  }
  
  default:
    break;
  }
  for(int x=0;x<input.size().width;x++){
    for(int y=0;y<input.size().height;y++){
      for(int c=0;c<input.channels();c++){
        char smoothPix = 0;
        for(int i = 0;i<degree;i++){
          for(int j = 0;j<degree;j++){
            smoothPix += getPixel(input,x-degree/2+i,y-degree/2+j,c)*h[i][j];
          }
        }
        setPixel(output,x,y,c,smoothPix);
      }
    }
  }
}


double uni_noise(double min, double max){
  // min 以上，max 以下の一様乱数を発生させる
  // 例えば -1 から 1 の乱数を発生させる場合は
  // uni_noise(-1,1)
  // のようにすればよい
  if (min >= max) return 0;

  return ((double)random()/RAND_MAX)*(max-min)+min;
}

int image_process(Mat &input, Mat &output,int process, int key){
  // 画像処理本体を記述
  // 押されたキーにしたがって異なる処理を実行する
  switch(process){
  case '3':
    // 3が押された場合の処理
    smoothing_transformation(input,output,0,3);
    break;
  case '2':
    // 2が押された場合の処理
    smoothing_transformation(input,output,0,5);
    break;
  case '1':
    // 1が押された場合の処理
    smoothing_transformation(input,output,1,3);
    break;
  default:
  case '0':
    // 0が押された場合 or それ以外の処理
    // affine と同様に関数を作成すること
    smoothing_transformation(input,output,1,5);
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
