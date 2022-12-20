from mazes.primitives import Grid
from mazes.algorithms import binary_tree


def test_binary_tree():
    """Test a binary tree."""
    grid = Grid((4, 4))
    binary_tree(grid)

    print(grid)
