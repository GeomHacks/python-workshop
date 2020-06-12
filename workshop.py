#variables and functions

b = 2 + 3
a = b/5
c = (a + 1)**2
d = abs(-1 * c)


def add_tip(total, tip_percent):
    ''' Return the total amount of a meal including tip'''
    tip = tip_percent*total
    return total + tip

finalprice = add_tip(20, 0.15)

print(finalprice)
'''
this is a multiline comment
as you can see I can type in comments
on multiple lines
'''
#==, !=, >, < , >=, <=
'''
lets try if else statements now
'''
if (27>5):
    print("27 is more then 5")

test = True

def check_test(test):
    if (test):
        print("if statement")
    else:
        print("else statement")
'''strings and lists'''
l = [1,2,3,4,5,6]
s = "string"

'''loops'''
for item in l:
    print(item)
for char in s:
    print(char)

for x in range(0, 5):
    print(l[x])
for x in range(0, 5, 2):
    print(l[x])

'''sets'''
somelist = [1,1,2,2,3,3]
someset = set(somelist)
print(someset)

'''while loops'''
num = 0
while(num < 5):
    print(num)
    num+=1
