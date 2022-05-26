class Tendril
{public final static int SEG_LENGTH=4;private int myNumSegments,myX,myY;private double myAngle;public Tendril(int len,double theta,int x,int y)
{myNumSegments=len;myAngle=theta;myX=x;myY=y;}
public void show()
{int startX=myX;int startY=myY;if(myNumSegments>=100){stroke(5,223,227);}else if(myNumSegments>=30){stroke(3,44,252);}else if(myNumSegments>=10){stroke(148,0,189);}else{stroke(242,29,207);}
for(int i=0;i<myNumSegments;i++){myAngle+=Math.random()*0.4-0.2;int endX=startX+(int)(SEG_LENGTH*Math.cos(myAngle));int endY=startY+(int)(SEG_LENGTH*Math.sin(myAngle));line(startX,startY,endX,endY);startX=endX;startY=endY;}
if(myNumSegments>10){Cluster newC=new Cluster(myNumSegments/3,startX,startY);}}}