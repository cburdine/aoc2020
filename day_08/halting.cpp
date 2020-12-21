#include <iostream>
#include <vector>

using namespace std;

const int NOP = 0, ACC = 1, JMP = 2;

struct instr { int type, val; };

void iexec(int& eip, instr& i, int& acc ){
    if(i.type == JMP){
        eip += i.val;
    } else {
        if(i.type == ACC){ acc += i.val; }
        ++eip;
    }
}

int main(){

    string op;
    int val;
    vector<instr> code;
    vector<bool> exec_code;

    while(cin >> op >> val){
        instr i;
        if(op == "acc"){
            i.type = ACC;
        } else if(op == "jmp"){
            i.type = JMP;
        } else {
            i.type = NOP;
        }
        i.val = val;

        code.push_back(i);
    }

    exec_code = vector<bool>(code.size(),false);

    int eip = 0, acc = 0;
    while(0 <= eip && eip < code.size()){
        if(exec_code[eip] == true){
            cout << "ACC: " << acc << endl;
            return 0;        
        }
        exec_code[eip] = true;
        iexec(eip,code[eip],acc);
    }

    return 0;
}

