#include <iostream>
#include <vector>
#include <sstream>
#include <cmath>

using namespace std;

int freq(char ch, string s){
    int cnt = 0;
    for(auto c : s){
        if(c == ch){ ++cnt; }
    }

    return cnt;
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
    
        int f = freq(ch[0], str);
        
        if(min_ch <= f && f <= max_ch){ 
            ++num_valid; 
            cout << "VALID" << endl;
        }
    }

    cout << endl << num_valid << endl;
    
    return 0;
}
