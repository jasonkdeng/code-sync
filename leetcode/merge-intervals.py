class Solution {
    public int[][] merge(int[][] intervals) {
        int start;
        int end;
        int latestEnd = 0;
        List <int[]> result = new ArrayList <int[]> ();
        Arrays.sort(intervals, (a,b) -> Integer.compare(a[0], b[0]));
        for (int i = 0; i < intervals.length; i++) {
            start = intervals[i][0];
            end = intervals[i][1];

            if (!result.isEmpty() && latestEnd >= end) {
                continue;
            }

            for (int j = i + 1; j < intervals.length; j++) {
                if (intervals[j][0] <= end) {
                    end = Math.max(intervals[j][1], end);

                }
            }
            result.add(new int[]{start, end});
            latestEnd = end;
        }
        int [][] res = new int [result.size()][];
        res = result.toArray(res);
        return res;
    }
}