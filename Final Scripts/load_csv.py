#codigo,GT,Autores,Instituciones
# with open('list.csv') as csv_file:
    # csv_reader = csv.reader(csv_file, delimiter=';')
    # line_count = 0
    # for row in csv_reader:
        # if line_count == 0:
            # print(f'Column names are {", ".join(row)}')
            # line_count += 1
        # else:
            # print(f'\t{row[0]} doc was made in the GT : {row[1]} , and was made by {row[2]}. The institution he/she/them works for is {row[3]}')
            # line_count += 1
    # print(f'Processed {line_count} lines.')
import csv	
array=[]
fnames=[]	
# Load all the txt files in the directory and save their filenames in another array
import glob
for file in glob.glob("*.txt"): 
    print(file)
    with open(file, 'rt', encoding='utf-8') as a:
         array = array + [a.read()] 
         fnames = fnames + [a.name]
		 
		 
		 
		 
docnum=fnames[1][2:6]
mail=[]   
with open('list.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        if row[0][0:4] == docnum:
            print(f'\t{row[0]} doc was made in the GT : {row[1]} , and was made by {row[2]}. The institution he/she/them works for is {row[3]}')
            # mail.append({row[3]})
            break
        else:
            line_count += 1
    print(f'Processed {line_count} lines.')    