import docx2txt
import PyPDF2
import pyresparser
import smtplib
import os
import spacy
spacy.load('en_core_web_sm')
from resume_parser import resumeparse
from pyresparser import ResumeParser
import pandas as pd
from sklearn import datasets

data = ResumeParser('C:\\Users\\prasa\\projects\\recruitment_project\\resumes\\pd.docx').get_extracted_data()

res = {key: data[key] for key in data.keys() & {'name','email', 'mobile_number'}}
print("Name: " + str(res['name']) + "\n" + "Email: " + str(res['email']) + "\n" + "Mobile Number: " + str(res['mobile_number']) + '\n')

# # Load resume in word #
resume = docx2txt.process("C:\\Users\\prasa\\projects\\recruitment_project\\resumes\\pd.docx")
# #print(resume)

# # Load resume in pdf #
# #resume = PyPDF2.PdfFileReader("C:\\Users\\prasa\\projects\\recruitment_project\\resumes\\pd.pdf")

# # load job description # 
#### JD1 ####
job_desc = docx2txt.process("C:\\Users\\prasa\\projects\\recruitment_project\\JD\\ODA_JD.docx")
# #print(job_desc)

# list of text to store resume and JD
text = [resume,job_desc]

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
count_matrix = cv.fit_transform(text)

from sklearn.metrics.pairwise import cosine_similarity
#print(cosine_similarity(count_matrix))
  
match = cosine_similarity(count_matrix)[0][1]
match = match*100
match = round(match, 2)
print("Your resume matches around " + str(match)+ "% of the given Python job description.")
print()

#### JD2 ####

job_desc1 = docx2txt.process("C:\\Users\\prasa\\projects\\recruitment_project\\JD\\ODA_JD1.docx")
# #print(job_desc)

# list of text to store resume and JD
text1 = [resume,job_desc1]

from sklearn.feature_extraction.text import CountVectorizer
cv = CountVectorizer()
count_matrix = cv.fit_transform(text1)

from sklearn.metrics.pairwise import cosine_similarity
#print(cosine_similarity(count_matrix))
  
match1 = cosine_similarity(count_matrix)[0][1]
match1 = match1*100
match1 = round(match1, 2)
print("Your resume matches around " + str(match1)+ "% of the given Java job description.")
print()


name1 = res['name']        #input("Enter Your Name: ")      
email1 = res['email']
link = "https://docs.google.com/forms/d/e/1FAIpQLSdrgyGTnTJ56VUEKiwFl1gm05r2AEpyiaEfTlBy7MkU4cqPUw/viewform?usp=sf_link"

if(match > 40):
    print("Application Accepted for the next round !!!")
    print("Be ready for the test !!!!")
    print("\n")

    ## Send Email ##
    sender_email = "odatestrecruitment@gmail.com"
    rec_email = email1
    password = "oda@1234"
    msg = "Dear " + str(name1) + "," + "\nWarm greetings from our team !!!" + "\nYour application for the position of Python developer is accepted for the next round !!!\nWe are planning to move forward with your application. \nIn order to do so please fill out the questionnaire below " + "\n"+link
    subject = "HR::Recruitment Process for the position of Python developer"

    #In regards to your application, We are pleased to inform you that your resume matches

    message = f'Subject: {subject}\n\n{msg}'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    print("Login Successful")

    server.sendmail(sender_email,rec_email,message)
    print("Email sent !!!")

elif(match1 > 50):
    print("Application Accepted for the next round !!!")
    print("Be ready for the test !!!!")
    print("\n")

    ## Send Email ##
    sender_email1 = "odatestrecruitment@gmail.com"
    rec_email1 = email1
    password1 = "oda@1234"
    msg = "Dear " + str(name1) + "," + "\nWarm greetings from our team !!!" + "\nYour application for the position of Java developer is accepted for the next round.\nWe are planning to move forward with your application. \nIn order to do so please fill out the questionnaire below " + "\n"+link
    subject = "HR::Recruitment Process for the position of Java developer"

    #In regards to your application, We are pleased to inform you that your resume matches

    message = f'Subject: {subject}\n\n{msg}'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email1, password1)
    print("Login Successful")

    server.sendmail(sender_email1,rec_email1,message)
    print("Email sent !!!")


else:
    print("Application Rejected we are sorry !!! \nAs resume match is less than the expected one.\nBetter luck next time")

    ## Send Email ##
    sender_email = "odatestrecruitment@gmail.com"
    rec_email = email1
    password = "oda@1234"
    msg = "Dear "+ name1 + "," + "\nApplication Rejected we are sorry !!!"
    subject = "HR:Recruitment Process"

    message = f'Subject: {subject}\n\n{msg}'

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    #print("Login Successful")

    server.sendmail(sender_email,rec_email,message)
    print("Email sent !!!")





