MATRIX_LENGTH=10
import csv

def generate_tile(label,score,end_row=False):
   text = "\\node[tile,label=center:\\Huge "
   if label != 'BLANK':
       text += label
       text += ",label={[xshift=5mm, yshift=-15mm]"
       text += str(score)
       text += '}'
   else:
       text += ' '
   text += "] {}; "
   if end_row:
       return (text + "\\\\")
   else:
       return (text + "&")



letters_dict = {}
length = 0
with open("frequency_chart.csv",'r') as filehandle:
    reader = csv.DictReader(filehandle)
    for row in reader:

        letters_dict[row['IPA']] = { 'frequency' : int(row['How many to make']), 'score' : int(row['Score'])}
        length += int(row['How many to make'])

with open('tilematrix.tex','w') as tilefile:
    idx = 0
    total = 0
    for letter in letters_dict:
        for _ in range(int(letters_dict[letter]['frequency'])):
            idx += 1
            total += 1
            if idx == MATRIX_LENGTH or total == length:
                end_row = True
                idx = 0
            else:
                end_row = False
            tilefile.write(generate_tile(letter,letters_dict[letter]['score'],end_row=end_row) + '\n')
