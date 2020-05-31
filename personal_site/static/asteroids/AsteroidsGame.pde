Spaceship starship;boolean is1Pressed,is3Pressed,is4Pressed,is5Pressed;Star[]stars=new Star[100];ArrayList<Asteroid>asteroids=new ArrayList<Asteroid>();ArrayList<Bullet>projectiles=new ArrayList<Bullet>();int time,cooldown;public void setup(){time=0;starship=new Spaceship();size(600,600);strokeWeight(1);background(0);for(int i=0;i<stars.length;i++){stars[i]=new Star();}
for(int i=0;i<(int)(Math.random()*5)+8;i++){asteroids.add(new Asteroid());}
is1Pressed=false;is3Pressed=false;is4Pressed=false;is5Pressed=false;}
public void draw(){background(0);if(time!=0){time-=1;}
if(cooldown!=0){cooldown-=1;}
for(int i=0;i<stars.length;i++){stars[i].show();}
if(is3Pressed){starship.turn(-4);starship.right(true);}else{starship.right(false);}
if(is4Pressed){starship.turn(4);starship.left(true);}else{starship.left(false);}
if(is5Pressed){starship.accelerate(0.15);starship.traveling(true);}else{starship.traveling(false);}
if(is1Pressed&&cooldown==0){projectiles.add(new Bullet(starship));cooldown=20;}
if(asteroids.size()>0){for(int i=0;i<asteroids.size();i++){asteroids.get(i).move();}}
if(projectiles.size()>0){for(int i=0;i<projectiles.size();i++){projectiles.get(i).move();}}
starship.move();for(int i=asteroids.size()-1;i>=0;i--){ArrayList<Integer>removingp=new ArrayList<Integer>();boolean asteroidcheck=false;for(int k=0;k<projectiles.size();k++){float ax=(float)asteroids.get(i).getAsteroidX();float ay=(float)asteroids.get(i).getAsteroidY();float px=(float)projectiles.get(k).impactCheckX();float py=(float)projectiles.get(k).impactCheckY();if(dist(ax,ay,px,py)<15){asteroidcheck=true;removingp.add(k);}}
if(asteroidcheck){boolean sizeCheck=asteroids.get(i).theSizing();originX=asteroids.get(i).getAsteroidX();originY=asteroids.get(i).getAsteroidY();asteroids.remove(i);if(sizeCheck){for(int rand=0;rand<(int)(Math.random()*3)+1;rand++){asteroids.add(new Asteroid(0.55,originX,originY));}}}
for(int j=removingp.size()-1;j>=0;j--){int numtoremove=removingp.get(j);projectiles.remove(numtoremove);}}
if(asteroids.size()>0){for(int i=0;i<asteroids.size();i++){asteroids.get(i).show();}}
if(projectiles.size()>0){for(int i=0;i<projectiles.size();i++){projectiles.get(i).show();}}
starship.show();}
void keyPressed(){if(key=='1')is1Pressed=true;if(key=='3')is3Pressed=true;if(key=='4')is4Pressed=true;if(key=='5')is5Pressed=true;if(key=='7')starship.stop();if(key=='2'&&time==0){starship.hyperspaceJump();time=30*4;}
if(key=='6')starship.warpSpeed();}
void keyReleased(){if(key=='1')is1Pressed=false;if(key=='3')is3Pressed=false;if(key=='4')is4Pressed=false;if(key=='5')is5Pressed=false;}