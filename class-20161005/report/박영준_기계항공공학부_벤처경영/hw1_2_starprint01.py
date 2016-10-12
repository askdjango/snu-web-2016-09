starprint = ""

n = 9
m = int((n+1)/2)

for i in range(1,n+1,2):
    m -= 1
    print(' '*m + '*'*i)

for i in range(7,0,-2):
    m += 1
    print(' '*m + '*'*i)


# for i in range(0,9):
#     for j in range(0,abs(4-i)):
#         starprint += " "
#     for j in range(0,8-2*abs(4-i)):
#         starprint += "*"
#     starprint += "*"
#     for j in range(0,abs(4-i)):
#         starprint += " "
#     if i < 8:
#         starprint += "\n"
#     else:
#         break
# print(starprint)