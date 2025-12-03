from aoc_2_part_2 import get_invalids

def test_small_range():
  start = 11
  end = 22

  invalids = get_invalids(start, end)
  assert invalids == [11, 22]

def test_small_range_diff_digits():
  start = 95
  end = 115

  invalids = get_invalids(start, end)
  assert invalids == [99, 111]

def test_med_range_diff_digits():
  start = 998
  end = 1012

  invalids = get_invalids(start, end)
  assert invalids == [999, 1010]

def test_no_invalids_same_range():
  start = 1188511880
  end = 1188511890

  invalids = get_invalids(start, end)
  assert invalids == [1188511885]

def test_big_numbers_short_range():
  start = 222220
  end = 222224

  invalids = [222222]
