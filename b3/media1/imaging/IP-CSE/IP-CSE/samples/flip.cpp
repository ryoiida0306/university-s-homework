#include <stdio.h>
#include <opencv2/opencv.hpp>
using namespace cv;

int main(int argc, char** argv){
	Mat_<Vec3b> image, output;
	image = imread("./result.jpg",1);
	if ( !image.data ){
		printf("No image data \n");
		return -1;
	}
	output = Mat_<Vec3b>(image.size(), 0);

	for(int y=0; y<image.size().height; y++){
	  for(int x=0; x<image.size().width; x++){
	    for(int c=0; c<image.channels(); c++){
	      output.data[y*output.step+(output.cols-x)*output.elemSize()+c] =
		image.data[y*image.step+x*image.elemSize()+c];
	    }
	  }
	}
	
	namedWindow("Display Image1",WINDOW_AUTOSIZE);
	imshow("Display Image1", image);
	namedWindow("Display Image2",WINDOW_AUTOSIZE);
	imshow("Display Image2", output);
	waitKey(0);
	return 0;
}
