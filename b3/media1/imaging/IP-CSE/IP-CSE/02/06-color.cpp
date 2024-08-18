// 色による領域検出処理（pp.9-10）
// マウスで表示画像をクリックすることで，色を確認できる
// 指定した色「以外」の領域を 1/5 の明るさで表示させることで，検出領域が
// 目立って表示されるようにプログラムを作成すること．

// q が押されるとプログラムが終了する
// w が押されると画像を保存

#include <iostream>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include "camera.h"
#include "pixel.h"

using namespace std;
using namespace cv;

static const string ResultFile("color-");


int range(double z,int min,int max){
  if(min<=z&&z<=max){return 1;}
  return 0;
}
//Rages:bluemin,bulemax,greenmin,greenmax,redmin,redmax
void color_transformation(Mat& input, Mat& output,int Ranges[1][6]){
  for(int x = 0;x < input.size().width;x++){
    for(int y = 0; y<input.size().height;y++){
      for(int i = 0;i<1;i++){
        //cout << range(getPixel(input,x,y,0),Ranges[i][0],Ranges[i][1]) <<endl;
        if(range(getPixel(input,x,y,0),Ranges[i][0],Ranges[i][1])==0&&range(getPixel(input,x,y,1),Ranges[i][2],Ranges[i][3])==0&&range(getPixel(input,x,y,2),Ranges[i][4],Ranges[i][5])==0){
          for(int c = 0; c<input.channels();c++){
            setPixel(output,x,y,c,getPixel(input,x,y,c)/5);
          }
        }else{
          for(int c = 0; c<input.channels();c++){
            setPixel(output,x,y,c,getPixel(input,x,y,c));
          }
        }
      }
    }
  }

}


int image_process(Mat &input, Mat &output,int process,int click, int x, int y, int key){
  // 画像処理本体を記述
  // 押されたキーにしたがって異なる処理を実行する
  // click はマウスがクリックされたか否か，
  // x, y は最後にマウスがクリックされた場所を示す
  
  if (click){
    // マウスがクリックされた場合の処理はここに書くと良い
    // 例えば，色の範囲を変化させるなど
    // Ranges[1][6] = {{getPixel(input,x,y,0)-10,getPixel(input,x,y,0)+10,getPixel(input,x,y,1)-10,getPixel(input,x,y,1)+10,getPixel(input,x,y,2)-10,getPixel(input,x,y,2)+10}};
    int diff = 50;
    int Ranges[1][6]= {{getPixel(input,x,y,0)-diff,getPixel(input,x,y,0)+diff,getPixel(input,x,y,1)-diff,getPixel(input,x,y,1)+diff,getPixel(input,x,y,2)-diff,getPixel(input,x,y,2)+diff}};
    color_transformation(input,output,Ranges);
  }

  switch(process){
  case '1':
    // 1が押された場合の処理
    break;
  default:
  case '0':
    // 0が押された場合 or それ以外の処理
    // int Ranges[1][6] = {{0,100,0,100,0,100}};//218,192,161
    //color_transformation(input,output,Ranges);
    break;
    
  }
  return 0;
}

int main(int argc, char** argv) {
  cv::Mat frame; // 画像表現のためのクラス，詳しくは copy.cpp 参照
  cv::Mat output; // 処理結果を格納
  int process = '0'; // 画像処理の種類を指定する，デフォルトは'0'
  int image_num = 0;
  dataset set={0,0,0};

  // カメラから画像の取り込みの場合
  if (argc > 1)
    openCamera(argv[1]); // camera open
  else
    openCamera();
    
  // 1枚取り込み
  frame = getImage();
  set.frame = &frame;

  if (!frame.data) {
    printf("No iamge data\n");
    return -1;
  }

  // 同サイズの画像を生成（必要があれば変更してよい）
  output = Mat_<Vec3b>(frame.size(), 0);

  namedWindow("video", 1); // 画像表示 Window 作成
  setMouseCallback("video",mouse_function, &set);
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
    image_process(frame, output, process, set.click, set.x, set.y, key);
    imshow("result", output); // 処理結果を表示する
    set.click = 0;

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
