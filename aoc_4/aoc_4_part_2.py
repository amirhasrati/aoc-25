from typing import List
import time

def main():
  # Get input grid
  file_name: str = "input.txt"
  file = open(file_name, "r")
  grid: List[str] = file.read().splitlines()
  file.close()
  
  num_removed: int = 0
  num_accessible: int

  while True:
    num_accessible = get_num_accessible(grid)

    if(num_accessible > 0):
      num_removed += num_accessible
    
    else:
      break

  print(num_removed)

def get_num_accessible(grid: List[str]) -> int:
  deletion_indices: List[tuple[int, int]] = []
  num_rows: int = len(grid)
  num_cols: int = len(grid[0])
  row_pos: int = 0
  col_pos: int = 0
  
  num_accessible: int = 0
  # brute force
  for row in grid:
    col_pos = 0
    for col in row:
      adjacent_rolls = 0
      if col == ".": 
        col_pos += 1
        continue
      
      # find the number of adjacent rolls (@)
      if row_pos != 0 and grid[row_pos - 1][col_pos] == "@":
        adjacent_rolls += 1
      
      if row_pos != num_rows - 1 and grid[row_pos + 1][col_pos] == "@":
        adjacent_rolls += 1

      if col_pos != 0 and grid[row_pos][col_pos - 1] == "@":
        adjacent_rolls += 1

      if col_pos != num_cols - 1 and grid[row_pos][col_pos + 1] == "@":
        adjacent_rolls += 1

      if row_pos != 0 and col_pos != 0 and grid[row_pos - 1][col_pos - 1] == "@":
        adjacent_rolls += 1

      if row_pos != 0 and col_pos != num_cols - 1 and grid[row_pos - 1][col_pos + 1] == "@":
        adjacent_rolls += 1
      
      if row_pos != num_rows - 1 and col_pos != 0 and grid[row_pos + 1][col_pos - 1] == "@":
        adjacent_rolls += 1
      
      if row_pos != num_rows - 1 and col_pos != num_cols - 1 and grid[row_pos + 1][col_pos + 1] == "@":
        adjacent_rolls += 1
      
      if(adjacent_rolls < 4):
        num_accessible += 1
        deletion_indices.append((row_pos, col_pos))

      col_pos += 1
    
    row_pos += 1
  
  for i in deletion_indices: # Remove accessible rolls
    str_list = list(grid[i[0]])
    str_list[i[1]] = "."
    grid[i[0]] = "".join(str_list)
    

  return num_accessible

if __name__ == "__main__":
  times = []

  for _ in range(50):
    start = time.perf_counter()
    main()
    end = time.perf_counter()
    times.append((end - start) * 1000)  # convert to ms

  print(f"Average time: {sum(times)/len(times):.3f} ms")
  print(f"Fastest: {min(times):.3f} ms")
  print(f"Slowest: {max(times):.3f} ms")