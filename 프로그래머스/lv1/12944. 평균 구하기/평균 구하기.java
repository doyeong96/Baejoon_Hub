class Solution {
    public double solution(int[] arr) {
        double answer = 0;
        double n = arr.length;
        int hap = 0;
        for(int i:arr){
            hap += i;
        }
        answer = hap/n;
        System.out.println(answer);
        return answer;
    }
}