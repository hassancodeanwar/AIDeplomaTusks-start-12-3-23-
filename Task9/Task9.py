import re

with open('C:\MyCourses\AIDiploma\Tasks\Task9\Task9.text', 'r') as file:
    data = file.read()
    
    
    print("\nNames List")
    pattern1= r'[A-z]+ [A-z]+'
    matches1 = re.findall(pattern1, data)
    namesList = []
    for name in matches1:
        namesList.append(name)
    print(namesList)       
    
    # Print each element in namesList on a single line
    print("\n")
    for name in namesList:
        print(name)
    
    
        
    print("\nPhones List")
    pattern2= r'\(\d{3}\) \d{3}-\d{4}'
    matches2 = re.findall(pattern2, data)
    phoneslist = []
    for phone in matches2:
        phoneslist.append(phone)
    print(phoneslist)       
    # Print each element in phonesList on a single line
    print("\n")
    for phone in phoneslist:
        print(phone)

    
    
    
    print("\nEmails List")
    pattern3 = r'[A-z0-9\.]+@[A-z0-9]+\.[A-z]+'
    matches3 = re.findall(pattern3, data)
    emailsList = []
    for email in matches3:
        emailsList.append(email)
    print(emailsList)   
    # Print each element in emailsList on a single line
    print("\n")
    for email in emailsList:
        print(email)