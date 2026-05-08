# Patterns

## Grid chunking / 2D-to-1D indexing
- For cell (i, j) in a grid chunked into k×k boxes: chunk = (i // k, j // k)
- Flatten to single index: (i//k)*(number of columns) + (j//k)
- Seen in: Valid Sudoku
- Drill: tabulate input→output before deriving formula
