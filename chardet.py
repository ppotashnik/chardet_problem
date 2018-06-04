import chardet

with open('newsafr.txt', 'rb') as f:
    b = f.read()
    result = chardet.detect(b)
    print(result)
    # s = data.decode(result['encoding'])
    # print(s)

