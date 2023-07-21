from tkinter import *
import sys,re

def display_bucket_file(bucket_filename):
    with open(bucket_filename, "r") as bucket_file:
        contents = bucket_file.read()
    print("Bucket File Contents:")
    print(contents)

bucket_filename = "bucket_file.bucket"
display_bucket_file(bucket_filename)


