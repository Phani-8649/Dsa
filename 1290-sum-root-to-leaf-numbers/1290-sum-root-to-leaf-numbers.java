/**
 * Definition for binary tree
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    public int sumNumbers(TreeNode root) {
        if(root == null) {
            return 0;
        }
        // Note: The Solution object is instantiated only once and is reused by each test case.
        ArrayList<Integer> sums = new ArrayList<Integer>();
        sumNumbersHelper(root, new ArrayList<Integer>, sums);
        int sum = 0;
        for(int n: sums) {
            sum += n;
        }
        return sum;
    }
    
    static void sumNumbersHelper(TreeNode root, ArrayList<Integer> path, ArrayList<Integer> sums) {
        path.add(root.val);
        if(root.left == null && root.right == null) {
            sums.add(numList(path));
        }
        if(root.right != null) {
            sumNumbersHelper(root.right, path, sums);
        }
        if(root.left != null) {
            sumNumbersHelper(root.left, path, sums);
        }
        path.remove(path.size()-1);
    }
    
    static int numList(ArrayList<Integer> path) {
        int num = 0;
        for(int k = path.size()-1, i = 1; k >=0; k--, i *= 10) {
            num += path.get(k)*i;
        }
        return num;
    }
}