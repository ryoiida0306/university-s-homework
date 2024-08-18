// テンプレートマッチング
// マウスでクリックされた領域をテンプレートとして利用できる
// 検出結果をわかりやすい形で表示すること（四角で囲むなど）
// テンプレート画像は template.pngで保存される．

// q が押されるとプログラムが終了する
// w が押されると画像を保存

#include <iostream>
#include <stdio.h>
#include <opencv2/opencv.hpp>
#include "camera.h"
#include "pixel.h"

using namespace std;
using namespace cv;

static const string ResultFile("template-");

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

void template_transformation(Mat& input,Mat& temp, Mat& output){
double Diff[input.size().width][input.size().height];
  for(int x = 0;x < input.size().width;x++){
    for(int y = 0; y<input.size().height;y++){
      double diff = 0;//似ているほど小さい
      for(int c = 0; c<input.channels();c++){
        for(int px = 0;px<temp.size().width;px++){
          for(int py = 0;py<temp.size().height;py++){
            for(int pc = 0;pc<temp.channels();pc++){
              if(x+px<=input.size().width&&y+py<=input.size().height!=1){
                diff =1001001001001;
                continue;
              }
              diff += abs(getPixel(temp,px,py,pc)-getPixel(input,x+px,y+py,c+pc));
            }
          }
        }
        cout << "("<<x<<","<<y<<","<<diff<<")" << endl;
        // if(alpha>diff){
        //   for(int px = 0;px<temp.size().width;px++){
        //     for(int py = 0;py<temp.size().height;py++){
        //      for(int pc = 0;pc<temp.channels();pc++){
        //         if(x+px>input.size().width==1||y+py>input.size().height==1){continue;}
        //         setPixel(output,x+px,y+py,c+pc,getPixel(input,x+px,y+py,c+pc));
        //       }
        //     }
        //   }
        // }
        
      }
      Diff[x][y] = diff;
    }
  }
  int max_x = 0;
  int max_y = 0;
  for(int x = 0;x < input.size().width;x++){
    for(int y = 0; y<input.size().height;y++){
      if(Diff[max_x][max_y]>Diff[x][y]){
        max_x = x;
        max_y = y;
      }
    }
  }
  cout << max_x << " " << max_y <<endl;
  for(int px = 0;px<temp.size().width;px++){
    for(int py = 0;py<temp.size().height;py++){
      for(int c = 0;c<temp.channels();c++){
        if(max_x+px>input.size().width==1||max_y+py>input.size().height==1){continue;}
        setPixel(output,max_x+px,max_y+py,c,getPixel(input,max_x+px,max_y+py,c));
      }
    }
  }
}

int image_process(Mat &input, Mat &temp, Mat &output,int process, int key){
  // 画像処理本体を記述
  // 押されたキーにしたがって異なる処理を実行する
  switch(process){
  case '2':
    // 2が押された場合の処理
    binarize_transformation(input,output,32);
    break;
  case '1':
    // 1が押された場合の処理
    template_transformation(input,temp, output);
    break;
  default:
  case '0':
    // 0が押された場合 or それ以外の処理
    

    break;
    
  }
  return 0;
}

int main(int argc, char** argv) {
  cv::Mat frame; // 画像表現のためのクラス，詳しくは copy.cpp 参照
  cv::Mat output; // 処理結果を格納
  cv::Mat temp; // テンプレート画像
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

  // テンプレート画像用（とりあえず，32 x 32 とする）
  temp = Mat_<Vec3b>(Size(32,32), 0);
  
  namedWindow("video", 1); // 画像表示 Window 作成
  setMouseCallback("video",mouse_function, &set);
  namedWindow("template", 1); // テンプレート画像を表示
  namedWindow("result", 1); // 結果画像表示 Window 作成

  while (1) {
    frame = getImage();
    imshow("video", frame); // 取り込んだ画像を表示する
    
    char key = waitKey(30); // 押されたキーにより処理を変更する

    // 処理の切り替え
    // 数字の 0 - 9 が押された場合は処理(process)を切り替える
    if (key >= '0' && key <='9')
      process = key;
      
    // マウスがクリックされた場合，テンプレートを更新
    if (set.click){
      copyArea(frame,temp,set.x, set.y);
      set.click = 0;
    }
    imshow("template",temp);

    // 画像処理を行う
    image_process(frame, temp, output, process, key);
    imshow("result", output); // 処理結果を表示する

    if (key == 'w') {
      // w が押された場合画像保存
      saveImage(ResultFile, output, frame);
      // テンプレート画像については固定のファイル名で保存
      imwrite("template.png",temp);
    }
    
    if (key == 'q') {
      // q が押された場合終了
      break;
    }
  }
    

  return 0;
}
