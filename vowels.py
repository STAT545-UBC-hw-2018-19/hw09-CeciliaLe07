import csv
def vowelcounter(vowel,listName):
    count =0
    for i in range(0, len(listName)):
        if listName[i] in vowel:
            count += 1
    return count

file = open('words.txt', mode = 'r', encoding = 'utf-8-sig')
lines = file.readlines()
file.close()

output = []
for line in lines:
    output.append(line.upper()[0])
    
total = ["count",
         vowelcounter("A",output),
         vowelcounter("E",output),
         vowelcounter("I",output),
         vowelcounter("O",output),
         vowelcounter("U",output)]

with open('vowels_count.tsv', 'w', newline='') as f_output:
    tsv_output = csv.writer(f_output, delimiter='\n')
    tsv_output.writerow(total)