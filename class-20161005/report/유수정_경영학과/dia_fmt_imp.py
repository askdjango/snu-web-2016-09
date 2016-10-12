size = 5
longgest_size = size * 2 - 1
format_center = '{:^' +str(longgest_size)+ '}'
#str 이라고 해주어야 문자열의 합으로 인식하므로 꼭 str() 필요하다!
for i in range(1, size+1):
    star_count = i * 2 - 1
    print(format_center.format('*' * star_count))

for i in range(size-1, 0, -1):
    star_count = i * 2 - 1
    print(format_center.format('*' * star_count))