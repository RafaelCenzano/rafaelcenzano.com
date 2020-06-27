class Asteroid extends Floater  
{
  private int rotation;
  private double sizing;
  public Asteroid(){
    int[] tempA1 = {2, 5,  3, -2, -3, -1};
    int[] tempA2 = {3, 0, -2, -2,  0, 3};

    rotation = (int)(Math.random() * 9) - 4;
    int temp = (int)(Math.random() * 3);
    myPointDirection = 0;
    corners = 6;
    xCorners = new int[corners];
    yCorners = new int[corners];
    if (corners == 6){
      for(int i = 0; i < corners; i++){
        xCorners[i] = (int)(tempA1[i] * ((Math.random() * 7) + 0.25));
        yCorners[i] = (int)(tempA2[i] * ((Math.random() * 7) + 0.25));
      }
    }
    myCenterX = Math.random() * 600;
    myCenterY = Math.random() * 600;

    myDirectionX = (Math.random() * 5) - 2;
    myDirectionY = (Math.random() * 5) - 2;
    myColor = color(70, 70, 70);
    sizing = 1;
  }
  public Asteroid(double multiplyer, double x, double y){
    sizing = multiplyer;
    int[] tempA1 = {2, 5,  3, -2, -3, -1};
    int[] tempA2 = {3, 0, -2, -2,  0, 3};

    rotation = (int)(Math.random() * 9) - 4;
    int temp = (int)(Math.random() * 3);
    myPointDirection = 0;
    corners = 6;
    xCorners = new int[corners];
    yCorners = new int[corners];
    if (corners == 6){
      for(int i = 0; i < corners; i++){
        xCorners[i] = (int)(tempA1[i] * ((Math.random() * 7) + 0.25)*sizing);
        yCorners[i] = (int)(tempA2[i] * ((Math.random() * 7) + 0.25)*sizing);
      }
    }
    myCenterX = x + (Math.random() * 11) - 5;
    myCenterY = y + (Math.random() * 11) - 5;

    myDirectionX = (Math.random() * 5) - 2;
    myDirectionY = (Math.random() * 5) - 2;
    myColor = color(70, 70, 70);
  }
  public void move(){   
    super.move();
    myPointDirection += rotation;
  }
  public double getAsteroidX(){
    return myCenterX;
  }
  public double getAsteroidY(){
    return myCenterY;
  }
  public boolean theSizing(){
    return sizing >= 1;
  }
}
