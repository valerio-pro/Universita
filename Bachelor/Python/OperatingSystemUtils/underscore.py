import os

'''
Specifica un path di un file (completo di estensione) o di una directory e rinomina il file stesso o tutti i file, 
ricorsivamente, contenuti nella directory specificata, aggiungendo caratteri '_' in caso di spazi vuoti nel nome
dei file.
'''


def rename(root):

    for x in os.listdir(root):
        if ' ' in x:
            file_path = os.path.join(root, x)

            if os.path.isdir(file_path):      # andare prima sulle foglie dell'albero delle directory
                rename(file_path)

            rename_file(file_path)

def rename_file(root):

    new_name = root.replace(os.path.basename(root), '')
    count = 0     # count serve per non usare piu' di un '_' quando ci sono piu' spazi bianchi consecutivi nel nome
    x = os.path.basename(root)

    for i in x:
        if i == ' ' and count == 0:
            new_name += '_'
            count = 1
        elif i != ' ':
            new_name += i
            count = 0

    os.rename(root, new_name)



if __name__ == '__main__':
    path_name = input('Insert the path name (or path tree) you want to rename with underscores: ')
    if os.path.isdir(path_name):
        rename(path_name)
    elif os.path.isfile(path_name):
        rename_file(path_name)





'''                     # RAW VERSION
def rename(root):

    for x in os.listdir(root):
        if ' ' in x:
            file_path = os.path.join(root, x)

            if os.path.isdir(file_path):      # andare prima sulle foglie dell'albero delle directory
                rename(file_path)

            new_name = '' + file_path.replace(os.path.basename(file_path), '')   # astrazione per tutti i SO, non usare + '\\' 
            count = 0   # count serve per non usare piu' di un '_' quando ci sono piu' spazi bianchi consecutivi nel nome

            for i in x:
                if i == ' ' and count == 0:
                    new_name += '_'
                    count = 1
                elif i != ' ':
                    new_name += i
                    count = 0

            os.rename(file_path, new_name)
'''
