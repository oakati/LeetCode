/**
 * Definition for a binary tree node.
 * struct TreeNode {
 *     int val;
 *     TreeNode *left;
 *     TreeNode *right;
 *     TreeNode() : val(0), left(nullptr), right(nullptr) {}
 *     TreeNode(int x) : val(x), left(nullptr), right(nullptr) {}
 *     TreeNode(int x, TreeNode *left, TreeNode *right) : val(x), left(left), right(right) {}
 * };
 */
class Solution {
public:
    vector<int> inorderTraversal(TreeNode* root) {
        std::vector<int> result;
        inorderTraversalHelper(root, result);
        return result;
    }

    void inorderTraversalHelper(TreeNode* root, std::vector<int>& result) {
        if (root) {
            inorderTraversalHelper(root->left, result);
            result.push_back(root->val);
            inorderTraversalHelper(root->right, result);
        }
    }
};