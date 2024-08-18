CXX		= g++ 
PKGCFG		= PKG_CONFIG_PATH=/opt/cse/pkg/opencv/lib64/pkgconfig pkg-config
CXXFLAGS	= -g `${PKGCFG} --cflags opencv`
LIBS		= -lm `${PKGCFG} --libs opencv`
PROGS		= cameratopng camerashow pngshow flip copy mouse


all: ${PROGS}

cameratopng: cameratopng.o
	${CXX} -o $@ $^ ${LIBS}

camerashow: camerashow.o
	${CXX} -o $@ $^ ${LIBS}

pngshow: pngshow.o
	${CXX} -o $@ $^ ${LIBS}

flip: flip.o
	${CXX} -o $@ $^ ${LIBS}

copy : copy.o
	${CXX} -o $@ $^ ${LIBS}

mouse : mouse.o
	${CXX} -o $@ $^ ${LIBS}

clean:
	\rm -f *.o ${PROGS} *~
