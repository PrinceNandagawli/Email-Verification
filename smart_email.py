user = input("Enter the email: ")
s =0
u =0
v =0
if len(user)>=6:
    if user[0].isalpha():
        if ("@"in user) and (user.count("@")==1):
            if (user[-4]==".") ^ (user[-3]=="."):
                for i in user:
                    if i==i.isspace():
                        s=1
                    elif i.isalpha():
                        if i==i.upper():
                            u=1
                    elif i.isdigit():
                        continue 
                    elif i=="_" or i=="." or i=="@":
                        continue
                    else:
                        v=1       
                if s==1 or u==1 or v==1:
                    print("wrong email") 
                else:
                    print("Email is Correct")           
            else:
                print("wrong email (include .com,.in,net,etc)")
        else:
            print("wrong email (@ error)")
    else:
        print("wrong email (include Alphabet)")
else:
    print("wrong email (include more characters)")
