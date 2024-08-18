// 画像のアフィン変換（テキストpp.4-6）
// まずは，pixel.h を完成させた後，それを利用するとやりやすいので留意すること
// q が押されるとプログラムが終了する
// w が押されると画像を保存
// キーボードのキーを押すことでパラメタを変化させられる．
// キーの詳細は image_process または， print_controlを参照

#include <iostream>
#include <string>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include <math.h>
#include "camera.h"
#include "pixel.h"

using namespace std;
using namespace cv;

static const string InputFile("input.png");
static const string ResultFile("affine-");


void affine_transformation(Mat& input, Mat& output,double sx, double sy, double theta, int tx, int ty) {
  // アフィン変換を行う
  // 以下の手順で行うとよい．
  // 0. 指導書 p.4 に掲載されたリストを参考にして
  //    pixel.h 内部の getPixel, setPixel を完成させる
  //    getPixel(img,x,y,c) は，img の座標(x,y)，チャネルcの値を取得する関数
  //    setPixel(img,x,y,c,pix)はimg の座標(x,y)，チャネルcにpixを代入する関数
  //    リスト内の6行目が特に重要
  //
  // 1. setPixelが完成したら，同様にp.4の内容を参考に
  //    inputの中身をoutputにコピーする関数としてこの関数を完成させる
  //    指導書内の例では，imgの座標(x,y)，チャネルcの値を順番に表示させている
  //    これを先ほど作成した setPixel, getPixel を使って置き換えることで
  //    input のすべての座標，すべてのチャネルの内容を outputへとコピー
  //
  //    ここまで完成したら，ひとまず実行してみて画像がコピーされた画像が表示
  //    されることを確認する．
  // 
  //  2. このあとは，アフィン変換により入力画像の(x,y)が出力（変換画像）の
  //     どの座標に対応するのかをp.5の 式(6)に従い計算し，単純にコピーするのでは
  //     なく，変換を施した画像が作成できることを確認（省略してもよい）
  //
  //  3. 最後に式(10)を完成させ，output の(x,y)に対応する入力画像の(xd,yd)を
  //     計算するプログラム作成し，これを用いてコピーすることで抜けのない
  //     変換画像を作成するプログラムを作成する
  
  for(int x=0;x<input.size().width;x++){
    for(int y=0;y<input.size().height;y++){
      for(int c=0;c<input.channels();c++){
        setPixel(output,x,y,c,0);
        int dx = ((x-tx)*cos(theta/180*M_PI)+(y-ty)*sin(theta/180*M_PI))/sx;
        int dy = (-(x-tx)*sin(theta/180*M_PI)+(y-ty)*cos(theta/180*M_PI))/sy;
        if(dx<0||input.size().width<=dx||dy<0||input.size().height<=dy){continue;}
        setPixel(output,x,y,c,getPixel(input,dx,dy,c));

      }
    }
  }
  

}

static void print_param(double sx, double sy, double theta, int tx, int ty){
  printf("theta = %f deg, t = (%d, %d), s = (%f, %f)\n",
	 theta, tx, ty, sx, sy);
  return;
}

static void print_control(void){
  printf("Control-parameters\n"
	 "(z,c): left, right, (s,x): up, down, (a,d): rotate\n"
	 "(f,v):Hori-zoom-in,out, (g,b): Ver-zoom-in,out\n");
}

int image_process(Mat& input, Mat& output, int process, char key) {
  // 画像処理本体を記述
  // 押されたキーにしたがって異なる処理を実行する
  // & をつけておくことで，数値渡しではなく参照渡しとなるので
  // 関数内と関数外で同一の画像を参照することができるようになる．
  static double sx=1.0, sy = 1.0;
  static double theta = 30;
  static int tx = 0, ty = 0;

  switch (key){
  case 'z':
    tx = tx - 10;
    break;
  case 'c':
    tx = tx + 10;
    break;
  case 's':
    ty = ty - 10;
    break;
  case 'x':
    ty = ty + 10;
    break;
  case 'a':
    theta += 5;
    break;
  case 'd':
    theta -= 5;
    break;
  case 'f':
    sx += 0.1;
    break;
  case 'v':
    sx -= 0.1;
    break;
  case 'g':
    sy += 0.1;
    break;
  case 'b':
    sy -= 0.1;
    break;
  }

  if (key > 0)
    print_param(sx,sy,theta,tx,ty);

  switch (process) {
  case '1': 
    // 1が押された場合の処理
    break;
  case '0':
  default: 
    // 0が押された場合 or デフォルト
    affine_transformation(input, output,sx, sy, theta, tx, ty);
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

  print_control();
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
