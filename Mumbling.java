public class Accumul {
    public static String accum(String s) {
        StringBuffer sb = new StringBuffer();
        s = s.toLowerCase();
        for (int i=0; i<s.length(); i++){
            for (int j=0; j<=i; j++) {
                if (j == 0){
                    sb.append((char)(s.charAt(i) - 32));
                }else {
                    sb.append(s.charAt(i));
                }
            }
            sb.append('-');
        }
        sb.toString();
        return sb.substring(0, sb.length() - 1);
    }
}