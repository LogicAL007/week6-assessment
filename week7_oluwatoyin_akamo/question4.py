# Write a python function to concatenate a few words using kwargs,
# the function should look like this concatenate(a="Data Epic ", b="has ",
# c="cool", d="Mentors", e="!")

def concatenate(**kwargs):
    result = ""
    for arg in kwargs.values():
        result += arg
    return result


print(concatenate(a="Data Epic ", b="has ", c="cool ", d="Mentors", e="!"))