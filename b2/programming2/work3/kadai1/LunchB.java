// LunchBクラスを書く(???を適切に直す)
public class LunchB ??? LunchA{
  private String ??? ; // トッピングの名前
  private int ??? ; // トッピングの価格

  public LunchB(String ??? , int pCurry,
        String topping, int pTopping){
     super( ??? );
     this.topping = ??? ;
     this.pTopping = ??? ;
  }

  @Override public String name(){
      return topping + super.name(); }

  @Override public int price() {
      return ???.price() + pTopping; }

}

