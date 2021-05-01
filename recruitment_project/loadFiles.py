from resume_parser import resumeparse
from pyresparser import ResumeParser
import os
import spacy
spacy.load('en_core_web_sm')

dir_list = os.listdir(r'C:\Users\prasa\projects\recruitment_project\resumes')
#print(dir_list)

res_list = []
paths = r'C:\Users\prasa\projects\recruitment_project\resumes'
c = 0
for i in dir_list:
    c = c + 1
    if c == 2000:
        break
    pfinal = os.path.join(paths, i)
    data = ResumeParser(pfinal).get_extracted_data()
    res_list.append(data)
print(len(res_list))
