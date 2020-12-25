#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;


int move(int current, vector<int>& next_ll){
    int rem_1, rem_2, rem_3;
    
    rem_1 = next_ll[current];
    rem_2 = next_ll[rem_1];
    rem_3 = next_ll[rem_2];

    //cout << next_ll[current] << ' ' << next_ll[rem_3] << endl;
    next_ll[current] = next_ll[rem_3];
    
    int dest = (current+next_ll.size()-1)%next_ll.size();
    
    while(dest == rem_1 || dest == rem_2 || dest == rem_3){
        dest = (dest+next_ll.size()-1)%next_ll.size();
    }

    int dest_next = next_ll[dest];
    next_ll[dest] = rem_1;
    next_ll[rem_3] = dest_next;
    
    return next_ll[current];
}

void dump(vector<int>& ll){
    for(int i = 0; i < ll.size(); ++i){
        cout << '[' << i << "]: " << ll[i] << endl;
    }
     
    int next = ll[0];
    cout << 0;
    while(next != 0){ 
        cout << ' ' << next; 
        next = ll[next];
    }
    cout << endl;
}

int main(){

    
    const int N_CUPS = 1000000;
    const int N_MOVES = 10000000;


    int init;
    cin >> init;
     
    vector<int> ll = vector<int>(N_CUPS,-1);
    
    vector<int> input;
    while(init > 0){
        input.push_back((init+9)%10);
        init /= 10;
    }
    
    reverse(input.begin(),input.end());
    
    if(ll.size() == input.size())
        input.push_back(input[0]);
    else
        input.push_back(input.size());
    
    int current = input[0];    
    
    // populate ll:
    for(int i = 0; i < ll.size(); ++i){
        if(i < (input.size()-1)){
            ll[input[i]] = input[i+1];
        } else {
            ll[i] = (i+1)%ll.size();
        }
    }    
    
    if(ll.size()+1 != input.size())
        ll[ll.size()-1] = current; 
     
     
    for(int i = 0; i < N_MOVES; ++i){
        current = move(current, ll);
    }
    
    //dump(ll);
    long long int r1 = ll[0]+1;
    long long int r2 = ll[ll[0]]+1;
    
    cout << "Answer: " << endl;
    cout << r1 << " * " << r2 << " = " << r1*r2 << endl;
}  




