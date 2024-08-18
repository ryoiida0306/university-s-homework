#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;
using namespace std;

static const string DefName("result.png");

int main(int argc, char** argv){
  Mat image;

  if (argc>1)
    image = imread(argv[1]);
  else
    image = imread(DefName,1);

  if ( !image.data ){
    printf("No image data \n");
    return -1;
  }
	
  // Window を作成して
  namedWindow("Display Image",WINDOW_AUTOSIZE);
  // 画像を表示
  imshow("Display Image", image);

  // 何かキーが押されれば終了
  waitKey(0);

  return 0;
}
