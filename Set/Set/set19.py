morning = {"Amit", "Rehan", "Soham", "Nisarg"}
afternoon = {"Riya", "Nikhil", "siddhant", "Priya"}
print("Present in both sessions:", morning & afternoon)
print("Present only in morning:", morning - afternoon)
print("Present only in afternoon:", afternoon - morning)
print("Present in at least one session:", morning | afternoon)