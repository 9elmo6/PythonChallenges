# Write your check_for_name function here:
def check_for_name(sentence,name):
  if name.lower() in sentence.lower():
    return True
  else:
    return False
# Uncomment these function calls to test your  function:
print(check_for_name("My name is elmo", "Jamie"))
print(check_for_name("My name is elmo", "elmo"))
print(check_for_name("My name is Elmo", "elmo"))
