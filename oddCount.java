public class Kata {

  public static int oddCount(int n){
    int count = 0;
    for (int i = 1; i < n; i += 2) count += 1;
    return count;
  }

}