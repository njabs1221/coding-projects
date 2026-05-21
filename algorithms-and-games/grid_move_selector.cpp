#include <iostream>
#include <vector>
#include <cmath>
#include <string>
#include <algorithm>

using namespace std;

int main(){
    int cols, rows;
    cin >> cols >> rows;

    int ax, ay;
    cin >> ax >> ay;

    int N;
    cin >> N;

    vector<vector<int>> mat(rows, vector<int>(cols, 0));

    mat[ay][ax] = 5;

    int head1, head2;

    for(int p = 1; p <= N; p++){
        int a, b, c, d, e, f;
        cin >> a >> b >> c >> d >> e >> f;
        mat[b][a] = p;
        mat[d][c] = p;
        mat[f][e] = p;
        if(p == 1){
            head1 = a;
            head2 = b;
        }
    }

    vector<pair<string, pair<int,int>>> moves = {
        {"DOWN",  {0,  1}},
        {"LEFT",  {-1, 0}},
        {"RIGHT", { 1, 0}},
        {"UP",    {0, -1}}
    };

    double bestDist = 1e18;
    vector<string> bestMoves;

    for(auto& m : moves){
        string dir = m.first;
        int nx = head1 + m.second.first;
        int ny = head2 + m.second.second;

        if(nx < 0 || nx >= cols || ny < 0 || ny >= rows)
            continue;

        int cell = mat[ny][nx];
        if(cell >= 1 && cell <= 4)
            continue;

        double dist = sqrt(pow(nx - ax, 2) + pow(ny - ay, 2));

        if(dist < bestDist){
            bestDist = dist;
            bestMoves.clear();
            bestMoves.push_back(dir);
        } else if(dist == bestDist){
            bestMoves.push_back(dir);
        }
    }

    sort(bestMoves.begin(), bestMoves.end());

    for(auto& s : bestMoves)
        cout << s << "\n";

    return 0;
}