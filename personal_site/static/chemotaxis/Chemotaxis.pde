 //declare bacteria variables here

Bacteria[] savedBacteria = new Bacteria[300];

 void setup()   
 {
 	frameRate(250);
 	background(0);
 	//initialize bacteria variables here
 	size(700,700);
 	for(int i = 0; i < savedBacteria.length; i++){
 		savedBacteria[i] = new Bacteria(350,350);
 	}
 }   
 void draw()   
 {    
 	//move and show the bacteria
 	for(int i = 0; i < savedBacteria.length; i++){
 		savedBacteria[i].move();
 		savedBacteria[i].show();
 	}
 }
void mousePressed(){
	background(0);
	for(int i = 0; i < savedBacteria.length; i++){
 		savedBacteria[i].myX = 350;
 		savedBacteria[i].myY = 350;
 		savedBacteria[i].myColor = 250;
 	}
}
 class Bacteria
 {
 	int myX, myY, myColor;
 	Bacteria(int x, int y){
 		myX = x;
 		myY = y;
 		myColor = 250;
 	}
 	void move(){
 		int temp1 = myX;
 		int temp2 = myY;
 		myX += (int)(Math.random() * 11) - 5;
 		myY += (int)(Math.random() * 11) - 5;
 		if(myY < 0 || myX > 700 || myX < 0 || myX > 700){
 			myX = temp1;
 			myY = temp2;
 			move();
 		}
 		myColor -= (myX + myY) / 800;
 	}
 	void show(){
 		fill(0, myColor, 0);
 		ellipse(myX, myY, 5, 5);
 	}
 }    