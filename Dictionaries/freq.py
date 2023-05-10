
def frequency_dictionary(words):
  freq={}
  for word in words:
    if word not in freq:
      freq[word] = 0
    freq [word]+= 1
  return freq
# Uncomment these function calls to test your  function:
print(frequency_dictionary(["elmo", "elmo", "cat", 1]))
print(frequency_dictionary([0,0,0,0,0]))
