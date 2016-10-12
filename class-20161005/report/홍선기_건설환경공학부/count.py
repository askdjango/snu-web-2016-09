message = '노랑 빨강 녹색 파랑 노랑 빨강 노랑 빨강'
message_list = message.split()
message_set_list = list(set(message_list))
for i in range(0,len(message_set_list)):
        print (message_set_list[i],":",message.count(message_set_list[i]))