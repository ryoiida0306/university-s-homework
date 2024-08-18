
public class Report7_4 {

	static void Display(int x[][]) {
		for (int i = 0; 8 > i; i++) {
			for (int j = 0; 8 > j; j++) {
				System.out.print(x[i][j]);
			}
			System.out.println();
		}
		System.out.println();
	}

	static void Initialization(int[][] x, int num) {
		for (int i = 0; 8 > i; i++) {
			for (int j = 0; 8 > j; j++) {
				x[i][j] = num;
			}
		}
	}

	static void delete(int[][] can, int x, int y) {
		for (int i = -8; 8 > i; i++) {
			if(i>=0) {
			can[x][i] = 0;
			can[i][y] = 0;
			}
			if(0<=x+i&&x+i<8&&0<=y+i&&y+i<8) {
				can[x+i][y+i]=0;
				}
			if(0<=x+i&&x+i<8&&0<=y-i&&y-i<8) {
				can[x+i][y-i]=0;

			}
		}
	}

//	static void Queen(int[][] King, int[][] can, int layor) {
//		if (layor == 8) {
//			Display(King);
////			Initialization(King, 0);
////			Initialization(can, 1);
//
//		} else {
//			for (int i = 0; 8 > i; i++) {
//				if (can[layor][i] == 1) {
//					King[layor][i] = 1;
//					delete(can, layor, i);
//					Display(King);
//					Display(can);
//					Queen(King, can, layor + 1);
//				}
//			}
//		}
//	}

	public static void main(String[] args) {
		int Queen1[][] = new int[8][8];
		int Queen2[][] = new int[8][8];
		int Queen3[][] = new int[8][8];
		int Queen4[][] = new int[8][8];
		int Queen5[][] = new int[8][8];
		int Queen6[][] = new int[8][8];
		int Queen7[][] = new int[8][8];
		int Queen8[][] = new int[8][8];
		int can1[][] = new int[8][8];
		int can2[][] = new int[8][8];
		int can3[][] = new int[8][8];
		int can4[][] = new int[8][8];
		int can5[][] = new int[8][8];
		int can6[][] = new int[8][8];
		int can7[][] = new int[8][8];
		int can8[][] = new int[8][8];

		Initialization(can1, 1);
		Initialization(can2, 1);
		Initialization(can3, 1);
		Initialization(can4, 1);
		Initialization(can5, 1);
		Initialization(can6, 1);
		Initialization(can7, 1);
		Initialization(can8, 1);

		for (int a = 0; 8 > a; a++) {
			//if (can1[0][a] == 1) {
				Queen1[0][a] = 1;
				Queen2[0][a] = 1;
				Queen3[0][a] = 1;
				Queen4[0][a] = 1;
				Queen5[0][a] = 1;
				Queen6[0][a] = 1;
				Queen7[0][a] = 1;
				Queen8[0][a] = 1;
				delete(can1, 0, a);
				delete(can2, 0, a);
				delete(can3, 0, a);
				delete(can4, 0, a);
				delete(can5, 0, a);
				delete(can6, 0, a);
				delete(can7, 0, a);
				delete(can8, 0, a);
//				Display(can1);
//				Display(Queen1);
				for (int b = 0; 8 > b; b++) {
					if (can1[1][b] == 1) {
						Queen2[1][b] = 1;
						Queen3[1][b] = 1;
						Queen4[1][b] = 1;
						Queen5[1][b] = 1;
						Queen6[1][b] = 1;
						Queen7[1][b] = 1;
						Queen8[1][b] = 1;
						delete(can2, 1, b);
						delete(can3, 1, b);
						delete(can4, 1, b);
						delete(can5, 1, b);
						delete(can6, 1, b);
						delete(can7, 1, b);
						delete(can8, 1, b);
//						Display(can2);
//						Display(Queen2);
						for (int c = 0; 8 > c; c++) {
							if (can2[2][c] == 1) {
								Queen3[2][c] = 1;
								Queen4[2][c] = 1;
								Queen5[2][c] = 1;
								Queen6[2][c] = 1;
								Queen7[2][c] = 1;
								Queen8[2][c] = 1;
								delete(can3, 2, c);
								delete(can4, 2, c);
								delete(can5, 2, c);
								delete(can6, 2, c);
								delete(can7, 2, c);
								delete(can8, 2, c);
//								Display(can3);
//								Display(Queen3);
								for (int d = 0; 8 > d; d++) {
									if (can3[3][d] == 1) {
										Queen4[3][d] = 1;
										Queen5[3][d] = 1;
										Queen6[3][d] = 1;
										Queen7[3][d] = 1;
										Queen8[3][d] = 1;
										delete(can4, 3, d);
										delete(can5, 3, d);
										delete(can6, 3, d);
										delete(can7, 3, d);
										delete(can8, 3, d);
//										Display(can4);
//										Display(Queen4);
										for (int e = 0; 8 > e; e++) {
											if (can4[4][e] == 1) {
												Queen5[4][e] = 1;
												Queen6[4][e] = 1;
												Queen7[4][e] = 1;
												Queen8[4][e] = 1;
												delete(can5, 4, e);
												delete(can6, 4, e);
												delete(can7, 4, e);
												delete(can8, 4, e);
//												Display(can5);
//												Display(Queen5);
												for (int f = 0; 8 > f; f++) {
													if (can5[5][f] == 1) {
														Queen6[5][f] = 1;
														Queen7[5][f] = 1;
														Queen8[5][f] = 1;
														delete(can6, 5, f);
														delete(can7, 5, f);
														delete(can8, 5, f);
//														Display(can6);
//														Display(Queen6);
														for (int g = 0; 8 > g; g++) {
															if (can6[6][g] == 1) {
																Queen7[6][g] = 1;
																Queen8[6][g] = 1;
																delete(can7, 6, g);
																delete(can8, 6, g);
//																Display(can7);
//																Display(Queen7);
																for (int h = 0; 8 > h; h++) {
																	if (can7[7][h] == 1) {
																		Queen8[7][h] = 1;
																		delete(can8, 7, h);
//																		Display(can8);
																		Display(Queen8);
																	}
																}
															}
														}
													}
												}
											}
										}
									}
								}
							}
						}
					}
				}
			}
		//}
	}





}
