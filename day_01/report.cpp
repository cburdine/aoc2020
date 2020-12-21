#include <vector>
#include <iostream>
#include <algorithm>

using namespace std;

int main(){

    vector<int> expenses;
    int val, target;

    while(cin >> val){
        expenses.push_back(val);   
    }

    sort(expenses.begin(), expenses.end());
    
    for(auto e : expenses){
        target = 2020 - e;

        if(binary_search(expenses.begin(),expenses.end(), target)){
            cout << e << " * " << target << " == " << endl;
            cout << e * target << endl;
            return 0;
        }
    }
    
    return -1;
}
