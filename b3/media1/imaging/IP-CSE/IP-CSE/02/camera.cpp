// camera capturing functions by opencv

#include <opencv2/opencv.hpp>
#include "camera.h"
#include <stdio.h>

using namespace cv;
using namespace std;

static string InputFile("input/input%03d.jpg");
static int FromFile = 0;
static VideoCapture Cap;
static Mat ImgDef;
static const int ImageNum = 150;

int openCamera(void){
  // camera open
  Cap.open(0);
  if (!Cap.isOpened())
    FromFile = 1;
  return 0;
}

int openCamera(char *input){
  InputFile = string(input);
  return 0;
}


Mat getImage(void){
  // カメラ or ファイルから画像取り込み
  static int num = 0;

  Mat frame;
  if (Cap.isOpened()){
    // ファイル読み込み
    Cap >> frame;
  }
  if (!frame.data){
    // 読み込み失敗した場合もデフォルト画像を使う
    char buff[256];
    sprintf(buff,&InputFile[0],num);
    frame = imread(buff);
    num = (num + 1) % ImageNum;
  }
  
  return frame.clone();
}

int saveImage(string pre, Mat img, Mat imgIn){
  return saveImage(pre,img, imgIn, 1);
}
  
int saveImage(string pre, Mat img, Mat imgIn, int inc){
  // 入力画像についても同時に保存する
  static int num = 0;
  char buff[4];

  sprintf(buff,"%02d",num);
  string name = pre + buff;
  imwrite(name+".png",img);
  imwrite(name+"-in.png",imgIn);
  num += inc;

  return 0;
}

// mouse 操作のための関数
void mouse_function(int event, int x, int y, int flag, void *data){
  // 左ボタンが押された場合に以下を実行(詳細は検索)
  dataset *set = (dataset*)data;

  if (event == CV_EVENT_LBUTTONDOWN){
    Mat *img = set->frame; // キャプチャ画像を取得
    // x, y がウィンドウ上のクリック位置なので，その輝度値を表示
    // 詳しくは検索
    cout << "(" << x << "," << y << ")  " << img->at<Vec3b>(y,x) << endl;
    set->x = x;
    set->y = y;
    set->click = 1;
  }
}

void copyArea(Mat &in, Mat &out, int x, int y){
  // 指定された領域を out の大きさに合わせてコピー
  if (x + out.size().width > in.size().width)
    x = in.size().width - out.size().width;
  if (y + out.size().height > in.size().height)
    y = in.size().height - out.size().height;

  in(Rect(x, y, out.cols, out.rows)).copyTo(out);
}

int recordImage(Mat &img){
  static int num = 0;
  char buff[64];

  sprintf(buff,&InputFile[0],num);
  imwrite(buff,img);
  num++;
  if (num >= ImageNum){
    num = 0;
    return 0;
  }
  return 1;
}
  
