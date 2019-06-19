#!python

def contains(text, pattern):
  """Return a boolean indicating whether pattern occurs in text."""
  assert isinstance(text, str), 'text is not a string: {}'.format(text)
  assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

  index = find_index(text, pattern)
  if index is not None:
    return True 
  else: 
    return False 

def find_index(text, pattern, starting_index = 0):
  """Return the starting index of the first occurrence of pattern in text,
  or None if not found."""
  assert isinstance(text, str), 'text is not a string: {}'.format(text)
  assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

  if pattern == '':
    return 0  

  match = 0
  p_index = 0
  starting = None

  for t_index in range(starting_index, len(text)):
    print('P Index: ', p_index, '& T Index: ', t_index)
    while t_index < len(text) and pattern[p_index] == text[t_index]:  # matched one letter
      match += 1 
      p_index += 1
      t_index += 1
      if match == len(pattern): # matched last letter of pattern
        starting = t_index - p_index 
        return starting 
    starting_index = t_index 
    p_index = 0 
    match = 0
  print('DONE')
  return None

def find_all_indexes(text, pattern):
  """Return a list of starting indexes of all occurrences of pattern in text,
  or an empty list if not found."""
  assert isinstance(text, str), 'text is not a string: {}'.format(text)
  assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

  count = 0
  starting_index = 0
  indexes = []

  if pattern == '':
    while count <= len(text) - 1:
      indexes.append(count)
      count += 1
    return indexes

  while count <= len(text) - 1:
    index = find_index(text, pattern, starting_index)
    if index is None:  # pattern not found 
      return indexes
    if index is not None:
      indexes.append(index)
      starting_index = index + 1
    count += 1 
  return indexes

def test_string_algorithms(text, pattern):
  found = contains(text, pattern)
  # print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
  # TODO: Uncomment these lines after you implement find_index
  index = find_index(text, pattern)
  # print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
  # TODO: Uncomment these lines after you implement find_all_indexes
  indexes = find_all_indexes(text, pattern)
  print('find_all_indexes({!r}, {!r}) => {}'.format(text, pattern, indexes))


def main():
  """Read command-line arguments and test string searching algorithms."""
  import sys
  args = sys.argv[1:]  # Ignore script file name
  if len(args) == 2:
    text = args[0]
    pattern = args[1]
    test_string_algorithms(text, pattern)
  else:
    script = sys.argv[0]
    print('Usage: {} text pattern'.format(script))
    print('Searches for occurrences of pattern in text')
    print("\nExample: {} 'abra cadabra' 'abra'".format(script))
    print("contains('abra cadabra', 'abra') => True")
    print("find_index('abra cadabra', 'abra') => 0")
    print("find_all_indexes('abra cadabra', 'abra') => [0, 8]")


if __name__ == '__main__':
  main()