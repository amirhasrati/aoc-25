from aoc_4_part_1 import get_num_accessible


def test_corners():
  grid = [
    "@...@",
    ".....",
    ".....",
    "....@"
  ]

  res = get_num_accessible(grid)

  assert res == 3