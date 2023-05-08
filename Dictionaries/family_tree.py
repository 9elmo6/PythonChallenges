def values_that_are_keys(my_dictionary):
  list = []
  for value in my_dictionary.values():
    if value in my_dictionary.keys():
      list.append(value)
  return list

print(values_that_are_keys({1:100, 2:1, 3:4, 4:10}))
print(values_that_are_keys({"a":"apple", "b":"a", "c":100}))
