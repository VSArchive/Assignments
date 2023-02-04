import re

email = "498_bt19@iiitkalyani.ac.in"

match1 = re.search('@iiitkalyani.ac.in', email)
match2 = re.search('@yahoo.in', email)

if match1:
    print("Belongs to iiitkalyani.ac.in")
elif match2:
    print("Belongs to yahoo.in")
else:
    print("Dose not belong to yahoo or iiitkalyani")
