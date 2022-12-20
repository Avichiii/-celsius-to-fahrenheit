'''converts celsius-to-fahrenheit'''

def cel_fer(num):

    return (num * 9/5) + 32

num = int(input("enter num: "))
conversion = cel_fer(num)

print(conversion)