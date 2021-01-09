#Getting Started with STRINGS
#a="Hello"
#print(a)
#print("%%"+"-"*20+"%%")

#Accessing individual elements from the strings
a="Hello World!"
#rint(a[0])#gives the 1st value
#print(a[-1])#gives the last value
#print(a[-5])
#print(a[-10])
#print(a[-15])#gives sting index out of range
#print(a[15])#gives string undex out of range'''
#print(a.find("o"))
#print(a.find("l"))
print(a.title())#Prints Hello World!
#-----------------------------------------------------------------------------------------#


#STRING MANIPULATION using: a)Upper b)Lower c)Join 
# d)Split e)Replace
#Split and Join functions
#JOIN Function
#s="-"
#seq=('a','b','c')
#print(s.join(seq))#joins the - in between a b c ie output=a-b-c

#SPLIT Function
#str='line1-abcdef \n line2-abc \n line3-abcd'
#print("Before Splitting :\n",str)
#print("After Splitting:\n",str.split())#Splits the strings by the ,

#a="Rohit Waghmare"
#print(a[:5])
#print(a[1:-1])#neglects 1st and last elements
#print(a[0:])#Gives all the char upto the last element
#print(a[::-1])#reverses the entire string
#print(a.upper())
#print(a.lower())
#print(a)

#email='mr[dot]waghmarerohit[at]gmail[dot]com'
#email1=email.replace('[at]','@')
#print(email1)
#print(email1.replace('[dot]','.'))

#examples
#s='this was a string'
#print(s)
#print(s.replace('string','list'))
#a=s.replace('was',"wasn't")
#print(a.replace('string','list'))

#s="F.R.I.E.N.D.S"
#print(s[::2])#used to remove '.'
#print(s[::2].lower())
#a=(s.replace('.',''))#another way
#print(a.lower()) 
#----------------------------------------------------------------------------------------
#a="rohit"
#print(a.capitalize())

#String formatting
'''first='Rohit'
last='Waghmare'
message=first+'['+last+'] is  coder'
print(message)
msg=f'{first}[{last}] is coder'
print(msg)'''