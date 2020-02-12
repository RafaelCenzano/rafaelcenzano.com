int[] gridX = {18, 30, 42};
int[] gridY = gridX;
int superSum = 0;
Die[] diceObjects = new Die[132];
int count = 0;


void setup(){
	noLoop();
	size(660, 810);
	noStroke();
	for(int y = 0; y < 720; y = y + 60){
		for (int x = 0; x < 650; x = x + 60){
   			diceObjects[count] = new Die(x, y);
   			count++;
    	}
	}
}

void draw(){
	//your code here
	background(0);
	int sum = 0;
  	
  	for(int i = 0; i < diceObjects.length; i++){
  		diceObjects[i].reset();
  		diceObjects[i].roll();
  		diceObjects[i].show();
  		sum += diceObjects[i].num;
  	}

  	superSum += sum;
  	textSize(32);
  	fill(0, 200, 0);
	text("Total for this roll: " + sum, 10, 760);
	text("Grandtotal: " + superSum, 10, 760 + 40);
}

void mousePressed(){
	redraw();
}

class Die{ //models one single dice cube

	//variable declarations here
	int dieX, dieY, num;
	color c;
	int[][] dots = {
					{0, 0, 0},
					{0, 0, 0},
					{0, 0, 0}
				   };
	
	//constructor
	Die(int x, int y){
		//variable initializations here
		dieX = x;
		dieY = y;
		c = color(0, 40 + (x / 7) + (y / 7), 0);
	}
	void roll(){
		//your code here
		num = (int)(Math.random() * 6) + 1;
		if(num == 1){
			one();
		}else if(num == 2){
			two();
		}else if(num == 3){
			three();
		}else if(num == 4){
			four();
		}else if(num == 5){
			five();
		}else if(num == 6){
			six();
		}else {
			System.out.println("Error occured");
			System.exit(0);
		}
	}
	void show(){
		//your code here
		fill(c);
		rect(dieX, dieY, 60, 60);
		//divide cube into 5 parts each 2 pixels wide
		for(int i = 0; i < 3; i++){
			for(int j = 0; j < 3; j++){
				if(dots[i][j] != 0){
					int dotY = gridY[i];
					int dotX = gridX[j];
					fill(255, 255, 255);
					ellipse(dotX + dieX, dotY + dieY, 8, 8);
				}
			}
		}
	}
	void reset(){
		for(int i = 0; i < 3; i++){
			for(int j = 0; j < 3; j++){
				dots[i][j] = 0;
			}
		}
	}
	void one(){
		dots[1][1] = 1;
	}
	void two(){
		dots[0][0] = 1;
		dots[2][2] = 1;
	}
	void three(){
		two();
		one();
	}
	void four(){
		two();
		dots[0][2] = 1;
		dots[2][0] = 1;
	}
	void five(){
		three();
		dots[0][2] = 1;
		dots[2][0] = 1;
	}
	void six(){
		four();
		dots[1][0] = 1;
		dots[1][2] = 1;
	}
}
