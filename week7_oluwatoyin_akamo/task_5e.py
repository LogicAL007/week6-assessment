'''function implementation of Args'''
def lst(*poll):
    print("this set of people are invited:")
    for name in poll:
        print("\t" + name.title())

lst('grace', 'joy', 'peace')
