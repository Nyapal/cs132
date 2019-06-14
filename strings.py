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

def find_index(text, pattern):
  """Return the starting index of the first occurrence of pattern in text,
  or None if not found."""
  assert isinstance(text, str), 'text is not a string: {}'.format(text)
  assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

  if pattern == '':
    return 0  

  index = 0
  starting = None

  for i, char in enumerate(text):
    print('Index', i, 'Char', i)
    while pattern[index] == text[i]: 
      print('Pattern[I]', pattern[index], 'Text[I]', text[i])
      if starting is None:
        starting = i
      if len(pattern) - 1 == index:
        return starting
      index += 1
      i += 1
    index = 0
  return None


def find_all_indexes(text, pattern):
  """Return a list of starting indexes of all occurrences of pattern in text,
  or an empty list if not found."""
  assert isinstance(text, str), 'text is not a string: {}'.format(text)
  assert isinstance(pattern, str), 'pattern is not a string: {}'.format(text)

  # index = find_index(text, pattern)
  # pattern_indexes = []

  # if(len(pattern) == 0):
  #   return list(range(0, len(text)))

  # while index is not None:
  #   offset = index + 1
  #   pattern_indexes.append(index)
  #   index = find_index(text, pattern, offset)
  # return pattern_indexes

def test_string_algorithms(text, pattern):
  found = contains(text, pattern)
  print('contains({!r}, {!r}) => {}'.format(text, pattern, found))
  # TODO: Uncomment these lines after you implement find_index
  index = find_index(text, pattern)
  print('find_index({!r}, {!r}) => {}'.format(text, pattern, index))
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
  hello = find_index('abc', 'ac')
  print(hello)