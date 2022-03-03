package java_ps.ps_tree;

import java.util.ArrayList;
import java.util.List;

public class LeetCode144 {

    // Pre-order Traverse(전위순회) = 부모노드 -> 왼쪽 자식 -> 오른쪽 자식

    // Definition for a binary tree node.
    static class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }
    }

    public List<Integer> preorderTraversal(TreeNode root) {

        List<Integer> result = new ArrayList<>();
        preOrder(root, result);
        return result;
    }

    public void preOrder(TreeNode root, List<Integer> result) {

        if(root == null) {
            return;
        }
        result.add(root.val);

        preOrder(root.left, result);
        preOrder(root.right, result);
    }
}
