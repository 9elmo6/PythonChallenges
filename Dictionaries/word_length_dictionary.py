# Write your word_length_dictionary function here:
def word_length_dictionary(words):
  lenghts = {}
  for word in words:
    lenghts[word] = len(word)
  return lenghts
# Uncomment these function calls to test your  function:
print(word_length_dictionary(["elmo", "ammar", "cat"]))
print(word_length_dictionary(["a", ""]))
