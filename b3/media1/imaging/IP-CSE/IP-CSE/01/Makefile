CXX		= g++ 
PKGCFG		= PKG_CONFIG_PATH=/opt/cse/pkg/opencv/lib64/pkgconfig pkg-config
CXXFLAGS	= -g `${PKGCFG} --cflags opencv`
LIBS		= -lm `${PKGCFG} --libs opencv`
PROGS		= affine smooth edge record


all: ${PROGS}

affine : 01-affine.o camera.o
	${CXX} -o $@ $^ ${LIBS}

smooth: 02-smooth.o camera.o
	${CXX} -o $@ $^ ${LIBS}

edge: 03-edge.o camera.o
	${CXX} -o $@ $^ ${LIBS}

record: 00-record.o camera.o
	${CXX} -o $@ $^ ${LIBS}

clean:
	\rm -f *.o ${PROGS} *~
