
boy_name = input("Enter boy name : ")
boy_age = int(input("Enter boy age : "))

girl_name = input("Enter girl name : ")
girl_age = int(input("Enter girl age : "))

# using abs because we want the age difference to be positive regardless of who is older
age_difference = abs(boy_age - girl_age)

print(boy_name + " loves " + girl_name + " and their age difference is " + str(age_difference) + " years.")
print(f"{boy_name} loves {girl_name} and their age difference is {age_difference} years.")



'''
this is a multiline comment
'''