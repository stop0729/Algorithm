#include <string>
#include <vector>

using namespace std;

int solution(string name) {
    int answer = 0;
    int length = name.size();
    int LR = length - 1;
    int index;
    
    for(int i=0; i<length; i++){
        int temp = name[i] - 'A';
        if(temp > 13) temp = 26 - temp;
        answer += temp;
        
        index = i+1;
        while(name[index] == 'A') index++;
        int tmp = min(2*i + length - index, i + 2 * (length - index));
        if(tmp < LR) LR = tmp;
    }
    answer += LR;
    return answer;
}