class Spaceship extends Floater  
{
  boolean moving, turningLeft, turningRight, hyperspace;
  int teleport;
  ArrayList <Double> lightning;
  public Spaceship(){
    moving = turningLeft = turningRight = hyperspace = false;
    lightning = new ArrayList <Double>();
    teleport = 0;
    corners = 10;
    int[] temp1 = {-8, 5, 1, 7, 16, 7, 1, 5, -8};
    int[] temp2 = {-8, -6, -5, -3, 0, 3, 5, 6, 8};
    xCorners = new int[10];
    yCorners = new int[10];
    for(int i = 0; i < temp1.length; i++){
      xCorners[i] = (int)(temp1[i] * 1.5);
      yCorners[i] = (int)(temp2[i] * 1.5);
    }
    myColor = color (200, 200, 220);
    myCenterX = myCenterY = 300; 
    myDirectionX = myDirectionY = 0;
    myPointDirection = 0;
  }
  public double getX(){
    return myCenterX;
  }
  public double getY(){
    return myCenterY;
  }
  public double getDirection(){
    return myPointDirection;
  }
  public double getDirectionX(){
    return myDirectionX;
  }
  public double getDirectionY(){
    return myDirectionY;
  }
  public void show(){

    fill(myColor);
    stroke(myColor);
    
    //translate the (x,y) center of the ship to the correct position
    translate((float)myCenterX, (float)myCenterY);

    //convert degrees to radians for rotate()
    float dRadians = (float)(myPointDirection*(Math.PI/180));
    
    //rotate so that the polygon will be drawn in the correct direction
    rotate(dRadians);

    if(teleport > 0){
      teleport -= 1;
      if(hyperspace){
        myDirectionX = myDirectionX / 2;
        myDirectionY = myDirectionY / 2;
      }else if(teleport % 4 == 0){
        myDirectionX = myDirectionX / 2;
        myDirectionY = myDirectionY / 2;
      }
    }

    if(hyperspace && teleport > 0){
      teleport -= 1;
      if (teleport % 4 == 0){//change lines every 4
        for(int i = 0; i < lightning.size(); i++){
          lightning.remove(i);
        }
        for(int i = 0; i < 4; i++){
          double x1 = 0.0;
          double x2 = 0.0 + (Math.random() * 3) - 1;
          double y1 = 0.0;
          double y2 = 0.0 + (Math.random() * 3) - 1;
          while(x2 > -30 * ((60 - teleport) / 40) && x2 < 30 * ((60 - teleport) / 40) || y2 < 30 * ((60 - teleport) / 40) && y2 > -30 * ((60 - teleport) / 40)){
            lightning.add(x1);
            lightning.add(x2);
            lightning.add(y1);
            lightning.add(y2);
            x1 = x2;
            y1 = y2;
            x2 += (Math.random() * 3) - 1;
            y2 += (Math.random() * 3) - 1;
          }
        }
        strokeWeight(2);
        stroke(12, 180, 199, 90);
        for(int i = 0; i < lightning.size() - 4; i += 4){
          double linex1 = lightning.get(i);
          double linex2 = lightning.get(i + 1);
          double liney1 = lightning.get(i + 2);
          double liney2 = lightning.get(i + 3);
          line((float)linex1, (float)linex2, (float)liney1, (float)liney2);
          line((float)linex1 * -1.0, (float)linex2 * -1.0, (float)liney1 * -1.0, (float)liney2 * -1.0);
          line((float)linex1 * -1.0, (float)linex2, (float)liney1 * -1.0, (float)liney2);
          line((float)linex1, (float)linex2 * -1.0, (float)liney1, (float)liney2 * -1.0);
        }
        strokeWeight(1);
      }
    }else if(hyperspace && teleport == 0){
      myDirectionY = myDirectionX = 0;
      myCenterY = (Math.random() * 600) + 1;
      myCenterX = (Math.random() * 600) + 1;
      hyperspace = false;
      myPointDirection = (int)(Math.random() * 360) + 1;
    }
    
    //draw the polygon
    beginShape();
    for (int nI = 0; nI < corners; nI++){
      vertex(xCorners[nI], yCorners[nI]);
    }
    endShape(CLOSE);
    if(moving){
      strokeWeight(3);
      stroke(0, 195, 230, 70);
      line(-5, 0, -20, 0);
      line(-5, 3, -20, 7);
      line(-5, -3, -20, -7);
      strokeWeight(1);
    }
    if(turningRight){
      strokeWeight(3);
      stroke(0, 200, 255, 50);
      line(16, 5, 15, 11);
      strokeWeight(1);
    }
    if(turningLeft){
      strokeWeight(3);
      stroke(0, 200, 255, 50);
      line(16, -5, 15, -11);
      strokeWeight(1);
    }

    //"unrotate" and "untranslate" in reverse order
    rotate(-1*dRadians);
    translate(-1*(float)myCenterX, -1*(float)myCenterY);
  }
  public void traveling(boolean check) {
    moving = check;
  }
  public void left(boolean check) {
    turningLeft = check;
  }
  public void right(boolean check) {
    turningRight = check;
  }
  public void stop(){
    teleport = 60;
  }
  public void warpSpeed() {
    myDirectionY *= 5;
    myDirectionX *= 5;
  }
  public void hyperspaceJump(){
    myDirectionX = myDirectionX / 2;
    myDirectionY = myDirectionY / 2;
    hyperspace = true;
    teleport = 60;
  }
}