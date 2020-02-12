int count;

public void setup(){
    size(600, 600);
    noLoop();
    noStroke();
    count = 1;
    background(0);
}

public void draw(){
    background(0);
    sierpinski(0, 600, 600, 1, count);
    count += 1;
}

public void mouseClicked() {
    redraw();
}

public void sierpinski(int x, int y, int len, int count, int maxCount) {
    if (count >= maxCount){
        triangle(x, y, x + len, y, x + (len / 2), y - len);
    }else{
        count += 1;
        sierpinski(x, y, len / 2, count, maxCount);
        sierpinski(x + (len / 4), y - (len / 2), len / 2, count, maxCount);
        sierpinski(x + (len / 2), y, len / 2, count, maxCount);
    }
}