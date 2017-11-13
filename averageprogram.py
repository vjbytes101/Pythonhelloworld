N = int(raw_input("Enter the numbers you want to average"))
sum = 0
count = 1
while count <= N:
    num = float(raw_input("Enter your number"))
    sum = sum + num
    count = count+1
average = sum/N
print "Average of ",N,"numbers is :",average
