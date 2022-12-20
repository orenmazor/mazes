from mazes.primitives import Grid
from mazes.algorithms import binary_tree


def test_binary_tree():
    """Test a binary tree."""
    grid = Grid((4, 4))
    binary_tree(grid)

    print(
        "the binary tree will always bias to having full hallways that meet kitty corner from the origin. so in our case, the bottom row and the east row will be hallways."
    )
    print(grid)
