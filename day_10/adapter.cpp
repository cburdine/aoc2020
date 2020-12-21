#include <iostream>
#include <vector>
#include <cassert>
#include <algorithm>

using namespace std;


int main(){

    int val;
    vector<int> adapters;
    while(cin >> val){
        adapters.push_back(val);
    }

    sort(adapters.begin(), adapters.end());

    int diff_freqs[4] = { 0, 0, 0, 1 };

    assert(0 < adapters[0] && adapters[0] < 4);
    ++diff_freqs[adapters[0]];

    for(int i = 1; i < adapters.size(); ++i){
        int diff = adapters[i]-adapters[i-1];
        assert(0 < diff && diff <= 3);
        ++diff_freqs[diff];
    }

    cout << "diff freqs:"<< endl 
         << "[1]: " << diff_freqs[1] << endl
         << "[2]: " << diff_freqs[2] << endl
         << "[3]: " << diff_freqs[3] << endl;

    cout << "[1] * [3] == " << diff_freqs[1]*diff_freqs[3] << endl;


    return 0;
}
