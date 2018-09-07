public class Solution {
    public static String repeatStr(final int repeat, final String string) {
        if (repeat <= 0){
            return "";
        }
        String str = string;
        for (int i = 0; i < repeat - 1; i ++){
            str += string;
        }
        return str;
    }
}