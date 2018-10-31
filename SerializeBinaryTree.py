class Node:
    """
    Each node has an integer value, and optionally has left and right children
    """
    pass
    
def serialize_tree(root_node):
    """
    Serializes a tree from top to bottom, left to right to a list of values

    Parameters
    ----------
    root_node : root node of a binary tree
        The tree is not ordered or balanced, it's just a binary tree
        Example:
            1
           / \
          2   3
         / \ / \
           4 2
      
    Returns
    -------
    serial_tree :  A list of serialized values
        Example: [1,2,3,None,4,2,None]
    """