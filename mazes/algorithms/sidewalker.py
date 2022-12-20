"""Implementation of the sidewalker maze."""
from random import choice, random, randint

from mazes.primitives import Grid, Cell


def sidewalker(grid: Grid) -> None:
    """Implement a side walker algorithm."""
    # since we are moving from the north west point instead
    # of the south west point, this changes how we walk.
    max_row, max_col = grid.inner.shape

    def at_eastern_boundary(cell: Cell):
        return cell.position[1] + 1 == max_col

    def at_southern_boundary(cell: Cell):
        return cell.position[0] + 1 == max_row

    def should_we_close_out_this_run(cell: Cell) -> bool:
        """Determine if the run should be closed out.

        A run is closed out if we are at the eastern boundary
        or 50% of the time.
        """
        coin_flip = randint(0, 1)
        return at_eastern_boundary(cell) or (
            not at_southern_boundary(cell) and coin_flip == 0
        )

    for row in grid.each_row():
        run = []

        for cell in row:
            run.append(cell)

            # figure out if we're done our run
            # if we are at the eastern boundary
            # or if we feel like it
            if should_we_close_out_this_run(cell):
                # pick a random cell from our current run
                # and make a southern hole in it
                chosen_exit = choice(run)

                south = (chosen_exit.position[0] + 1, chosen_exit.position[1])

                if not at_southern_boundary(cell):
                    chosen_exit.south = grid[south]

                # then clear the run
                run = []
            else:
                # we punch a whole east from this current cell
                east = (cell.position[0], cell.position[1] + 1)
                cell.east = grid[east]
