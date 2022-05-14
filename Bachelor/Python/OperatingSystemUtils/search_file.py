import os

'''
Specifica il nome di un file, completo di estensione (es: prova.txt), e il path di una directory per trovare in quale
directory si trova il file e a che profondita' dalla directory di input.
'''


def search_file(filename, root, level = 0):

    for x in os.listdir(root):
        file_path = os.path.join(root, x)  
        if os.path.isfile(file_path) and x == filename:  
            print('File found: ', '\n', '--> in directory: ' + os.path.basename(root), '\n', '--> directory path: ' + root,
            '\n', '--> at level', level, 'from the input directory')
        elif os.path.isdir(file_path):
            search_file(filename, file_path, level+1)


if __name__ == '__main__':
    filename = input('Indica il nome del file, completo di estensione, che stai cercando: ')
    dir = input('Indica il path della directory da cui vuoi cercare il file: ')
    print('\n')
    search_file(filename, dir)