#!/usr/bin/python3
def island_perimeter(grid):
  """Calculates the perimeter of an island in a grid.

  Args:
    grid: A list of lists of integers representing land (1) and water (0).

  Returns:
    The perimeter of the island.
  """

  perimeter = 0
  rows = len(grid)
  cols = len(grid[0])

  for i in range(rows):
    for j in range(cols):
      if grid[i][j] == 1:
        # Check neighbors
        if i == 0 or grid[i - 1][j] == 0:
          perimeter += 1
        if j == 0 or grid[i][j - 1] == 0:
          perimeter += 1
        if i == rows - 1 or grid[i + 1][j] == 0:
          perimeter += 1
        if j == cols - 1 or grid[i][j + 1] == 0:
          perimeter += 1

  return perimeter
