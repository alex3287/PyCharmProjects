import pyperclip, shelve, sys

mcbShelf = shelve.open('mcb')

#сохранятся содержимое буфера обмена

if len(sys.argv)==3 and sys.argv[1].lower() == 'save':
    mcbShelf[sys.argv[2]] = pyperclip.paste()
    print(sys.argv)
elif len(sys.argv) == 2:
    if sys.argv[1].lower() == 'list':
        pyperclip.copy(str(list(mcbShelf.keys())))
        print(str(list(mcbShelf.keys())))
    elif sys.argv[1] in mcbShelf:
        t=mcbShelf[sys.argv[1]]
        pyperclip.copy(t)
        print(mcbShelf[sys.argv[1]])
mcbShelf.close()
