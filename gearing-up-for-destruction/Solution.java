class Scratch {

    public static void main(String[] args) {
        int[] temp = solution(new int[]{1, 51});
        System.out.printf("[%d,%d]%n",temp[0],temp[1]);

    }

    public static int[] solution(int[] pegs) {

        // Your code here

        if(pegs.length<2) {
            return new int[] {-1,-1};
        }

        boolean even = pegs.length % 2 == 0;
        int[] distances = new int[pegs.length - 1];
        for (int i = 0; i < distances.length; i++) {
            distances[i] = pegs[i + 1] - pegs[i];
        }


        int sum = 0;
        boolean sign = true;
        for (int i = 0; i < distances.length; i++) {

            if (sign) sum += distances[i];
            else sum -= distances[i];

            sign = !sign;
        }

        int a = sum * 2;
        int b = even ? 3 : 1;

        if (a % b == 0) {
            a = a / b;
            b = 1;
        }

        float radius = (float) a / (float) b;

        if (radius < 1) return new int[]{-1, -1};

        for (int distance : distances) {
            if (radius > distance - 1) return new int[]{-1, -1};
            radius = distance - radius;
        }

        return new int[]{a, b};
    }

}