#include <iostream>
#include <vector>
#include <algorithm>

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
    int num, invalid_num;

    const int PREAMBLE_LEN = 25;

    while(cin >> num){
        numbers.push_back(num); 
    }
        
    for(int i = PREAMBLE_LEN; i < numbers.size(); ++i){
        if(!is_valid(numbers, i, PREAMBLE_LEN)){
            invalid_num = numbers[i];
           cout << "First Invalid Number: " << numbers[i] << " at " << i << endl;
           break;
        }
    }

    vector<int> longest_seq, seq;
    for(int i = 0; i < numbers.size(); ++i){
        int sum = 0;
        seq.clear();
        for(int j = i; j < numbers.size() && sum < invalid_num; ++j){
            seq.push_back(numbers[j]);
            sum += numbers[j];
        }

        if(sum == invalid_num && seq.size() > longest_seq.size()){
            longest_seq.swap(seq);
        }
    }

    int min_elt = *min_element(longest_seq.begin(),longest_seq.end()),
        max_elt = *max_element(longest_seq.begin(),longest_seq.end());
    cout << "Maximum sequence len: " << longest_seq.size() << endl;
    cout << "Min/Max sum: " << min_elt << " + " << max_elt << " == " 
         << min_elt+max_elt << endl;

    return 0;
}
