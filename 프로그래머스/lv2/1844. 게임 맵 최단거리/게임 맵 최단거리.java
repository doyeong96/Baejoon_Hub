import java.util.*;

class Solution {
    static int[] dr = {0,0,-1,1};
    static int[] dc = {1,-1,0,0};
    static Queue<Point> q;
    static boolean[][] vis;
    static int n,m;
    static int answer;
    
    public static class Point{
        int r;
        int c;
        int cnt;
        public Point(int r, int c, int cnt){
            this.r = r;
            this.c = c;
            this.cnt = cnt;
        }
    }
    
    public int solution(int[][] maps) {
        answer = 0;
        n = maps.length;
        m = maps[0].length;
        vis = new boolean[n][m];
        answer = bfs(0,0,maps);
        return answer;
    }
    
    public int bfs(int r, int c, int[][] maps){
        q = new LinkedList<>();
        q.offer(new Point(r,c,1));
        vis[r][c] = true;
        
        while(!q.isEmpty()){
            Point cur = q.poll();
            if(cur.r == n-1 && cur.c == m-1){
                return cur.cnt;
            }
            
            for(int d=0; d<4; d++){
                int nr = cur.r + dr[d];
                int nc = cur.c + dc[d];
                
                if(0 <= nr && n > nr && 0 <= nc && m > nc){
                    if(maps[nr][nc] == 1 && !vis[nr][nc]){
                        q.offer(new Point(nr,nc, cur.cnt + 1));
                        vis[nr][nc] = true;
                    }
                }
            }
        }
        return -1;
    }
}