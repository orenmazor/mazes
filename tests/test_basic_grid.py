"""Basic grid tests."""
import pytest
from mazes.primitives import Cell, Grid


def test_basic_grid():
    """Confirm we can build a basic grid."""
    grid = Grid((10, 10))

    assert type(grid[(0, 0)]) == Cell
    assert (1, 2) == grid[(1, 2)].position

    me = grid[(1, 1)]
    assert not me.north
    me.link(grid[(0, 1)])
    assert (0, 1) == me.north.position


def test_edges():
    grid = Grid((10, 10))

    northwest = grid[(0, 0)]
    assert northwest

    assert not northwest.west
    assert not northwest.north

    assert not northwest.is_linked(northwest.west)
    assert not northwest.is_linked(None)
    with pytest.raises(AssertionError):
        northwest.link(None)
