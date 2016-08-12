import ctypes

def crash():
  """Cause Python to segfault."""
  i = ctypes.c_char('a')
  j = ctypes.pointer(i)
  c = 0
  while True:
    j[c] = 'a'
    c += 1
  j

crash()
