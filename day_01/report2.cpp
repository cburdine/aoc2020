#include <vector>
#include <iostream>
#include <algorithm>

// three records must sum to 2020

using namespace std;

int main(){

    vector<int> expenses;
    int val, target_ub, target, e, e2;

    while(cin >> val){
        expenses.push_back(val);   
    }

    sort(expenses.begin(), expenses.end());
    
    for(auto e_itr = expenses.begin(); e_itr < expenses.end(); ++e_itr){
        e = *e_itr;
        target_ub = 2020 - e;
        auto target_ub_itr = upper_bound(e_itr+1, expenses.end(), target_ub);        

        for(auto e2_itr = (e_itr+1); e2_itr != target_ub_itr; ++e2_itr){
            e2 = *e2_itr;
            target = (target_ub -  e2);

            //cout << e << ' ' << e2 << " ("  << target << ")\n";

            if(binary_search(e2_itr, expenses.end(), target)){
                cout << e << " * " << e2 << " * " << target << " == " << endl;
                cout << e * e2 * target << endl;
            }
        }
    }
    
    return -1;
}
