def add_ten(my_dictionary):
  for i in my_dictionary.keys():
    my_dictionary[i]+=10
  return my_dictionary
# Uncomment these function calls to test your  function:
print(add_ten({1:5, 2:2, 3:3}))
print(add_ten({10:1, 100:2, 1000:3}))
