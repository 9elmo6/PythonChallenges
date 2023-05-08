# Write your every_other_letter function here:
def every_other_letter(word):
  letters = ""
  for l in range(0, len(word), 2):
    letters += word[l]

  return letters 

# Uncomment these function calls to test your function:
print(every_other_letter("Ammar Elmoghazy"))
# should print Cdcdm
print(every_other_letter("Hello world!"))
# should print Hlowrd
print(every_other_letter(""))
# should print 