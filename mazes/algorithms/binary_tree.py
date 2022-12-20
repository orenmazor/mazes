"""Implementation of the binary tree maze."""
from random import choice, random

from mazes.primitives import Grid


def binary_tree(grid: Grid) -> None:
    """Just a basic bitch binary tree."""
    # since we are moving from the north west point instead
    # of the south west point, this basic walk flips the options
    # from north/east to south/east
    for position, cell in grid.each_cell():
        possible_directions = {}

        # account for the south direction
        if position[0] < grid.inner.shape[0] - 1:
            possible_directions["south"] = (position[0] + 1, position[1])

        # account for the east direction
        if position[1] < grid.inner.shape[1] - 1:
            possible_directions["east"] = (position[0], position[1] + 1)

        if not possible_directions:
            # this happens when we are at the corner
            # which means we're done
            return

        random_direction = choice(list(possible_directions.keys()))

        setattr(cell, random_direction, grid[possible_directions[random_direction]])
