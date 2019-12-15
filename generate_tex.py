import csv

def generate_tile(label,end_row=False):
   text = "\\node[tile,label=center:\\Huge "
   if label != 'BLANK':
       text += label
   text += "] {}; "
   if end_row:
       return (text + "\\\\")
   else:
       return (text + "&")



letters_dict = {}
with open("frequency_chart.csv",'r') as filehandle:
    reader = csv.DictReader(filehandle)
    for row in reader:
        letters_dict[row['IPA']] = { 'frequency' : row['How many to make'], 'score' : row['Score']}

#with open('tilematrix.tex','w') as tilefile:
for letter in letters_dict:
    print(generate_tile(letter))
