#string concatenation
b = ":"
c = ")"
s1 = b + 2*c #c appears 2times and concate with b
f = "a"
g = " b"
h = "3"
s2 = (f+g)*int(h) #the type of value identified and multipy the concate string

o/p: 
:))
a ba ba b


# string slicing 
s = "ABC d3f ghi"
print(s[3:len(s)-1]) 
print(s[4:0:-1]) #stop value is excluded
print(s[6:3]) #it is decrementing but step is not mentioned

 o/p:
 d3f gh
d CB


#input/output
word=input("enter the string:")
print("I can " + word + " better than you!")
print(5 * word)

o/p:
enter the string: run
I can run better than you!
runrunrunrunrun


