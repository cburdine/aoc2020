#include <iostream>
#include <vector>

using namespace std;

int n_collisions(vector<string>& slope, int sl_r, int sl_d){

    int wid = slope[0].length();
    int n_trees = 0;
    
    for(int i = 0; sl_d*i < slope.size(); ++i){
        if(slope[sl_d*i][(sl_r*i)%wid] == '#'){
            ++n_trees;
        }
    }
    return n_trees;
}

int main(){

    vector<string> slope;
    string line;
    long long int prod = 1;

    int slopes_r[5] = { 1, 3, 5, 7, 1 };
    int slopes_d[5] = { 1, 1, 1, 1, 2 };

    while(getline(cin,line)){
        slope.push_back(line);
    }

    for(int i =0 ; i < 5; ++i){
        cout << "(" << slopes_r[i] << ", " << slopes_d[i] << ")" << endl;
        long long int colls = n_collisions(slope, slopes_r[i], slopes_d[i]);
        cout << colls << endl;
        prod *= colls;
    }

    cout << prod << endl;

    return 0;
}
