#pragma onece
#include <opencv2/opencv.hpp>
#include <string>

int openCamera(void);
int openCamera(char *input);

cv::Mat getImage(void);

// 画像保存用関数
int saveImage(std::string pre, cv::Mat img, cv::Mat imgIn, int inc);
int saveImage(std::string pre, cv::Mat img, cv::Mat imgIn);

// データ受け渡しのための構造体
typedef struct {
  cv::Mat *frame;
  int x;
  int y;
  int click;
} dataset;

void mouse_function(int event, int x, int y, int flag, void *data);
void copyArea(cv::Mat &in, cv::Mat &out, int x, int y);
int recordImage(cv::Mat &img);
