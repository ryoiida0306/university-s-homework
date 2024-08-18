CXX	= g++ 
PKGCFG	= PKG_CONFIG_PATH=/opt/cse/pkg/opencv/lib64/pkgconfig pkg-config
CXXFLAGS = -g `${PKGCFG} --cflags opencv`
LIBS = -lm `${PKGCFG} --libs opencv`
PROGS	= contrast binarize color

all: ${PROGS}

contrast : 04-contrast.o camera.o
	${CXX} -o $@ $^ ${LIBS}

binarize: 05-binarize.o camera.o
	${CXX} -o $@ $^ ${LIBS}

color: 06-color.o camera.o
	${CXX} -o $@ $^ ${LIBS}

clean:
	\rm -f *.o *~ ${PROGS}
