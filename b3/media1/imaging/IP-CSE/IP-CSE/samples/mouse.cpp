// マウスを使う例
#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;

// template image
static Mat_<Vec3b> tmpImg;

// マウスがクリックされた場合にこの関数が呼ばれる
void mouse_function(int event, int x, int y, int flag, void *data){
  // 左ボタンが押された場合に以下を実行(詳細は検索)
  if (event == CV_EVENT_LBUTTONDOWN){
    Mat img = *(Mat*)data; // キャプチャ画像を取得

    // x, y がウィンドウ上のクリック位地なので、その周辺をコピー
    // 詳しくは検索
    std::cout << x << ", " << y << std::endl;
    img(Rect(x-tmpImg.cols/2, y - tmpImg.rows/2, tmpImg.cols, tmpImg.rows)).copyTo(tmpImg);
    imshow("template",tmpImg);
    waitKey(1);
  }
}

int main(int argc, char** argv){
  VideoCapture cap;
  Mat frame;
  
  tmpImg = cv::Mat_<Vec3b>(Size(32,32),0);

  cap.open(0);
  cap >> frame;
  if (frame.data == NULL) return 0;

  // マウスを使う準備
  namedWindow("Window");
  setMouseCallback("Window", mouse_function, &frame);
  
  while(1){
    cap >> frame;
    imshow("Window", frame);
    char key = waitKey(30);
    if (key == 'q')
      break;
  }
  
  return 0;
}
