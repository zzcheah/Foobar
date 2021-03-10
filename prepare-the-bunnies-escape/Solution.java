import java.util.LinkedList;

public class Solution {
    public static int solution(int[][] map) {
        // Your code here
        LinkedList<Node> queue = new LinkedList<>();
        Node start = new Node(0, 0, 1, "na",true);
        int row = map.length;
        int col = map[0].length;

        int[][][] memo = new int[row][col][2];


        queue.add(start);

        while (!queue.isEmpty()) {

            Node node = queue.poll();
            int x = node.x;
            int y = node.y;
            String from = node.from;
            int next = node.distance + 1;
            boolean power = node.power;

            if(power) {
                int path = memo[x][y][1];
                if(path == 0) {
                    memo[x][y][1]= node.distance;
                } else {
                    if(path<= node.distance) continue;
                }
            } else {
                int path = memo[x][y][0];
                if(path == 0) {
                    memo[x][y][0]= node.distance;
                } else {
                    if(path<= node.distance) continue;
                }
            }

            if(x==row-1 && y==col-1) {
                return node.distance;
            }




            // right
            if (y < col - 1 && !from.equals("right")) {
                boolean blocked = map[x][y + 1] == 1;
                if (blocked) {
                    if (power) {
                        queue.add(new Node(node.x, node.y + 1, next, "left",false));
                    }
                } else {
                    queue.add(new Node(node.x, node.y + 1, next, "left",power));
                }
            }

            // down
            if (x < row - 1 && !from.equals("down")) {
                boolean blocked = map[x + 1][y] == 1;
                if (blocked) {
                    if(power) {
                        queue.add(new Node(node.x + 1, node.y, next, "up", false));
                    }
                } else {
                    queue.add(new Node(node.x + 1, node.y, next, "up", power));
                }
            }

            // up
            if (x > 0 && !from.equals("up")) {
                if (map[x - 1][y] == 1) {
                    if(power) {
                        queue.add(new Node(node.x - 1, node.y, next, "down", false));
                    }
                } else {
                    queue.add(new Node(node.x - 1, node.y, next, "down", power));
                }
            }

            // left
            if (y > 0 && !from.equals("left")) {
                if (map[x][y - 1] == 1) {
                    if (power) {
                        queue.add(new Node(node.x, node.y - 1, next, "right", false));
                    }
                } else {
                    queue.add(new Node(node.x, node.y - 1, next, "right", power));
                }
            }


        }

        return -99;
    }

    static class Node {

        public Node(int x, int y, int distance, String from, boolean power) {
            this.x = x;
            this.y = y;
            this.distance = distance;
            this.from = from;
            this.power = power;
        }

        int x;
        int y;
        int distance;
        String from;
        boolean power;
    }
}