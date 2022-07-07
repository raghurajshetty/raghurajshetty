from merge import Solution_heapq as sh

def test_result():
  obj = sh()
  assert obj.srm_heapq([1, 3], [2, 4]) == 1.5
