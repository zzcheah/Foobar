import java.math.BigInteger;

class Scratch {
    public static void main(String[] args) {
        System.out.println(solution("4", "1"));
    }


    public static String solution(String x, String y) {
        // Your code here
        if(x.equals("1") && y.equals("1")){
            return "impossible";
        }

        BigInteger m = new BigInteger(x);
        BigInteger f = new BigInteger(y);
        BigInteger step = BigInteger.ZERO;

        if (m.compareTo(BigInteger.ONE) < 0 || f.compareTo(BigInteger.ONE) < 0 || m.compareTo(f) == 0) {
            return "impossible";
        }

        BigInteger larger;
        BigInteger smaller;

        if (m.compareTo(f) > 0) {
            larger = m;
            smaller = f;
        } else {
            larger = f;
            smaller = m;
        }

        while (larger.compareTo(BigInteger.ZERO) > 0 && smaller.compareTo(BigInteger.ZERO) > 0) {


            if(smaller.compareTo(BigInteger.ONE)==0) {
                step = step.add(larger.divide(smaller)).subtract(BigInteger.ONE);
                break;
            } else {

                BigInteger whole = larger.divide(smaller);
                BigInteger remainder = larger.mod(smaller);

                larger = smaller;
                smaller = remainder;

                step = step.add(whole);

            }

        }

        if(smaller.compareTo(BigInteger.ONE)<0 || larger.compareTo(BigInteger.ONE)<0) {
            return "impossible";
        }

        return step.toString();

    }

}