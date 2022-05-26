class Bullet extends Floater{
    public Bullet(Spaceship starship){
        myCenterX = starship.getX();
        myCenterY = starship.getY();
        myPointDirection = starship.getDirection();
        double dRadians = myPointDirection * (Math.PI/180);
        myDirectionX = 5 * Math.cos(dRadians) + starship.getDirectionX();
        myDirectionY = 5 * Math.sin(dRadians) + starship.getDirectionY();
    }
    public void show(){
        fill(212, 50, 38);
        stroke(212, 50, 38);
        strokeWeight(2);
    
        //translate the (x,y) center of the ship to the correct position
        translate((float)myCenterX, (float)myCenterY);

        //convert degrees to radians for rotate()     
        float dRadians = (float)(myPointDirection*(Math.PI/180));
    
        //rotate so that the polygon will be drawn in the correct direction
        rotate(dRadians);

        line(0, 0, 5, 0);

        //"unrotate" and "untranslate" in reverse order
        rotate(-1*dRadians);
        translate(-1*(float)myCenterX, -1*(float)myCenterY);
    }
    public double impactCheckX(){
        return myCenterX + 5;
    }
    public double impactCheckY(){
        return myCenterY;
    }
}
