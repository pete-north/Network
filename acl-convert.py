#import required things
import json
from ntc_templates.parse import parse_output

#welcome message for production value
print("##############################################################")
print("###                    IOS ACL CONVERTER                   ###")
print("##############################################################")
print("This script converts Cisco IOS CLI ACL's into JSON format")
print("Enter/Paste show ip access-lists output in the terminal")
print("to submit the list, enter a blank line")
print()
print("Enter/Paste show command output:")


#capture IOS ACL input from user
acl_output = []
while True:
    line = input()
    if line:
        acl_output.append(line)
    else:
        break
acl_input = '\n'.join(acl_output)

#my auty function
def input_loop():
    while True:
        line = input()
        if line:
            acl_output.append(line)
        else:
            break
    acl_input = '\n'.join(acl_output)
    return acl_input

#name your kid function
def name_function():
    return input()

#absolute mad man loop
while not acl_input:
    print("you forgot to type anything, try pasting in your acl:")
    acl_input = input_loop()
    if acl_input:
        break

#Parse input with NTC templates
acl_parsed = parse_output(platform="cisco_ios", command="show ip access-lists", data=acl_input)

#user feedback
print("...ACL successfully parsed!")

#confirm save a file
input("Press enter to save:")

#create a file
acl_file = json.dumps(acl_parsed, indent = 4)

#call name_function
print("What should we name the child?")
childs_name = name_function()

# Writing to file
with open(childs_name, "w") as outfile:
    outfile.write(acl_file)

print("Success! Check script directory for little", childs_name)
