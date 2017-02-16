#! usr/bin/python3
#программа для создания backups

import os, zipfile

def backupToZip(folder):
    """
    создает резервную копию всего содержимого папки folder
    """
    folder = os.path.abspath(folder)

    number=1
    while True:
        zipFilename = os.path.basename(folder)+'_'+str(number)+'.zip'
        if not os.path.exists(zipFilename):
            break
        number += 1

    print('Создается файл %s...' % (zipFilename))
    backupZip = zipfile.ZipFile(zipFilename, 'w')

    for foldername, subfolders, filenames in os.walk(folder):
        print('Добавления файла из папки %s...' % (foldername))
        #Добавить в zip-файл текущую папку.
        backupZip.write(foldername)
        #Добавить в Zip-файл все файлы из данной папки
        for filename  in filenames:
            newBase= os.path.basename(folder) + '_'
            if filename.startswith(newBase) and filename.endswith('.zip'):
                continue # не создавать резервной копии
            backupZip.write(os.path.join(foldername, filename))
    backupZip.close()
    print('Все готово!!!')

        
if __name__ == '__main__':
    n = input('Введите путь к папке для создания из нее Zip-архива \n>>>')
    backupToZip(n)
    
