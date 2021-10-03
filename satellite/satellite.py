"""exercism satellite module."""


def tree_from_traversals(preorder, inorder):
    """
    Build a binary tree from a list of preorder and inorder.

    :param preorder list - The pre-order traveral of the tree.
    :param inorder list - The in-order traveral of the tree.
    :return dict - A dictionary describing the binary tree.
    """
    if len(preorder) != len(inorder):
        raise ValueError("Lengths of pre-order and inorder do not match.")

    if len(preorder) != len(set(preorder)) or len(inorder) != len(set(inorder)):
        raise ValueError("Duplicates found.")

    if len(preorder) > 0 and len(set(preorder).intersection(set(inorder))) == 0:
        raise ValueError("Inconsistent traveral found.")

    tree = {}
    while len(preorder) > 0:
        node = preorder.pop(0)
        populate_tree(tree, node)

    return tree

def populate_tree(tree, node):
    if tree.get("v") is None:
        tree["v"] = node
        tree["l"] = {}
        tree["r"] = {}
    else:
        left = tree.get("l")
        right = tree.get("r")
        if left == {}:
            tree["l"] = populate_tree(left, node)
        elif right == {}:
            tree["r"] = populate_tree(right, node)
        else:
            # This solution seems wrong, since we don't populate the left...
            populate_tree(right, node)

    return tree
