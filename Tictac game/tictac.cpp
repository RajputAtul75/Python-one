#include<iostream>
using namespace std;
int currentPlayer; 
char currentMarker;
char board[3][3] = {{'1','2','3'},{'4','5','6'},{'7','8','9'}};

void drawBoard(){
    cout<<" "<<board[0][0]<<" | "<<board[0][1]<<" | "<<board[0][2]<<" \n";
    cout<<"---|---|---\n";
    cout<<" "<<board[1][0]<<" | "<<board[1][1]<<" | "<<board[1][2]<<" \n";
    cout<<"---|---|---\n";
    cout<<" "<<board[2][0]<<" | "<<board[2][1]<<" | "<<board[2][2]<<" \n";
    cout<<"---|---|---\n";
}

bool placeMarker(int slot){
    int row = (slot-1)/3;
    int col = (slot-1)%3;

    if(board[row][col] != 'X' && board[row][col] != '0'){
         board[row][col] = currentMarker;
         return true;
    }
    else{
        return false;
    }
}

void game(){
    cout<<"Player1 choose your marker: X or 0"<<endl;
    char markerP1;
    cin>>markerP1;

    currentPlayer = 1;
    currentMarker = markerP1;
    drawBoard();
    int playerwon;
    for(int i=0; i<9; i++){
        cout<<"Its player"<<currentPlayer<<"Enter the slot:";
        int slot;
        cin>>slot;

        if(slot<1 || slot>9){
            cout<<"Please select the valid slot!"<<endl;
            i--;
            continue;
        }
        if(!placeMarker(slot)){
            cout<<"Slot occupied! try again"<<endl;
            i--;
            continue;
        }
        drawBoard();


    }
}

int main(){
    game();
    return 0;
}