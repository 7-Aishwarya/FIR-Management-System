import re
import sys
from tkinter import Tk, messagebox

def hash_function(case_date):
    hash_value = 0
    for char in case_date:
        hash_value += ord(char)
    return hash_value % 10

def index_text_file(txt_filename, idx_filename, delimiter_chars=",.;:!?"):
    txt_fil = open(txt_filename, "r")
    word_occurrences = {}
    line_num = 0

    for lin in txt_fil:
        line_num += 1
        words = re.findall('F...', lin)
        words2 = [word.strip(delimiter_chars) for word in words]
        for word in words2:
            if word in word_occurrences:
                word_occurrences[word].append(line_num)
            else:
                word_occurrences[word] = [line_num]

    if line_num < 1:
        print("No lines found in the text file. No index file created.")
        txt_fil.close()
        sys.exit(0)

    word_keys = list(word_occurrences.keys())
    word_keys.sort()

    idx_fil = open(idx_filename, "w")
    for word in word_keys:
        line_nums = word_occurrences[word]
        idx_fil.write(word + " ")
        for line_num in line_nums:
            idx_fil.write(str(line_num) + " ")
        idx_fil.write("\n")

    txt_fil.close()
    idx_fil.close()

def delete_records(txt_file, idx_file, bucket_file, fir_numbers):
    flag = 0
    idx_f = open(idx_file, "r")
    for line in idx_f:
        words = line.split()
        if words[0] in fir_numbers:
            flag = 1
            line_nums = words[1:]
            txt_f = open(txt_file, "r")
            for line_num in line_nums:
                c = int(line_num)
                l2 = record[c - 1].split('|')
                print("\nFIR number: " + l2[0])
                print("Victim name: " + l2[1])
                print("Accused name: " + l2[2])
                print("Case place: " + l2[3])
                print("Case time: " + l2[4])
                print("Case description: " + l2[5])
                print("Case status: " + l2[6] + "\n")
            txt_f.close()

            l2 = [int(num) for num in line_nums]
            record2 = [rec for i, rec in enumerate(record, 1) if i not in l2]

            file1 = open(txt_file, "w")
            file1.writelines(record2)
            file1.close()
            index_text_file(txt_file, idx_file)

            bucket_f = open(bucket_file, "r")
            bucket_records = bucket_f.readlines()
            bucket_f.close()

            for fir_number in fir_numbers:
                for i in range(len(bucket_records)):
                    if re.search(fir_number + r'\|\S+', bucket_records[i]):
                        bucket_records[i] = re.sub(fir_number + r'\|\S+', "####", bucket_records[i])

            bucket_f = open(bucket_file, "w")
            bucket_f.writelines(bucket_records)
            bucket_f.close()

    if flag == 0:
        print("No such record exists")
    idx_f.close()

# Hide the root window
root = Tk()
root.withdraw()

# Check if user confirms deletion before proceeding
result = messagebox.askquestion("Confirmation", "Are you sure you want to delete the record?")
if result == "yes":
    record = open("victim.txt").readlines()
    delete_records("victim.txt", "index_file.idx", "bucket_file.bucket", [sys.argv[1]])
