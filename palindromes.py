#!python

import string
# Hint: Use these string constants to ignore capitalization and/or punctuation
# string.ascii_lowercase is 'abcdefghijklmnopqrstuvwxyz'
# string.ascii_uppercase is 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
# string.ascii_letters is ascii_lowercase + ascii_uppercase


def is_palindrome(text):
  """A string of characters is a palindrome if it reads the same forwards and
  backwards, ignoring punctuation, whitespace, and letter casing."""
  # implement is_palindrome_iterative and is_palindrome_recursive below, then
  # change this to call your implementation to verify it passes all tests
  assert isinstance(text, str), 'input is not a string: {}'.format(text)
  return is_palindrome_iterative(text)
  # return is_palindrome_recursive(text)

def clean (text):
  clean_text = ''
  for letter in text:
    if letter.isalpha():
      clean_text += letter.lower()
  return clean_text


def is_palindrome_iterative(text):
  clean_pal = clean(text)
  rev_pal = clean_pal[::-1]

  clean_text = ''.join(clean_pal)
  rev = ''.join(rev_pal)

  if clean_text == rev:
    return True 
  else:
    return False

def is_palindrome_recursive(text, left=None, right=None):
  text = clean(text)
  print('Text', text)

  if left is None and right is None: 
    left = 0
    right = len(text) - 1

  while left < right: 
    if text[left] == text[right]:
      print('Letters matched')
      left += 1
      right -= 1 
      return is_palindrome_recursive(text, left, right)
    else:
      return False
  return True 


def main():
  import sys
  args = sys.argv[1:]  # Ignore script file name
  if len(args) > 0:
      for arg in args:
          is_pal = is_palindrome(arg)
          result = 'PASS' if is_pal else 'FAIL'
          is_str = 'is' if is_pal else 'is not'
          print('{}: {} {} a palindrome'.format(result, repr(arg), is_str))
  else:
      print('Usage: {} string1 string2 ... stringN'.format(sys.argv[0]))
      print('  checks if each argument given is a palindrome')


if __name__ == '__main__':
  main()