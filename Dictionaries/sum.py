def sum_values(my_dictionary):
  sum = 0 
  for i in my_dictionary.values():
    sum +=i
  return sum

# Uncomment these function calls to test your sum_values function:
print(sum_values({"milk":5, "eggs":2, "flour": 3}))
print(sum_values({10:1, 100:2, 1000:3}))
