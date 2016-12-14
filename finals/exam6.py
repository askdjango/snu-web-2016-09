import requests
from hangul import hangul
from collections import defaultdict

JAUM_SET = set(hangul.CHOSUNG_LIST + hangul.JONGSUNG_LIST)


def jaum_count(ch):
    return len([e for e in hangul.split(ch) if e and e in JAUM_SET])


def main(article):
    result_dict = defaultdict(list)

    for word in article.split():
        word_jaum_count = sum(jaum_count(ch) for ch in word)
        result_dict[word_jaum_count].append(word)

    result_list = sorted(result_dict.items(), reverse=True)
    for (count, members) in result_list:
        print(count, members)


if __name__ == '__main__':
    article = requests.get('https://goo.gl/9L7seu').text
    main(article)

