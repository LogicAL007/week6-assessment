def concatenate(**kwargs):
    result = ""

    if 'a' in kwargs:
        result += kwargs['a']
    if 'b' in kwargs:
        result += kwargs['b']
    if 'c' in kwargs:
        result += kwargs['c']
    if 'd' in kwargs:
        result += kwargs['d']
    if 'e' in kwargs:
        result += kwargs['e']
    return result

comment = concatenate(a="Data Epic ", b="has ", c="cool ", d="Mentors", e="!")
print(comment)  
