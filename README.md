# FIR Management System using File Structures(Hashing Collison Resolution Using Bucketing)

Tech Stack - Python

A FIR Portal based on File Strutures Concepts:
- Collision Resolutions Using Bucketing.
- Variable Length Records
- Hash Key = Case Place

Key Functionalities:
- Login and Signup
- Registering FIR
- Searching for FIR
- Deleting FIR
- Displaying Contents Of Buckets


Insertion Of A Record:
- In this project ,hash address is generated for case place based on the addrees generated case place along with its fir no(firno|caseplace) occupy its home address in bucket file.
Bucket file is made up of 0 to 9 address spaces i.e 10 buckets. Each buckets can hold upto 5 records that is they are made up of 5 slots.When all slots get filled in corresponding bucket it leads in Bucket Overflow  due to collission and corresponding recording will not be inserted into that slot.


Deletion Of A Record:(Tombstones for handling deletion(####)):
- Whenever record is deleted its entry in bucketfile will also get deleted and it is replaced with #### indicating record is deleted a new record can be inserted into that slot.

Note: The format of FIR ID while registering should be 'F' followed by 3 digits. Ex: F123

<br><br>

How to RUN the project:
1. Install necessary library - Tkinter
2. RUN ```python InitMain.py```

<br><br>
Screenshots
<br>

<img src="https://user-images.githubusercontent.com/89032469/183235077-5ef87fb8-fa61-416d-821a-9c5ccd452cec.png" >       
<img src="https://user-images.githubusercontent.com/89032469/183235219-cd5b90ac-a42a-4fa1-8746-931ca1a0d0e3.jpg" >        
 <img src="https://user-images.githubusercontent.com/89032469/183235237-d8f93e04-7865-4668-9b0c-19003f8c213c.png" >
<img src = "https://github.com/7-Aishwarya/CNS-Lab-Programs-VTU-5th-Sem-/assets/98330491/cdbc29ef-7286-4d14-bd88-6487d3f78a3c"  >
