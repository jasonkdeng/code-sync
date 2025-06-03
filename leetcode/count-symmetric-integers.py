class Solution {
    public int countSymmetricIntegers(int low, int high) {
        int count = 0;
        for (int i = low; i < high + 1; i++) {
            if (i > 10 && i < 100) {
                if (sumDigs (i/10) == sumDigs (i%10)) {
                    count ++;
                }
            }
            else if (i > 1000 && i < 10000) {
                if (sumDigs (i/100) == sumDigs (i%100)) {
                    count ++;
                }
            }
        }
        return count;
    }
    public int sumDigs (int n) {
        if (n/10 == n) {
            return n;
        }
        return (n%10 + sumDigs (n/10));
    }
}