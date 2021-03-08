import java.math.BigInteger;

public class Solution {
    public static String solution(int[] xs) {
        // Your code here
        int leftOut = -1001;
        int posCount = 0;
        int negCount = 0;
        int neutralCount = 0;
        BigInteger posProduct = new BigInteger(String.valueOf(1));
        BigInteger negProduct = new BigInteger(String.valueOf(1));
        BigInteger finalProduct = new BigInteger(String.valueOf(1));

        if(xs.length==1) {
            if(xs[0]<0) {
                return String.valueOf(xs[0]);
            }
        }

        for (int i = 0; i < xs.length; i++) {

            int num = xs[i];

            if (num == -1) {
                neutralCount++;
            }

            if (num < -1) {
                negProduct = negProduct.multiply(BigInteger.valueOf(num));
                negCount++;
                if (num > leftOut) {
                    leftOut = num;
                }
            }

            if (num >= 1) {
                posCount++;
                posProduct = posProduct.multiply(BigInteger.valueOf(num));
            }

        }


        posProduct = posCount == 0 ? BigInteger.ZERO : posProduct;

        if (negCount == 0) {

            if (neutralCount > 0 && neutralCount % 2 == 0) {
                negProduct = BigInteger.ONE;
            } else {
                negProduct = BigInteger.ZERO;
            }

        } else if (negCount == 1) {

            if (neutralCount != 0) {
                negProduct = negProduct.multiply(BigInteger.valueOf(-1));
            } else {
                negProduct = BigInteger.ZERO;
            }

        } else {
            if (negProduct.compareTo(BigInteger.valueOf(0)) < 0) {
                if (neutralCount != 0) {
                    negProduct = negProduct.multiply(BigInteger.valueOf(-1));
                } else {
                    negProduct = negProduct.divide(BigInteger.valueOf(leftOut));
                }
            }
        }


        if (posProduct.compareTo(BigInteger.ZERO)==0 && negProduct.compareTo(BigInteger.ZERO)==0) {
            finalProduct=BigInteger.ZERO;
        } else {
            if (posProduct.compareTo(BigInteger.ZERO)==0) {
                finalProduct = negProduct;

            } else {
                if (negProduct.compareTo(BigInteger.ZERO)==0) {
                    finalProduct = posProduct;
                } else {
                    finalProduct = posProduct.multiply(negProduct);
                }

            }
        }


        return finalProduct.toString();

    }
}