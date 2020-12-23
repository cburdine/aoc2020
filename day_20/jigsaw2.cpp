#include <iostream>
#include <vector>
#include <map>
#include <set>
#include <algorithm>
#include <cassert>

using namespace std;

string MONSTER [3] = { 
"                  # ", 
"#    ##    ##    ###",
" #  #  #  #  #  #   "
};

long long int count_img_char(char ch, vector<vector<char>>& img){
    long long int count = 0;
    for(int r = 0; r < img.size(); ++r){
    for(int c = 0; c < img[0].size(); ++c){
        if(img[r][c] == ch){ ++count; }
    }}

    return count;
}

void rotate_img(vector<vector<char>>& img){
    auto new_img = vector<vector<char>>(img[0].size(),vector<char>(img.size()));
    for(int r = 0; r < img.size(); ++r){
    for(int c = 0; c < img[0].size(); ++c){
        new_img[c][r] = img[img.size()-(r+1)][c];
    }}
    img = new_img;
}

void hflip_img(vector<vector<char>>& img){
    for(int r = 0; r < img.size()/2; ++r){
    for(int c = 0; c < img[0].size(); ++c){
        swap(img[r][c],img[img.size()-(r+1)][c]);
    }}
}

void print_img(vector<vector<char>>& img){
    for(int r = 0; r < img.size(); ++r){
        for(int c = 0; c < img[0].size(); ++c){
            cout << img[r][c];
        }
        cout << endl;
    }
}

vector<pair<int,int>> monster_pattern(){

    vector<pair<int,int>> pattern;
    for(int i = 0; i < 3; ++i){
    for(int j = 0; j < 20; ++j){
        if(MONSTER[i][j] == '#'){
            pattern.push_back(make_pair(i,j));
        }
    }}

    return pattern;
}

bool check_pattern(vector<vector<char>>& img, 
                    vector<vector<char>>& img_map, 
                    vector<pair<int,int>>& pattern,
                    int r, int c){
    for(auto& p : pattern){
        if(img[r+p.first][c+p.second] != '#'){ return false; }
    }
    
    for(auto& p : pattern){
        img_map[r+p.first][c+p.second] = '@';
    }

    return true;
}

string canonical_form(string border){
    string rev = border;
    reverse(rev.begin(), rev.end());
    return (border < rev)? border : rev;
}

int border_match(string a, string b){
    if(a == b){ return 1; }
    reverse(a.begin(), a.end());
    if(a == b){ return -1; }
    return 0;
}

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
    
    void orient_relative_to(tile_t& other){
        int b_ind, oth_b_ind;
        
        vector<string> borders = get_borders();
        vector<string> oth_borders = other.get_borders();
        
        // determine relative orientation:
        bool aligned = false;
        int alignment;
        for(oth_b_ind = 0; oth_b_ind < 4 && !aligned; ++oth_b_ind){
        for(b_ind = 0; b_ind < 4 && !aligned; ++b_ind){
            if((alignment = border_match(borders[b_ind],oth_borders[oth_b_ind]))){
                aligned = true;
            }
        }}
        assert(aligned);
        
        // flip this tile and re-orient if needed:
        if(alignment == 1){
            transpose(); 
            aligned = false;
            borders = get_borders();
            for(oth_b_ind = 0; oth_b_ind < 4 && !aligned; ++oth_b_ind){
            for(b_ind = 0; b_ind < 4 && !aligned; ++b_ind){
                if(border_match(borders[b_ind],oth_borders[oth_b_ind]) == -1){
                    aligned = true;
                }
            }}
        }
        assert(aligned);
        
        // calculate and perform rotations:
        int target_b_ind = (oth_b_ind+2)%4;
        int n_rotations = (4 + (target_b_ind - b_ind))%4;
        for(int i = 0; i < n_rotations; ++i){ rotate(); }
    }
    
    void transpose(){
        for(int r = 0; r < 10; ++r){
        for(int c = r+1; c < 10; ++c){
            swap(tile[r][c],tile[c][r]);
        }}
    }

    // rotates counter-clockwise:
    void rotate(){
        char tmp[10][10];
        for(int r = 0; r < 10; ++r){
        for(int c = 0; c < 10; ++c){
            tmp[r][c] = tile[c][9-r];
        }}

        for(int r = 0; r < 10; ++r){
        for(int c = 0; c < 10; ++c){
            tile[r][c] = tmp[r][c];
        }}
    }
    
    // returns in order: U, L, D, R
    vector<string> get_borders(){
        vector<string> borders;
        char left[11]; 
        char right[11];
        char up[11];
        char down[11];

        for(int i = 0; i < 10; ++i){
            left[i]  = tile[9-i][0];
            right[i] = tile[i][9];
            up[i]    = tile[0][i];
            down[i]  = tile[9][9-i];
        }
        
        up[10] = 0;
        left[10] = 0;
        down[10] = 0;
        right[10] = 0;
        
        borders.push_back(string(up));
        borders.push_back(string(left));
        borders.push_back(string(down));
        borders.push_back(string(right));
        
        return borders;
    }

    void print(ostream& out){
        for(int r = 0; r < 10; ++r){
            cout << string(tile[r]) << endl;
        }
    }

    char pixel_at(int r, int c){
        assert(r < 8 && c < 8);
        return tile[r+1][c+1];        
    }
};

int main(){

    map<string,int> border_count;

    // parse input:
    string token;
    int id;
    vector<string> lines;
    
    // map of border -> tiles with border
    map<string,vector<int>> border_tiles;
    
    // map of tile id -> tile
    map<int,tile_t> tiles;
     
    // parse input:    
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
       
    // categorize all pieces:
    set<int> corner_pieces;
    set<int> edge_pieces;
    set<int> central_pieces;
    set<string> edge_borders;
     
    for(auto& p : tiles){
        int n_neighbors = 0, n_matches = 0;
        for(string b : p.second.get_borders()){
            b = canonical_form(b); 
            n_matches = border_tiles[b].size();
            if(n_matches >= 2){ 
                ++n_neighbors; 
            } else {
                edge_borders.insert(b);
            }
        }
        
        if(n_neighbors <= 2){
            corner_pieces.insert(p.first);
        } else if(n_neighbors == 3){
            edge_pieces.insert(p.first);
        } else {
            assert(n_neighbors == 4);
            central_pieces.insert(p.first);
        }
    }

    cout << "corners:" << endl;
    for(auto p : corner_pieces){
        cout << p << endl;
    }

    cout << "edges:" << endl;
    for(auto p : edge_pieces){
        cout << p << endl;
    }

    cout << "centrals:" << endl;
    for(auto p : central_pieces){
        cout << p << endl;
    }

    // align first corner piece:
    int start_corner = *corner_pieces.begin();
    vector<vector<int>> tile_grid;
    tile_grid.push_back(vector<int>());
    tile_grid[0].push_back(start_corner);
    vector<string> c_borders;
    
    do{
        tiles[start_corner].rotate();
        c_borders = tiles[start_corner].get_borders();
         
    } while(edge_borders.find(canonical_form(c_borders[2])) != edge_borders.end() ||
            edge_borders.find(canonical_form(c_borders[3])) != edge_borders.end() );
    
    // place tiles in tile grid:
    int tiles_placed = 1;
    int margin_tile = start_corner, current_tile = start_corner;
    bool row_done = false;
    
    while(tiles_placed < tiles.size()){
        // place the next tile:
        string next_border;
        int next_tile;

        if(row_done){
            // start the next row:
            next_border = tiles[margin_tile].get_borders()[2];
            vector<int> candidates = border_tiles[canonical_form(next_border)];
            assert(candidates.size() == 2); 
            next_tile = (candidates[0] == margin_tile)? candidates[1] : candidates[0];
            tiles[next_tile].orient_relative_to(tiles[margin_tile]);
            tile_grid.push_back(vector<int>(1,next_tile));
            current_tile = next_tile;
            margin_tile = current_tile;
            row_done = false;
        
        } else {
            // continue previous row:
            next_border = tiles[current_tile].get_borders()[3];
            vector<int> candidates = border_tiles[canonical_form(next_border)];
            assert(candidates.size() == 2);
            next_tile = (candidates[0] == current_tile)? candidates[1] : candidates[0];
            tiles[next_tile].orient_relative_to(tiles[current_tile]);
            tile_grid.back().push_back(next_tile);
            current_tile = next_tile;

        }
           
        string right_border = tiles[current_tile].get_borders()[3];
        row_done = (edge_borders.find(canonical_form(right_border)) != edge_borders.end());
        ++tiles_placed;
    }

    // construct image:
    int n_img_rows = 8*tile_grid.size();
    int n_img_cols = 8*tile_grid[0].size();
    vector<vector<char>> img;
    for(int r = 0; r < n_img_rows; ++r){
        img.push_back(vector<char>(n_img_cols));
        for(int c = 0; c < n_img_cols; ++c){
            img[r][c] = tiles[tile_grid[r/8][c/8]].pixel_at(r%8,c%8);
        }
    }    
    print_img(img); 
    
    bool found_monster = false;
    auto pattern = monster_pattern();

    for(int flip = 0; flip < 2 && !found_monster; ++flip){
        for(int rot = 0; rot < 4 && !found_monster; ++rot){
            // check for sea monsters:
            vector<vector<char>> img_map = img;
            for(int r = 0; r < n_img_rows-3; ++r){
            for(int c = 0; c < n_img_cols-20; ++c){
                found_monster |= check_pattern(img,img_map,pattern,r,c);
            }}

            if(found_monster){
                cout << endl;
                print_img(img_map);
                cout << endl << "Water roughness: " << count_img_char('#', img_map) << endl;
                return 0;
            }
            rotate_img(img);
        }
        hflip_img(img);
    } 
    
    return 1;
}
