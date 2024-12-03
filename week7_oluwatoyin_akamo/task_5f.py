'''Kwarg function implementation'''
def form(**user):
    print("this is your info:")
    for k, v in user.items():
        print(k.title() + ": " + v.title())

form(f_name='bamidele', l_name='oluwapelumi', m_name="Adeleke",
      membership="data epic", rank="beginner with no experiece"
      )