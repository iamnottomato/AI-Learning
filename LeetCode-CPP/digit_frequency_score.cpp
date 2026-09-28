#include <iostream>
#include <vector>
using namespace std;

int digitFrequencyScore(int n) {
    int box[10] = {0};
    while(n>0){
        int d = n%10;
        box[d]++;
        n = n/10;
    }
    int ans = 0;
    for(int i = 0; i < 10; i++){
        ans += i * box[i];
    }
    return ans;
}

int main(){
    int num;
    cin >> num;
    cout << digitFrequencyScore(num) << endl;
    return 0;
}
