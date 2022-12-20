"""Maze primitives."""
from __future__ import annotations

from numpy import array, ndenumerate, full
from typing import Tuple, Dict, List, Generator, Optional
from random import randint


class Grid(object):
    """A basic implementation of a maze grid."""

    inner: array

    def __init__(self: Grid, shape: Tuple[int, int]) -> None:
        super().__init__()

        self.inner = full(shape, Cell((-1, -1)))
        self.populate_grid()
        # self.configure_cells()

    def populate_grid(self: Grid) -> None:
        """Populate the grid with disjoint cells."""
        for position, _ in ndenumerate(self.inner):
            self.inner[position] = Cell(position=position)

    def __getitem__(self: Grid, key: Tuple) -> Cell:
        """Return item in the grid."""
        return self.inner[key]

    def random(self: Grid) -> Cell:
        """Return a random cell."""
        random_row = randint(0, self.inner.shape[0])
        random_col = randint(0, self.inner.shape[1])
        return self.inner[(random_row, random_col)]

    def size(self: Grid) -> int:
        """Return array size."""
        return self.inner.size

    def each_row(self: Grid) -> Generator:
        """Yield a row at a time."""
        for row in self.inner:
            yield row

    def each_cell(self: Grid) -> Generator:
        """Yield a cell and a position at a time."""
        for position, cell in ndenumerate(self.inner):
            if cell:
                yield (position, cell)

    def __repr__(self: Grid) -> str:
        """Return a visual representation of the maze."""

        def print_line() -> str:
            return "+" + "---+" * self.inner.shape[1] + "\n"

        result = "\n" + print_line()
        for row in self.each_row():
            bottom_line = "+"
            current_row = "|"

            for cell in row:
                # we only look at east and south
                # because those are the directions
                # we are moving in

                # first add our body of the cell
                current_row += "   "

                if cell.east:
                    # we have a way east
                    # so draw an empty space
                    current_row += " "
                else:
                    current_row += "|"

                if cell.south:
                    # we have a way south
                    # so draw an empty space
                    bottom_line += "   +"
                else:
                    bottom_line += "---+"

            current_row += "\n"
            bottom_line += "\n"
            result += current_row
            result += bottom_line

        return result


class Cell(object):
    """A cell is a single position in a maze and is aware of its neighbours."""

    position: tuple
    links: dict = {}
    north: Optional[Cell] = None
    south: Optional[Cell] = None
    east: Optional[Cell] = None
    west: Optional[Cell] = None

    def __init__(self: Cell, position: Tuple) -> None:
        """Initialize the position."""
        self.position = position

    def link(self: Cell, sibling: Cell, bidirectional: bool = False) -> None:
        """Link a sibling cell."""
        # we should never get a none
        assert sibling

        if sibling.position[0] == self.position[0]:
            # we are on the same row
            if sibling.position > self.position:
                self.east = sibling
            else:
                self.west = sibling

        elif sibling.position[1] == self.position[1]:
            if sibling.position > self.position:
                self.south = sibling
            else:
                self.north = sibling

        if bidirectional:
            # we dont want to get in here yet
            return
            sibling.link(self)

    def is_linked(self: Cell, sibling: Cell) -> bool:
        """Check if we are linked to this cell."""
        return sibling in self.neighbours()

    def directions(self: Cell) -> List[Tuple[int, int]]:
        """Return a list of possible directions from here.

        These may not all be legal.
        """
        _directions = []

        # we can move west
        _directions.append((self.position[0] - 1, self.position[1]))
        # we can move east
        _directions.append((self.position[0] + 1, self.position[1]))

        # we can move north
        _directions.append((self.position[0], self.position[1] - 1))

        # we can move south
        _directions.append((self.position[0], self.position[1] + 1))

        return _directions

    def neighbours(self: Cell) -> List[Cell]:
        """Return list of neighbours."""
        return list(filter(lambda x: x, [self.north, self.south, self.east, self.west]))

    def __repr__(self: Cell) -> str:
        """Return a representation of the cell."""
        result = f"Cell(position=({self.position})"

        if self.west:
            result += f", west={self.west.position}"

        if self.east:
            result += f", east={self.east.position}"

        if self.north:
            result += f", north={self.north.position}"

        if self.south:
            result += f", south={self.south.position}"

        return result
