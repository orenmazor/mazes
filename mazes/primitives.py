"""Maze primitives."""
from __future__ import annotations

from numpy import array, ndenumerate, full
from typing import Tuple, Dict, List, Generator
from random import randint


class Grid(object):
    """A basic implementation of a maze grid."""

    inner: array

    def __init__(self: Grid, shape: Tuple[int, int]) -> None:
        super().__init__()

        self.inner = full(shape, Cell((-1, -1)))
        self.populate_grid()
        self.configure_cells()

    def populate_grid(self: Grid) -> None:
        """Populate the grid with disjoint cells."""
        for position, _ in ndenumerate(self.inner):
            self.inner[position] = Cell(position=position)

    def configure_cells(self: Grid) -> None:
        """Connect all cells in a grid to all of their neighbours."""
        for position, cell in ndenumerate(self.inner):
            row, col = position
            if row != 0:
                cell.north = self.inner[(row - 1, col)]
            if row != self.inner.shape[0] - 1:
                cell.south = self.inner[(row + 1, col)]
            if col != self.inner.shape[1] - 1:
                cell.east = self.inner[(row, col + 1)]
            if col != 0:
                cell.west = self.inner[(row, col - 1)]

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


class Cell(object):
    """A cell is a single location in a maze and is aware of its neighbours."""

    location: tuple
    links: dict
    north: Cell
    south: Cell
    east: Cell
    west: Cell

    def __init__(self: Cell, position: Tuple) -> None:
        """Initialize the position."""
        self.location = position

    def link(self: Cell, sibling: Cell, bidirectional: bool = False) -> Cell:
        """Link a sibling cell."""
        self.links[sibling] = True
        if bidirectional:
            sibling.link(self)

        return self

    def unlink(self: Cell, sibling: Cell, bidirectional: bool = False) -> Cell:
        """Unlink a sibling cell."""
        del self.links[sibling]
        if bidirectional:
            sibling.unlink(self)

        return self

    def is_linked(self: Cell, sibling: Cell) -> bool:
        """Check if we are linked to this cell."""
        return sibling in self.links

    def get_links(self: Cell) -> Dict:
        """Return list of links."""
        return self.links

    def neighbours(self: Cell) -> List:
        """Return list of neighbours."""

        return list(filter(lambda x: x, [self.north, self.south, self.east, self.west]))
