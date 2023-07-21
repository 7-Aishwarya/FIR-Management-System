import sys
import re
import os
from tkinter import Tk, messagebox

# Hide the root window
root = Tk()
root.withdraw()

# Hash function to generate an address from the case_date
def hash_function(case_date):
    hash_value = 0
    for char in case_date:
        hash_value += ord(char)
    return hash_value % 10

def calculate_address(case_date):
    address = hash_function(case_date)
    return address

def create_bucket_file():
    bucket_filename = "bucket_file.bucket"

    if os.path.exists(bucket_filename):
        return

    with open(bucket_filename, "w") as bucket_file:
        for i in range(10):
            bucket_file.write("Bucket {}: //// //// //// //// ////\n".format(i))


def get_bucket_address(case_date):
    address = calculate_address(case_date)
    return address

def add_to_bucket(address, fir_number, case_date):
    bucket_filename = "bucket_file.bucket"
    with open(bucket_filename, "r") as bucket_file:
        lines = bucket_file.readlines()

    row_index = address
    empty_slot_index = lines[row_index].find("////")
    deleted_slot_index = lines[row_index].find("####")

    if empty_slot_index == -1 and deleted_slot_index == -1:
        print("Bucket overflow")
        messagebox.showerror("Bucket Overflow", "The bucket has overflowed.")
        return False

    if empty_slot_index != -1:
        line = lines[row_index]
        updated_line = line.replace("////", "{}|{}".format(fir_number, case_date), 1)
        lines[row_index] = updated_line
    elif deleted_slot_index != -1:
        line = lines[row_index]
        updated_line = line.replace("####", "{}|{}".format(fir_number, case_date), 1)
        lines[row_index] = updated_line

    with open(bucket_filename, "w") as bucket_file:
        bucket_file.writelines(lines)

    return True

def index_text_file(txt_filename, idx_filename, delimiter_chars=",.;:!?"):
    txt_fil = open(txt_filename, "r")

    word_occurrences = dict()
    line_num = 0

    for lin in txt_fil:
        line_num += 1
        words = re.findall('^F...', lin)
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

# Main code
txt_filename = "victim.txt"
txt_fil = open(txt_filename, "a")
txt_indexname = "index_file.idx"
n = len(sys.argv)
FIR_no = sys.argv[1]
vic_name = sys.argv[2]
acc_name = sys.argv[3]
case_date = sys.argv[4]
case_time = sys.argv[5]
case_stat = sys.argv[6]

case_desc1 = ""
for i in range(7, n):
    case_desc1 = case_desc1 + sys.argv[i] + " "

entry = FIR_no + ' ' + '|' + vic_name + '|' + acc_name + '|' + case_date + '|' + case_time + '|' + case_desc1 + '|' + case_stat + '|' + '\n'

# Validate case time
if not re.match(r'^\d{2}:\d{2}$', case_time):
    messagebox.showerror("Invalid Case Time", "The case time is invalid. Please provide a time in HH:MM format.")
    sys.exit(1)
with open(txt_filename, "r") as txt_file:
    for line in txt_file:
        if FIR_no in line:
            messagebox.showerror("Duplicate FIR Number", "The provided FIR number is already registered. Please provide a unique FIR number.")
            sys.exit(1)

create_bucket_file()
address = get_bucket_address(case_date)
added_to_bucket = add_to_bucket(address, FIR_no, case_date)

if added_to_bucket:
    txt_fil.write(entry)
    messagebox.showinfo("Record Inserted", "The record has been successfully inserted!")

txt_fil.close()

index_text_file(txt_filename, txt_indexname)
