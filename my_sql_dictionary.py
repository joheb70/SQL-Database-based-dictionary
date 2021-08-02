#Objective : To create interactive dictionary using mysql database
#Author : Abdul Joheb Ansari
# 
# 
# -----------------------------------------------------------------------

import mysql.connector
from difflib import get_close_matches

con = mysql.connector.connect(
user = "ardit700_student",
password = "ardit700_student",
host = "108.167.140.122",
database = "ardit700_pm1database"
)


cursor = con.cursor()
word = input("Enter the word : ")
query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()



def findmeaning(word):
    word = word.lower()  
    
    if word in results:
        return results[word]
    elif word.title() in results:
        return results[word.title()]
    elif word.upper() in results:
        return results[word.upper()]
    elif len( get_close_matches(word, results.keys()))>0:
        yesno = input("Did you mean %s instead? Enter Y if Yes, or N for No :" % get_close_matches(word,results.keys())[1])
        if yesno == "Y":
            return results[get_close_matches(word, results.keys())[1]]
        elif yesno == "N":
            return "Check Spelling" 
        else:
            return "The system does not understand your input"
    else:
        return "The word was not found. Please check spelling" 
     

if results:
    for result in results:
        print(result[1])
    else:
        print("Try another word \U0001f604 ")


        
