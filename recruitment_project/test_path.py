import os

#Function to read resumes from the folder one by one
mypath='C:\\Users\\prasa\\projects\\recruitment_project\\resumes' #enter your path here where you saved the resumes
onlyfiles = [os.path.join(mypath, f) for f in os.listdir(mypath) if os.path.isfile(os.path.join(mypath, f))]

print(mypath)