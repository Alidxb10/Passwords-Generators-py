charset = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','&','*','#']
mfile = open("allpassword.txt","w")
for i in charset:
for j in charset:
for k in charset:
for m in charset:
mfile.write(i+j+k+m+"\n")
mfile.close()


#code to sort the strong and weak passwords in different text files
numbers = ['0','1','2','3','4','5','6','7','8','9']
special = ['&','*','#']
alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
password = open("allpassword.txt").readlines()
strong = open("strong.txt","w")
weak = open("weak.txt","w")

for i in password:
    # if the first character is a number then the password is stored in the WEAK text file
    if(i[0] in numbers):
        weak.write(i)
    else:
        specialcount = 0
        numcount = 0
        alphacount = 0
        for char in i:
            if char in special:
                specialcount = 1
            if char in numbers:
                numcount = 1
            if char in alphabet:
                alphacount = 1
        # if the password has at least a number, alphabet character, and special character then the password is stored in the STRONG text file
        if (specialcount == 1):
            if (numcount == 1):
                if (alphacount ==1):
                    strong.write(i)
        #otherwise it will be stored in the WEAK text file 
        else:
            weak.write(i)
strong.close()
weak.close()
