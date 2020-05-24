# -*- coding: utf-8 -*-
"""csvEditor.py

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1-iCD6Q-rZXDPYHd0iV7jMR68sBjO9X2b
"""

import csv
import re

members_split_regex = re.compile(r'([a-zA-Z0-9 ]+):([a-zA-Z0-9 ]+)\\n\\n([a-zA-Z0-9 ]+)\\n\\n([a-zA-Z0-9 ]+)\\n\\n([a-zA-Z0-9 ]+)\\n\\n([a-zA-Z0-9 ]+)')

# with open('dumped_CVs.csv') as input_file, open('output_csv.csv', 'w', newline='') as output_file:
#     csv_reader = csv.DictReader(input_file)
#     fieldnames = csv_reader.fieldnames.copy()
#     #print(input_file)
    
#     fieldnames.remove('Members')
    
#     csv_writer = csv.DictWriter(output_file, extrasaction='ignore', fieldnames=fieldnames + ['Member_Rank', 'Member_Name', 'Member_Surname', 'Member_ID_Method', 'Member_ID_Num', 'Member_Gender', 'Member_Notes'])
#     #print(csv_writer)
#     csv_writer.writeheader()
#     #print(csv_reader)
#     for row in csv_reader:
#         print(row)
#         for member_tuple in members_split_regex.findall(row['Members']):
#             #print(members_split_regex.findall(row['Members']))
#             member_dict = {}

#             (
#                 member_dict['Member_Rank'],
#                 member_dict['Member_Name'],
#                 member_dict['Member_Surname'],
#                 member_dict['Member_ID_Method'],
#                 member_dict['Member_ID_Num'],
#                 member_dict['Member_Gender'],
#                 member_dict['Member_Notes']
#             ) = member_tuple
#             #print(member_dict)
#             member_dict.update(row)
#             print(row)
#             csv_writer.writerow(member_dict)
#             print(member_dict)

output = []

members_split_regex = re.compile(r'([a-zA-Z0-9 ]+)\\n\\n([a-zA-Z0-9 ]+)\\n\\n([a-zA-Z0-9 ]+)\\n\\n([a-zA-Z0-9 ]+)\\n\\n([a-zA-Z0-9 ]+)\\n\\n([a-zA-Z0-9 ]+)')

"""delimetere used for splitting \\n\\n"""

with open('dumped_CVs.csv') as f:
    csv_reader = csv.DictReader(f)
    for row in csv_reader:
        #print(row)
        members = row['Members']
        split_members = members_split_regex.findall(members)
        #print(split_members)
        for member in split_members:
                (member_name, member_skills, member_experience, 
                 member_languages, member_hobbies, member_notes) = member
                print(split_members)

                output.append({'Member_Name': member_name, 'Member_Skills': member_skills,
                               'Member_Experiences': member_experience, 
                               'Member_Languages': member_languages, 'Member_Hobbies': member_hobbies,
                               'Member_Notes': member_notes})

with open('outputCVs.csv', 'w', newline='') as f:
    csv_writer = csv.DictWriter(f, fieldnames=['Member_Name', 'Member_Skills', 'Member_Experiences','Member_Languages', 'Member_Hobbies', 'Member_Notes'])
    csv_writer.writeheader()
    csv_writer.writerows(output)