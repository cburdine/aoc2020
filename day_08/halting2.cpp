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

bool run(vector<instr>& code, int& acc){
    int eip = 0;
    vector<bool> exec_code = vector<bool>(code.size(), false);
    while(0 <= eip && eip < code.size()){
        if(exec_code[eip] == true){
            return false;
        }
        exec_code[eip] = true;
        iexec(eip,code[eip],acc);
    }
    return (eip == code.size());
}

int main(){

    string op;
    int val;
    vector<instr> code; 

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
    
    for(int i = 0; i < code.size(); ++i){ 
        int itype = code[i].type;
        if(itype != ACC){
            int acc = 0;
            code[i].type = (itype == NOP)? JMP : NOP;
            if(run(code,acc)){
                cout <<  "Correct ACC: " << acc << endl;
                return 0;
            }
            code[i].type = itype;
        }
    }   
    
    return 0;
}

