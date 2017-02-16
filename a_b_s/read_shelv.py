#программа для чтения содержимого shelve files

import shelve

def fu2(a):
    """
    данная функция открывает shelve file
    для чтения 
    в параметрах необходимо передать имя файла
    """
    with shelve.open(a) as f2:
        print('\t\tвыберите нужный ключ\n',list(f2.keys()))
        k=input('\n')
        print(f2[k])

if __name__=='__main__':
    n = input('введите имя файла для открытия\t')
    fu2(n)

