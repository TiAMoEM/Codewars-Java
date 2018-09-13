public class Solution {
    public static int century(int number) {
        // your code goes here
        if (number % 100 == 0){
            return number / 100;
        }else {
            return number / 100 + 1;
        }
    }
}