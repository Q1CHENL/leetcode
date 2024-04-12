
// Definition for a binary tree node.
class TreeNode {
    val: number
    left: TreeNode | null
    right: TreeNode | null
    constructor(val?: number, left?: TreeNode | null, right?: TreeNode | null) {
        this.val = (val===undefined ? 0 : val)
        this.left = (left===undefined ? null : left)
        this.right = (right===undefined ? null : right)
    }
}

function isSymmetric(root: TreeNode | null): boolean {
    if (root === null) return true
    // Handle special case
    if (root.left !== null && root.right!== null && root.left.val !== root.right.val) return false
    let valArray = inOrderTravere(root)
    if (valArray.length % 2 == 0) return false
    return valArray.toString() === valArray.reverse().toString()
};

// Traverse order: left, root, right
function inOrderTravere(root: TreeNode | null): number[] {
    // Handle special case
    if (root == null) return [-999]
    if (root.left === null && root.right == null) return [root.val]
    return inOrderTravere(root.left).concat([root.val]).concat(inOrderTravere(root.right))
}

// Special cases:
// [1,2,2,2,null,2]
// [5,4,1,null,1,null,4,2,null,2,null]
// Notice: the array is formed from the tree top-down layer by layer

const node7 = null;
const node6 = new TreeNode(2);
const node5 = null;
const node4 = new TreeNode(2);
const node3 = new TreeNode(2, node6, node7);
const node2 = new TreeNode(2, node4, node5);
const root = new TreeNode(1, node2, node3);

console.log(isSymmetric(root))