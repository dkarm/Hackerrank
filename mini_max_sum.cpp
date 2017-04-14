#include <map>
#include <set>
#include <list>
#include <cmath>
#include <ctime>
#include <deque>
#include <queue>
#include <stack>
#include <string>
#include <bitset>
#include <cstdio>
#include <limits>
#include <vector>
#include <climits>
#include <cstring>
#include <cstdlib>
#include <fstream>
#include <numeric>
#include <sstream>
#include <iostream>
#include <algorithm>
#include <unordered_map>

using namespace std;


int main(){
    long int a;
    long int b;
    long int c;
    long int d;
    long int e;
    cin >> a >> b >> c >> d >> e;

    
    vector <long int> sums;
    
    sums.push_back(a+b+c+d);
    sums.push_back(b+c+d+e);
    sums.push_back(a+c+d+e);
    sums.push_back(a+b+d+e);
    sums.push_back(a+b+c+e);
    
    sort(sums.begin(), sums.end());
    
    cout << sums[0] << " " << sums[4];
    
    return 0;
}

