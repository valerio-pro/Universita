import os

'''
Specifica il path di una directory e visualizza tutti i file e il loro livello nell'albero radicato nella 
directory specificata.
'''


def dir_tree(root, level = 0):

    for x in os.listdir(root):
        file_path = os.path.join(root, x)
        if os.path.isfile(file_path):
            print('The file ' + x + ' is at level:', level, 'of the input directory')
        elif os.path.isdir(file_path):
            dir_tree(file_path, level+1)

if __name__ == '__main__':
    dir = input('Insert the path name of a directory: ')
    dir_tree(dir)