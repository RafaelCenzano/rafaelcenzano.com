//your code here
Particle[] warpLines = new Particle[800];
void setup()
{
	size(600, 600);
	frameRate(30);
	for(int i = 0; i < warpLines.length; i++){
		warpLines[i] = new Particle();
	}
	warpLines[0] = new OddballParticle();
	strokeWeight(4);
}
void draw()
{
	background(0);
	for(int i = 800 - 1; i >= 0; i--){
		warpLines[i].move();
		warpLines[i].show();
	}
}
class Particle
{
	double myX, myY, speed, angle, startY, startX;
	int lineColor, weightOfLine;
	Particle(){
		myY = myX = 300;
		speed = (double)(Math.random() * 30) + 14;
		angle = (double)((int)(Math.random() * 360) + 1) * (Math.PI/180);
		int randnum = (int)(Math.random() * 8);
		if(randnum == 0){lineColor = color(225, 225, 255);}
		if(randnum == 1){lineColor = color(100, 100, 215);}
		if(randnum == 2){lineColor = color(250, 250, 255);}
		if(randnum == 3){lineColor = color(30, 30, 70);}
		if(randnum == 4){lineColor = color(100, 100, 150);}
		if(randnum == 5){lineColor = color(200, 200, 250);}
		if(randnum == 6){lineColor = color(200, 200, 200);}
		if(randnum == 7){lineColor = color(150, 150, 255);}
		weightOfLine = 4;
	}
	void move(){
		if(myY > 600 || myX > 600 || myY < 0 || myX < 0){
			myX = myY = 300;
			angle = (double)((int)(Math.random() * 360) + 1) * (Math.PI/180);
			weightOfLine = 5;
		}
		if(myY > 350 || myX > 350 || myY < 250 || myX < 250){
			weightOfLine = 7;
		}
		if(myY > 450 || myX > 450 || myY < 150 || myX < 150){
			weightOfLine = 10;
		}
		startY = myY;
		startX = myX;
		myX += Math.cos(angle) * speed;
		myY += Math.sin(angle) * speed;
	}
	void show(){
		stroke(lineColor);
		strokeWeight(weightOfLine);
		line((float)startX, (float)startY, (float)myX, (float)myY);
	}
}

class OddballParticle extends Particle//inherits from Particle
{
	int check;
	OddballParticle(){
		myX = 300;
		myY = 450;
		check = 0;
	}
	void move(){
		check++;
		if(check > 4){
			myX = 300;
		    myY = 450;
		}
		myX += (Math.random() * 9) - 4;
		myY += (Math.random() * 9) - 4;
	}
	void show(){
		stroke(75, 83, 94);
		strokeWeight(10);
		line((float)myX, (float)myY + (float)60, (float)myX - (float)30, (float)myY + (float)85);
		line((float)myX, (float)myY + (float)60, (float)myX + (float)24, (float)myY + (float)80);
		noStroke();
		fill(75, 83, 94);
		rect((float)myX - 10, (float)myY + 25, 20, 30);
		arc((float)myX, (float)myY + (float)60, (float)30, (float)30, (float)Math.PI, (float)(2 * Math.PI));
		rect((float)myX - 15, (float)myY + 55, 30, 30);
		arc((float)myX, (float)myY + (float)80, (float)30, (float)30, (float)0, (float)Math.PI);
		fill(119, 131, 150);
		ellipse((float)myX, (float)myY, 120, 75);
		rect((float)myX - 40, (float)myY + 47, 17, 85);
		rect((float)myX + 24, (float)myY + 47, 17, 85);
		fill(143, 158, 181);
		ellipse((float)myX, (float)myY, 35, 20);
	}
}