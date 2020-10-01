#include<bits/stdc++.h>
using namespace std;

#define v(type) vector<type>
#define v2(type) vector<vector<type> >
#define vsort(vec) sort(vec.begin(), vec.end())
#define gr(type) greater<type>()
#define rvsort(vec, type) sort(vec.begin(), vec.end(), gr(type))
#define bsrch(s,e,n) binary_search(s,e,n)
#define ubnd(s,e,n) upper_bound(s,e,n)-s
#define lbnd(s,e,n) lower_bound(s,e,n)-s
#define ll long long int
#define pb push_back
#define iterator(type) vector<type>::iterator
#define mp(type1, type2) map<type1, type2>
#define mmp(type1, type2) multimap<type1, type2>
#define ump(type1, type2) unordered_map<type1, type2>
#define mump(type1, type2 ) unordered_multimap<type1, type2>
#define s(type) set<type>
#define ms(type) multiset<type>
#define pr(type1, type2) pair<type1, type2>
#define mpr(n,m) make_pair(n,m)
#define stk(type) stack<type>
#define pqb(type) priority_queue<type>
#define pqs(type) priority_queue<type, v(type), greater<type>>
#define setbits(x) __builtin_popcountll(x)
#define zrobits(x) __builtin_ctzll(x)
#define mod 1000000007
#define inf 1e18
#define ps(x, y) fixed<<setprecision(y)<<x
#define floop(x,i,n) for(x=i; x<n; x++)
#define vfloop(v) for(auto &val: v)
#define w(x) int x; cin >> x; while(x--) 
#define endl "\n"
#define out(x) cout << x << endl
#define in(x) cin >> x
#define clr(val) memset(val,0,sizeof(val))
#define what_is(x) cerr << #x << " is " << x << endl; 
#define OJ \
    freopen("input.txt", "r", stdin); \
    freopen("output.txt", "w", stdout);
#define FIO ios_base::sync_with_stdio(false);cin.tie(NULL);cout.tie(NULL);
#define split(str, tokens, delim)  stringstream ss(str); string temp; while(getline(ss, temp, delim))tokens.pb(temp);


// bool comp(const v(int)&v1, const v(int)&v2){
    // if ((v1[0]*v1[0] + v1[1]*v1[1]) < (v2[0]*v2[0] + v2[1]*v2[1]))
        // return true;
    // return false;
// }

int tsp(int mask, int pos, int n,const v2(int)&dist, v(int)&path){
    if(mask == (1<<n)-1) return dist[pos][0];
    int ans = INT_MAX;
    for(int nextcity=1;nextcity<n;nextcity++){
        if(((mask&(1<<nextcity)) == 0)&& pos!=nextcity){
            int d = dist[pos][nextcity] + tsp(mask|(1<<nextcity), nextcity, n, dist, path);
            if(d < ans){
                path[pos] = nextcity;
                cout << "pos: " << pos << "path: " << path[pos] << endl;
                ans = d;
            }
        }
    }
    return ans; 
}

int main(){
    OJ;
    string locations;
    getline(cin, locations);
    v(string) tok;
    split(locations, tok, ';');
    int l = tok.size();
    v2(int) coord(l+1, v(int)(2)); // 2D vector to store coord.
    coord[0][0]=0, coord[0][1]=0;
    for(int i=0; i<l; i++){
        v(string) s;
        split(tok[i], s, '|');
        coord[i+1][0] = stoi(s[0]);
        coord[i+1][1] = stoi(s[1]);
        s.clear();
    }
    tok.clear();

    // vfloop(coord)
    // cout << val[0] << " " << val[1] <<endl;
    v2(int) adMat(l+1, v(int)(l+1));

    for(int i=0; i<l+1; i++){
        for(int j=0; j<l+1; j++){
            int x = (coord[i][0]-coord[j][0])*(coord[i][0]-coord[j][0]);
            int y = (coord[i][1]-coord[j][1])*(coord[i][1]-coord[j][1]);

            adMat[i][j] = floor(pow((x+y),0.5));
        }
    }

    coord.clear();

    for(int i=0; i<l+1; i++){
        for(int j=0; j<l+1; j++){
            cout << adMat[i][j] << " ";
        }
        cout << endl;
    }
    v(int) path(l+1, -1);
    int ans = tsp(1,0,l+1,adMat, path);
    cout << ans;
    cout << endl;
    vfloop(path){
        out(val);
    }
}