# Write your add_exclamation function here:
def add_exclamation(word):
  if len(word) < 20:
    for i in range(20-len(word)):
      word +="!"

  return word
print(add_exclamation("elmo"))
print(add_exclamation("Learn with me"))
