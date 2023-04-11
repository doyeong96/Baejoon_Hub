import java.util.*;
import java.io.*;

public class Main {
    static class Pair implements Comparable<Pair> {
        int start, end;

        Pair(int start, int end) {
            this.start = start;
            this.end = end;
        }

        public int compareTo(Pair p) {
            if (this.start == p.start)
                return this.end - p.end;
            return this.start - p.start;
        }
    }

    static class FastReader {
        BufferedReader br;
        StringTokenizer st;

        public FastReader() {
            br = new BufferedReader(new InputStreamReader(System.in));
        }

        String next() {
            while (st == null || !st.hasMoreElements()) {
                try {
                    st = new StringTokenizer(br.readLine());
                } catch (IOException e) {
                    e.printStackTrace();
                }
            }
            return st.nextToken();
        }

        int nextInt() {
            return Integer.parseInt(next());
        }
    }

    static FastReader input = new FastReader();

    public static void main(String[] args) {
        int n = input.nextInt();
        Pair[] pairs = new Pair[n];

        for (int i = 0; i < n; i++) {
            int start = input.nextInt();
            int end = input.nextInt();
            pairs[i] = new Pair(start, end);
        }

        Arrays.sort(pairs);

        PriorityQueue<Integer> pq = new PriorityQueue<>();
        for (Pair p : pairs) {
            if (pq.isEmpty())
                pq.add(p.end);
            else {
                if (pq.peek() <= p.start) {
                    pq.poll();
                    pq.add(p.end);
                } else {
                    pq.add(p.end);
                }
            }
        }

        System.out.println(pq.size());
    }
}
