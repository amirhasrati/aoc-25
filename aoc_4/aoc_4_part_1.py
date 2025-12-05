from typing import List

def main():
  # Get input grid
  file_name: str = "input.txt"
  file = open(file_name, "r")
  grid: List[str] = file.read().splitlines()
  file.close()
  
  result: int = get_num_accessible(grid)
  print(result)

def get_num_accessible(grid: List[str]) -> int:
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
      
      col_pos += 1
    
    row_pos += 1

  return num_accessible

if __name__ == "__main__":
  main()