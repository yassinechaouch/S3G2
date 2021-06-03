#On the Python file, you need to add the addressing of "webArguments" to "Python Arguments"
# In my case i had to add the following to my "normal" script:

import cgi, cgitb
print( "Content-type: text/html\n\n" )   #for showing print on HTML
data = cgi.FieldStorage()
argument = data["webArguments"].value    #argument = name of PLC i need to fetch
#some script for connecting to PLC and reading current value of 
#variable  with name "argument", in this example "aiTemperature"
print(plcVar)