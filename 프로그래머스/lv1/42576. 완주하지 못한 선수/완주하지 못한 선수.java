import java.util.*;
class Solution {
    public String solution(String[] participant, String[] completion) {
        String answer = "";
        HashMap<String, Integer> hm = new HashMap<>();
        
        for(int i=0; i< participant.length; i++){
            hm.put(participant[i], hm.getOrDefault(participant[i],0)+1);
        }
        
        for(int j=0; j<completion.length; j++){
            hm.put(completion[j], hm.get(completion[j]) -1);
        }
        
        for(String key : hm.keySet()){
            if(hm.get(key) != 0){
                answer = key;
                break;
            }
        }
        return answer;
    }
}