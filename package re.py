data = "Deadpool is a funny character"

import re
if(re.search(r"Deadpool",data)):
    print("yes")
else:
    print("no")

print(re.sub(r"funny",r"violent",data))