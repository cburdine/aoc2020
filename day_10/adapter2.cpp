#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>
#include <cmath>

using namespace std;


int main(){

    int val;
    vector<int> adapters;
    while(cin >> val){
        adapters.push_back(val);
    }

    sort(adapters.begin(), adapters.end());
    int target = 3 + adapters.back();
    adapters.push_back(target);

    vector<long long int> mem_table = vector<long long int>(target+1,0);
    
    mem_table[0] = 1;
    for(int a : adapters){
        for(int i = max(0,a-3); i < a; ++i){
            mem_table[a] += mem_table[i];
        }
    }

    for(int a : adapters){
        cout << "[" << a << "]: " << mem_table[a] << endl;
    }

    cout << "# of ways: " << mem_table.back() << endl;

    return 0;
}
