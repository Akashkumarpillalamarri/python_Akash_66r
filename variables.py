
n="My naMe is Akash KuMar"
m="akash"
print(" upper ",n.upper())
print("lower ",n.lower())
print("title ",n.title())
print("is upper",m.isupper())
print("is lower",m.islower())
print("swapcase", n.swapcase())
print("capitalize",n.capitalize())
j="    hie"
print(j)
j=j.strip()
print(j)
#lstrip-- Left strip   and rstrip---- Right Strip
# to remove spaces at lest and right side we use the lstrip and rstrip

h="   hello everyone   "
print(" left strip:",h.lstrip())
print("right strip:",h.rstrip())


#3
# replace 
k=" to day we are having python class in classroom"
print(k)
k=k.replace("a","_")
print(k)


#4
#search  and find in string
#find() and index() both are used to find the index of the first occurrence of the specified
 # now example
l="today we are working on string operations"
print(l.find("on"))
print(l.index("on"))
print("index of o:",l.index("o"))
print("fing of o",l.find("o"))
print("for z not in strng  gives:",l.find("z"))
print("count of on ",l.count("on"))
print("need from reverse(last)",l.rindex("o"))
print("len of string is ",len(l))
# count
print("count of o",l.count("o"))
