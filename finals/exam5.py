# -*- coding: utf-8 -*-
import csv
from collections import defaultdict
import random

def key_fn(row):
    i1, numbers = row
    return len(numbers)

def main():
    result_dict = defaultdict(list)

    for i in range(1000):
        number = random.randint(1, 100000)
        result_dict[number%10].append(number)

    result_list = sorted(result_dict.items(), key=key_fn, reverse=True)

    with open('exam5.csv', 'wt', encoding='cp949', newline='\n') as f:
        writer = csv.writer(f)
        writer.writerow(['랭크', '1의자릿수', '그룹 내 숫자 갯수',
            '그룹 내 제일큰수', '그룹 내 다음 큰수', '그룹 내 그 다음 큰수'])

        for idx, (i1, numbers) in enumerate(result_list, 1):
            writer.writerow([idx, i1, len(numbers), *numbers[:3]])

if __name__ == '__main__':
    main()

