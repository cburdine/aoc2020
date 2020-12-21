#include <iostream>
#include <vector>

using namespace std;

bool is_valid(vector<int>& n, int ind, int plen){

    for(int i = ind-plen; i < ind; ++i){
        for(int j = i+1; j < ind; ++j){
            if(n[i]+n[j] == n[ind]){
                return true;
            }
        }
    }
    return false;
}

int main(){

    vector<int> numbers;
    int num;

    const int PREAMBLE_LEN = 25;

    while(cin >> num){
        numbers.push_back(num); 
    }
        
    for(int i = PREAMBLE_LEN; i < numbers.size(); ++i){
        if(!is_valid(numbers, i, PREAMBLE_LEN)){
           cout << "First Invalid Number: " << numbers[i] << " at " << i << endl;
           return 0;
        }
    }

    return 0;
}
