def reverse_string(word):
  reverse=""
  for i in range(len(word)-1, -1, -1):
    reverse += word[i]
  return reverse
print(reverse_string("Ammar elmoghazy"))
print(reverse_string("Hello world!"))
print(reverse_string(""))
