CC	= g++ 
PKGCFG	= PKG_CONFIG_PATH=/opt/cse/pkg/opencv/lib64/pkgconfig pkg-config
CXXFLAGS	= -g `${PKGCFG} --cflags opencv`
LIBS 	= -lm `${PKGCFG} --libs opencv`
PROGS	= back frame template

all: ${PROGS}

back: 07-back.o camera.o
	${CC} -o $@ $^ ${LIBS}

frame: 08-frame.o camera.o
	${CC} -o $@ $^ ${LIBS}

template: 09-template.o camera.o
	${CC} -o $@ $^ ${LIBS}

clean:
	\rm -f *.o *~ ${PROGS}
