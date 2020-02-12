private double fractionLength = 0.85;
private int smallestBranch = 20;
//private double branchAngle = 0.35;
private double branchAngle = 0.35;
public void setup() 
{   
    size(700,700);
    stroke(112, 56, 0);

} 
public void draw() 
{   
    background(16, 186, 224);
    stroke(255, 247, 0, 220);
    fill(255, 247, 0, 220);
    ellipse(0, 0, 150, 150);
    double angle = 3*Math.PI/2;
    double lengthOfInitialBranch = 100;
    int startX = 350;
    int startY = 600;

    // Trunk
    fill(112, 56, 0);
    stroke(112, 56, 0);
    double angle1 = angle + branchAngle;
    double angle2 = angle - branchAngle;
    double length = lengthOfInitialBranch * fractionLength;
    int endX1 = (int)(lengthOfInitialBranch*Math.cos(angle1) + startX);
    int endY1 = (int)(lengthOfInitialBranch*Math.sin(angle1) + startY);
    int endX2 = (int)(lengthOfInitialBranch*Math.cos(angle2) + startX);
    int endY2 = (int)(lengthOfInitialBranch*Math.sin(angle2) + startY);
    beginShape();
    vertex(endX1, endY1);
    vertex(startX, startY);
    vertex(endX2, endY2);
    vertex(endX2, 700);
    vertex(endX1, 700);
    endShape(CLOSE);

    drawBranches(startX, startY, lengthOfInitialBranch, angle);
}
public void drawBranches(float x, float y, double branchLength, double angle) 
{   
    double angle1 = angle + branchAngle;
    double angle2 = angle - branchAngle;
    double length = branchLength * fractionLength;
    int endX1 = (int)(branchLength*Math.cos(angle1) + x);
    int endY1 = (int)(branchLength*Math.sin(angle1) + y);
    int endX2 = (int)(branchLength*Math.cos(angle2) + x);
    int endY2 = (int)(branchLength*Math.sin(angle2) + y);
    strokeWeight((float)branchLength / 7);
    stroke(112, 56, 0);
    line(x, y, endX1, endY1);
    line(x, y, endX2, endY2);
    if(length > smallestBranch){
        double branchAngleNext = (Math.random()*0.025) + 0.325;
        double angle1Next = angle + branchAngleNext;
        double angle2Next = angle - branchAngleNext;
        drawBranches(endX1, endY1, length, angle1Next);
        drawBranches(endX2, endY2, length, angle2Next);
    }
    if(length < 50){
        translate(endX1, endY1);
        rotate((float)angle1);
        leaf(endY1, endY1, 13, 10);
        rotate(-1*(float)angle1);
        translate(-1*endX1, -1*endY1);

        translate(endX2, endY2);
        rotate((float)angle2);
        leaf(endX2, endY2, 13, 10);
        rotate(-1*(float)angle2);
        translate(-1*endX2, -1*endY2);
    }
}
public void leaf(float x, float y, float w, float h){
    stroke(75, 219, 35);
    fill(75, 219, 35);
    ellipse(0, 0, w, h);
}
