import os

os.chdir('Desktop/Programmazione/Programmi Python/Script')

with open('tom_sawyer.txt', 'r') as fp_in:
    list_of_words = fp_in.read().split(' ')
    new_list = list(filter(lambda x: x not in (',', 'Most', 'of', 'the', 'adventures', 'I', '?','!','-',',',':',';','/n'), list_of_words))
    new_string = ' '
    for x in new_list:
        new_string += (str(x) + ' ' )

with open('new_tom_sawyer.txt', 'w') as fp_out:
    fp_out.write(new_string)