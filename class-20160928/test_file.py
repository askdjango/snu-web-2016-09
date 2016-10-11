
f = open("result.txt", "wt", encoding="utf8")
f.write("단어1")
f.write("단어2")
f.write("단어3")
f.close()

f = open("result.txt", "rt", encoding="utf8")
print(f.read())
f.close()

'''
f = open("result2.txt", "wb")
f.write("단어1".encode("utf8"))
f.write("단어2".encode("utf8"))
f.write("단어3".encode("utf8"))
f.close()
'''

