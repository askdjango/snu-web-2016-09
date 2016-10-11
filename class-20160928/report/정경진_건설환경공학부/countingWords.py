message = input("문자열 입력: ")
array = message.split()
dictionary = {x:array.count(x) for x in array}
print(dictionary)