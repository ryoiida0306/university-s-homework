// 画素を取り扱うためのインライン関数の定義
// 必要があれば適切に記述の後，使用しても良い
// sample/copy.cpp を参考にすること

#pragma once

#include <opencv2/opencv.hpp>

static inline unsigned char getPixel(cv::Mat img, int x, int y, int c){
  // ここでは座標(x,y)におけるc（0-2）チャネルの値を取得する
  unsigned char pix=0;
  // 0 の部分を適切に変更することで，pix に適切な値を代入すること
  pix = img.data[y*img.step+x*img.channels()+c];
  return pix;
}

static inline void setPixel(cv::Mat img, int x, int y, int c,unsigned char pix){
  // ここでは座標(x,y)のc(0-2）チャネルにpixを代入する
  // 以下のコメント部分を外し，の 0 の部分を適切に変更して
  // 画素への代入を実装せよ．

   img.data[y*img.step+x*img.channels()+c] = pix;
  return;
}

