#include <iostream>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;

bool valid(char ch, int start, int end, string s){
    
    return (s[start] == ch) ^ (s[end] == ch);
}

int main(){
    
    int num_valid = 0;

    string line;
    while(getline(cin, line)){
        stringstream ss(line);
        
        int min_ch, max_ch;
        string ch, str;
                
        ss >> min_ch >> max_ch >> ch >> str;
        max_ch = abs(max_ch);
        cout << min_ch << ' ' << max_ch << ' ' << ch << ' ' << str << endl; 
        
        if(valid(ch[0], min_ch-1, max_ch-1, str)){ 
            ++num_valid; 
            cout << "VALID" << endl;
        }
    }

    cout << endl << num_valid << endl;
    
    return 0;
}
