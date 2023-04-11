class Solution {
    public long[] solution(int x, int n) {
        long[] answer = new long[n];
        long num = x;
        int a = n;
        for(int i = 0; i < a; i++){
            answer[i] = num;
            num += x;
        }
        return answer;
    }
}