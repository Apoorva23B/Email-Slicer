email=input("Enter an email address : ")
if (email.count('@')==1 and len(email[:email.index("@")])>0 and len(email[email.index("@")+1:])>4):
 print("Username is : "+ email[:email.index("@")])
 print("Domain is : "+ email[email.index("@")+1:])
else:
 print("Invalid email..!")