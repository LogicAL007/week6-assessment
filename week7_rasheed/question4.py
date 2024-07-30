def concatenate(**kwargs):
    result = ""
    for key, value in kwargs.items():
        result += value
    return result

result = concatenate(a="Data Epic ", b="has ", c="cool ", d="Mentors", e="!")
print(result)
