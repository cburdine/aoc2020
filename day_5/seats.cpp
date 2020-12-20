#include <iostream>
#include <cmath>
#include <algorithm>
#include <vector>

using namespace std;

int seat_id(string seat){
    int id = 0;
    for(int i = 0; i < 10; ++i){
        id= (id<<1);
        if(seat[i] == 'B' || seat[i] == 'R'){
            id = (id|1);
        }
    }
    //cout << "row: " << (id>>3) << endl;
    //cout << "col: " << (id&7) << endl;

    return id;
}

int main(){

    vector<int> seats;
    string seat;
    
    while(getline(cin, seat) && seat.size() > 0){
        seats.push_back(seat_id(seat));
    }
    
    sort(seats.begin(), seats.end());

    cout << seats[0] << endl;
    for(auto itr = (seats.begin()+1); itr != seats.end(); ++itr){
        cout << *itr << endl;
        if( (*itr - *(itr-1)) > 1){
            cout << "SEAT: " << (*itr - 1) << endl;
        }
    }

    return 0;
}
