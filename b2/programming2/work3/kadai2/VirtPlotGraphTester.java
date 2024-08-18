// mainメソッドを含むVirtPlotGraphTesterクラスを書く

class VirtPlotGraphTester{

	public static final int xRange = 20;

	public static void main(String args[]){

		VirtPlotGraph virtPlotGraphs[] = {
			new VirtPlotGraph('1'),
			new SinVPGraph('2', xRange),
			new ???('3', xRange),
		};

		for(int x = 0;x <= xRange;x++){
			VirtPlotGraph.clear();
			VirtPlotGraph.setX(???);
			for(int i = 0;i < virtPlotGraphs.???;i++){
				virtPlotGraphs[i].computeY();
				virtPlotGraphs[i].plot();
			}
			VirtPlotGraph.println();
		}

	}

}

