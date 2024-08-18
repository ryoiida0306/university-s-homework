// mainメソッドを含むShapeTesterEx141クラスを書く

    // 次と同等以上のテストをして，動作を説明すること
    Shape p[] = { new Point(), new Rectangle(3,2), new Parallelogram(4,3) };
    for(Shape s : p){
      s.print();                                                                      if(s instanceof Plane2D){
        System.out.println("Area="+((Plane2D)s).getArea());
      }
      System.out.println();
    }

    Plane2D q[] = { new Rectangle(3,2), new Parallelogram(4,3) };
    for(Plane2D i : q){
      System.out.println("Area="+i.getArea());
    }

