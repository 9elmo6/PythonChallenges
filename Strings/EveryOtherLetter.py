# Write your every_other_letter function here:
def every_other_letter(word):
  letters = ""
  for l in range(0, len(word), 2):
    letters += word[l]

  return letters 

# Uncomment these function calls to test your function:
print(every_other_letter("Ammar Elmoghazy"))
print(every_other_letter("Hello world!"))
print(every_other_letter(""))
