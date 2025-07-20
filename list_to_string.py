# list to string
list_of_words = ["my", "name", "is", "faza"]
result = ' '.join(list_of_words)

print(result)

# string to list
sentence = "my name is faza"
result = sentence.split()
print(result)

sentence = "my,name,is,faza"
result = sentence.split(',')
print(result)