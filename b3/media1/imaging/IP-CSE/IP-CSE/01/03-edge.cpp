// 画像からのエッジ検出（pp.6-7）

// 明るさの表示範囲に留意すること
// 一般的な画像では明るさ（輝度）が unsigned char により表現されるため
// (0 - 255)の範囲となる．
// 一方，図5のフィルタを適用した場合，明るさがこの範囲を超過することがある．
// 適切な範囲となるように調整すること

// この問題を解く前に，濃度変換に関する課題に取り組むと，
// どのような処理を加えればよいかがわかりやすい

// まずは，pixel.h を完成させた後，それを利用するとやりやすいので留意すること
// q が押されるとプログラムが終了する
// w が押されると画像を保存

#include <iostream>
#include <string>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include "camera.h"
#include "pixel.h"

using namespace std;
using namespace cv;

static const string ResultFile("edge-");
//h_patternが0のときSobelフィルタ、1のときlaplacianフィルタ
void edge_transformation(Mat& input, Mat& output ,int h_pattern){
  double h1[3][3];
  double h2[3][3];

  switch (h_pattern)
  {
  case 0:{
  // double h1_sub[3][3] = {{-1,0,1},{-2,0,2},{-1,0,1}};
  // double h2_sub[3][3] = {{-1,-2,-1},{0,0,0},{1,2,1}};
  double h1_sub[3][3] = {{1,2,1},{0,0,0},{-1,-2,-1}};
  double h2_sub[3][3] = {{1,2,1},{0,0,0},{-1,-2,-1}};
  for(int i = 0;i<3;i++){
    for(int j =0;j<3;j++){
      h1[i][j] = h1_sub[i][j];
      h2[i][j] = h2_sub[i][j];
    }
  }
  break;
  }
  case 1:{
  double h1_sub[3][3] = {{-1,-1,-1},{-1,8,-1},{-1,-1,-1}};
  double h2_sub[3][3] = {{-1,-1,-1},{-1,8,-1},{-1,-1,-1}};
  for(int i = 0;i<3;i++){
    for(int j =0;j<3;j++){
      h1[i][j] = h1_sub[i][j];
      h2[i][j] = h2_sub[i][j];
    }
  }
  break;
  }
  default:
  cout << "this h_pattern is not defined." << endl;
    break;
  }

  for(int x=0;x<input.size().width;x++){
    for(int y=0;y<input.size().height;y++){
      for(int c=0;c<input.channels();c++){
        char smoothPix_1 = 0;
        char smoothPix_2 = 0;
        for(int i = 0;i<3;i++){
          for(int j = 0;j<3;j++){
            for(int k = 0;k<3;k++){
              smoothPix_1 += getPixel(input,x-1+i,y-1+j,k)*h1[i][j];
              smoothPix_2 += getPixel(input,x-1+i,y-1+j,k)*h2[i][j];

            }
          }
        }
        // smoothPix /= degree*degree;
        setPixel(output,x,y,c,sqrt(pow(smoothPix_1,2)+pow(smoothPix_2,2)));
      }
      //setPixel(output,x,y,c,getPixel(input,x,y,c));
    }
  }
  // cout << h[0][0] << endl;
}

int image_process(Mat input, Mat output,int process, int key){
  // 画像処理本体を記述
  // 押されたキーにしたがって異なる処理を実行する
  switch(process){
  case '1':
    // 1が押された場合の処理
    edge_transformation(input,output,1);

    break;
  default:
  case '0':
    // 0が押された場合 or それ以外の処理
    // affine と同様に関数を作成すること
    edge_transformation(input,output,0);

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
