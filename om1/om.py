
punct="""!"#$&%\'()*+,-,/;:<=>?@[\\]^_{|}`~"""
userstr=input("Enter the string")
newstr=""


def ispallindrome(check):
    if(check==check[::-1] ):
        print("Pallindrome String")
    else:
        print("Not a pallindrome string")

for i in userstr:
    if(i not in punct):
        newstr=newstr+i
lstr=newstr.lower()
spcremove=lstr.replace(" ","")

ispallindrome(spcremove)


