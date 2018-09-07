public class TwiceAsOld{

  public static int TwiceAsOld(int dadYears, int sonYears){
    //TODO: Add code here
    if ((dadYears - 2 * sonYears) < 0){
      return (2 * sonYears - dadYears);
    } else{
      return (dadYears - 2 * sonYears);
    }
  }

}