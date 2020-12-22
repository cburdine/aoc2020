#include <iostream>
#include <map>

using namespace std;

int main(){

    const int N_TURNS = 30000000;
    
    map<int,int> spoken;

    char comma;
    int last_spoken;

    int t = 1;
    while(cin >> last_spoken){
        spoken[last_spoken] = t;
        cin >> comma;
        cout << "(" << t << "): " << last_spoken << endl;
        ++t;
    }
    
    while(t <= N_TURNS){
        
        if(spoken.find(last_spoken) == spoken.end()){
            spoken[last_spoken] = (t-1);
            last_spoken = 0;
        } else {
            int prior_turn = spoken[last_spoken];
            spoken[last_spoken] = (t-1);
            last_spoken = ((t-1) - prior_turn);
        }
        cout << "[" << t << "]: " << last_spoken << endl;
        ++t;
    }   

    cout << last_spoken << endl;

    return 0;
}
