#include <iostream>
#include <vector>
#include <map>
#include <algorithm>
#include <cassert>

using namespace std;

struct tile_t {
    int id;

    int neighbors[4] = {-1, -1, -1 ,-1};
    char tile[10][11];

    tile_t(){}
    
    tile_t(int id, vector<string> input){
        this->id = id;
        assert(input.size() == 10);
        for(int r = 0; r < input.size(); ++r){
            for(int c = 0; c < 10; ++c){
                tile[r][c] = input[r][c];
            }
            tile[r][10] = 0;
        }
    }

    vector<string> get_borders(){
        vector<string> borders;
        char left[11]; 
        char right[11];
        for(int r = 0; r < 10; ++r){
            left[r] = tile[r][0];
            right[r] = tile[r][9];
        }
        left[10] = 0;
        right[10] = 0;

        borders.push_back(string(tile[0]));
        borders.push_back(string(left));
        borders.push_back(string(tile[9]));
        borders.push_back(string(right));
        
        return borders;
    }
};

string canonical_form(string border){
    string rev = border;
    reverse(rev.begin(), rev.end());
    return (border < rev)? border : rev;
}

int border_match(string a, string b){
    if(a == b){ return 1; }
    reverse(a.begin(),a.end());
    if( a == b){ return -1; }
    return 0;
}



int main(){

    map<string,int> border_count;

    // parse input:
    string token;
    int id;
    vector<string> lines;
    map<string,vector<int>> border_tiles;
    map<int,tile_t> tiles;
        
    while(cin >> token >> id){
        getline(cin,token);
        lines.clear();    
        for(int i = 0; i < 10; ++i){
            getline(cin,token);
            lines.push_back(token);
        }
        getline(cin,token);
        tile_t next_tile = tile_t(id,lines);
        tiles[id] = next_tile;

        for(string b : next_tile.get_borders()){ 
            b = canonical_form(b);
            if(border_tiles.find(b) == border_tiles.end()){
                border_tiles[b] = vector<int>();
            }
            border_tiles[b].push_back(id);
        }
    }
    
    // print border -> tile id mapping:
    /*
    vector<int> corner_ids;
    for(auto& p : border_tiles){
        cout << p.first << ":" << endl;
        for(int id : p.second){
            cout << ' ' << id;
        }
        cout << endl;
    }
    */

    // determine the corner pieces:
    vector<int> corner_pieces;
    for(auto& p : tiles){
        int n_neighbors = 0;
        for(string b : p.second.get_borders()){
            b = canonical_form(b);
            if(border_tiles[b].size() >= 2){ ++n_neighbors; }
        }
        if(n_neighbors <= 2){
            corner_pieces.push_back(p.first);
        }
    }

    long long int prod = 1;    
    for(int i : corner_pieces){ 
        cout << i << endl; 
        prod *= i;
    }

    cout << "product: " << prod << endl;
    
    
    return 0;
}
