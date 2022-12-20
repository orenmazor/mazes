from mazes.primitives import Cell, Grid


def test_basic_grid():
    """Confirm we can build a basic grid."""
    grid = Grid((10, 10))

    assert type(grid[(0, 0)]) == Cell
    assert (1, 2) == grid[(1, 2)].location

    me = grid[(1, 1)]
    assert (0, 1) == me.north.location
    assert (2, 1) == me.south.location
    assert (1, 0) == me.west.location
    assert (1, 2) == me.east.location
