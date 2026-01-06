// Given the root of a binary tree, the level of its root is 1, the level of its children is 2, and so on.

// Return the smallest level x such that the sum of all the values of nodes at level x is maximal.

 
/**
 * Definition for a binary tree node.
 * class TreeNode {
 *     val: number
 *     left: TreeNode | null
 *     right: TreeNode | null
 *     constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
 *         this.val = (val===undefined ? 0 : val)
 *         this.left = (left===undefined ? null : left)
 *         this.right = (right===undefined ? null : right)
 *     }
 * }
 */

function maxLevelSum(root: TreeNode | null): number {
    let levels = []

    function dfs(node: TreeNode | null, level: number) {
        if (node == null) {
            return
        }
        if (levels.length === level) {
            levels.push(0)
        }
        levels[level] += node.val
        dfs(node.left, level + 1)
        dfs(node.right, level + 1)
    }

    dfs(root, 0)

    let max = -1 * (10 ** 6)
    let mxIndex = -1
    
    for (let i = 0; i < levels.length; i++) {
        if(max < levels[i]){
            max = levels[i]
            mxIndex = i
        }
    }
    return mxIndex + 1
};
