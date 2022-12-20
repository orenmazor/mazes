from mazes.primitives import Grid
from mazes.algorithms import sidewalker


def test_sidewalker_tree():
    """Test a sidewalker tree."""
    grid = Grid((4, 4))
    sidewalker(grid)

    print(
        "The sidewalker/winder algorithm biases towards having one unbroken hallway on the side opposite from the starting point. so in our case it'll be the entire bottom row clear."
    )
    print(grid)
