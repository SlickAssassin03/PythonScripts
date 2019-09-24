def obj(liststyle=0, *args):  # Does not take lists yet.
    style = ['. ', ' >> ', ' ··> ', ' : ', ' > ']
    if (liststyle>4):
        liststyle = 0
    while True:
        if (args[0]==None): break
        objlist = ['']
        for obj in args:
            if isinstance(obj, list) or isinstance(obj, tuple):
                print('Lists and tuples not supported.')
                break
            if (obj==None): break
            else: objlist.append(obj)
        objlist.pop(0)
        for obj in objlist:
            num = objlist.index(obj) + 1
            print('{}{}{}'.format(num, style[liststyle], obj))
        break

b = ['You cannot pass lists yet, it will ignore them.']
a = 'You can pass variables in obviously.'
obj(0, 'Line one is kind of cool!', 'Line two is less cool', a, b)  # You can pass as many args as you like, it will ignore lists/tuples.
