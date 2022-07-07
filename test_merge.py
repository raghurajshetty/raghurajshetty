from merge import Solution_heapq as sh

def test_result():
  obj = sh()
  assert obj.srm_heapq([1, 3], [2, 0]) == 1.5
