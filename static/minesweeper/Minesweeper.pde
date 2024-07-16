import de.bezier.guido.*;
//Declare and initialize constants NUM_ROWS and NUM_COLS = 20
public final static int NUM_COLS = 20;
public final static int NUM_ROWS = 20;
public final static int MINE_COUNT = 90;
public boolean firstClick;
public int minedCount;
private MSButton[][] buttons; //2d array of minesweeper buttons
private ArrayList <MSButton> mines; //ArrayList of just the minesweeper buttons that are mined

void setup ()
{
    size(400, 400);
    textAlign(CENTER,CENTER);
    
    // make the manager
    Interactive.make( this );
    
    //your code to initialize buttons goes here
    buttons = new MSButton[NUM_ROWS][NUM_COLS];

    for(int i = 0; i < NUM_ROWS; i++){
        for(int j = 0; j < NUM_COLS; j++){
            buttons[i][j] = new MSButton(i, j);
        }
    }

    firstClick = true;
    minedCount = 0;

    mines = new ArrayList <MSButton>();
    
    setMines();
}
public void setMines()
{
    for(int i = 0; i < MINE_COUNT; i++){
        int row = (int)(Math.random()*NUM_ROWS);
        int col = (int)(Math.random()*NUM_COLS);
        if(!mines.contains(buttons[row][col])){
            mines.add(buttons[row][col]);
        }
    }
}
public void setMines(int r, int c)
{
    for(int i = 0; i < MINE_COUNT; i++){
        int row = (int)(Math.random()*NUM_ROWS);
        int col = (int)(Math.random()*NUM_COLS);
        if(!mines.contains(buttons[row][col])){
            mines.add(buttons[row][col]);
        }
    }
}

public void draw ()
{
    background( 0 );
    if(isWon() == true)
        displayWinningMessage();
}
public boolean isWon()
{
    return !(minedCount < ((NUM_ROWS * NUM_COLS) - MINE_COUNT));
}
public void displayLosingMessage()
{
    gameOver();
    buttons[0][0].setLabel("Y");
    buttons[0][1].setLabel("O");
    buttons[0][2].setLabel("U");
    buttons[0][3].setLabel(" ");
    buttons[0][4].setLabel("L");
    buttons[0][5].setLabel("O");
    buttons[0][6].setLabel("S");
    buttons[0][7].setLabel("E");
}
public void displayWinningMessage()
{
    gameOver();
    buttons[0][0].setLabel("Y");
    buttons[0][1].setLabel("O");
    buttons[0][2].setLabel("U");
    buttons[0][3].setLabel(" ");
    buttons[0][4].setLabel("W");
    buttons[0][5].setLabel("I");
    buttons[0][6].setLabel("N");
}
public void gameOver() {
    for(int i = 0; i < NUM_ROWS; i++){
        for(int j = 0; j < NUM_COLS; j++){
            buttons[i][j].gameOver();
        }
    }
}
public boolean isValid(int r, int c)
{
    return r < NUM_ROWS && r >= 0 && c < NUM_COLS && c >= 0;
}
public int countMines(int row, int col)
{
    int numMines = 0;

    for(int i = row - 1; i <= row + 1; i++){
        for(int j = col - 1; j <= col + 1; j++){
            if(isValid(i, j) && mines.contains(buttons[i][j])){
                numMines++;
            }
        }
    }

    return numMines;
}
public class MSButton
{
    private int myRow, myCol;
    private float x,y, width, height;
    private boolean clicked, flagged, game, clickable;
    private String myLabel;
    
    public MSButton (int row, int col)
    {
        width = 400/NUM_COLS;
        height = 400/NUM_ROWS;
        myRow = row;
        myCol = col; 
        x = myCol*width;
        y = myRow*height;
        myLabel = "";
        flagged = clicked = false;
        game = clickable = true;
        Interactive.add( this ); // register it with the manager
    }

    // called by manager
    public void mousePressed() 
    {
        if(firstClick && mines.contains(this)){
            for(int i = mines.size() - 1; i >= 0; i--){
                mines.remove(i);
            }
            setMines(myRow, myCol);
        }
        if(firstClick && countMines(myRow, myCol) > 0){
            while (countMines(myRow, myCol) > 0){
                for(int i = mines.size() - 1; i >= 0; i--){
                    mines.remove(i);
                }
                setMines(myRow, myCol);
            }
        }
        if(game && clickable){
            firstClick = false;
            clicked = true;
            if(keyPressed || mouseButton == RIGHT){
                if(flagged){
                    flagged = false;
                    clicked = false;
                }else{
                    flagged = true;
                }
            }else if(mines.contains(this)){
                displayLosingMessage();
            }else if(countMines(myRow, myCol) > 0){
                clickable = false;
                minedCount++;
                setLabel(countMines(myRow, myCol));
            }else{
                clickable = false;
                minedCount++;
                for(int i = -1; i <= 1; i++){
                    for(int j = -1; j <= 1; j++){
                        if(isValid(myRow + i, myCol + j) && buttons[myRow + i][myCol + j].checkClicked()){
                            buttons[myRow + i][myCol + j].mousePressed();
                        }
                    }
                }
            }
        }
    }
    public void draw () 
    {    
        if (flagged)
            fill(0);
        else if( clicked && mines.contains(this) ) 
            fill(255,0,0);
        else if(clicked)
            fill(200);
        else 
            fill(100);

        rect(x, y, width, height);
        fill(0);
        text(myLabel,x+width/2,y+height/2);
    }
    public void setLabel(String newLabel)
    {
        myLabel = newLabel;
    }
    public void setLabel(int newLabel)
    {
        myLabel = ""+ newLabel;
    }
    public boolean isFlagged()
    {
        return flagged;
    }
    public boolean checkClicked() {
        return !clicked;
    }
    public void gameOver() {
        game = false;
    }
}
