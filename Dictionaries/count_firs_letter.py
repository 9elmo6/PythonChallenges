def count_first_letter(names):
  count = {}
  for key in names.keys():
    if key[0] not in count:
      count[key[0]] = 0
    count[key[0]] += len(names[key])


  return count

print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Lannister": ["Jaime", "Cersei", "Tywin"]}))
print(count_first_letter({"Stark": ["Ned", "Robb", "Sansa"], "Snow" : ["Jon"], "Sannister": ["Jaime", "Cersei", "Tywin"]}))
