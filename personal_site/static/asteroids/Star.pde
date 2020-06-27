class Star //note that this class does NOT extend Floater
{
  private double myX, myY;
  private int myColor, size;
  public Star(){
    myX = Math.random() * 600;
    myY = Math.random() * 600;
    size = (int)(Math.random() * 6);
    myColor = color((int)(Math.random() * 200) + 55,(int)(Math.random() * 200) + 55,(int)(Math.random() * 200) + 55);
  }
  public void show(){
    fill(myColor);
    stroke(myColor);
    ellipse((float)myX, (float)myY, size, size);
  }
}
