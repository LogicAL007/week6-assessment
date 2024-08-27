def concatenate(**kwargs):
    sentence = ''.join(kwargs.values())
    return sentence

func = concatenate(a="Data Epic ", b="has ", c="cool", d="Mentors", e="!")
print(func) 
