public void setup()
{size(800,800);background(0);noLoop();}
public void draw()
{background(0);Cluster c=new Cluster(100,mouseX,mouseY);}
public void mousePressed()
{redraw();}