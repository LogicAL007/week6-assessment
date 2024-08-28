''' function that concatenate words'''
def sentence(**scatter):
    words = ''
    for word in scatter.values():
        words += word
    return words

#program test
result = sentence(a='we ', b='are ', c='one ')
print(result)
