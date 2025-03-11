my_sentence = "python is fun and powerful"
print(len(my_sentence))
print(my_sentence[0])
print(my_sentence[10:0])
print(my_sentence.lower())
print(my_sentence.count("o"))
print(my_sentence.find("fun"))
my_sentence.replace("powerful", "amazing")
print(my_sentence)
new_message = "learning python is exciting!"
my_log = my_sentence + new_message
print(my_log)
my_log = "{}, {},".format(my_sentence, new_message)
print(my_log)
print(dir(my_sentence))
help(str.replace)
