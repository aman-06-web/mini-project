
## Billing Amount
#first 100 calls free
#charge per call for 100 to 200 is 0.5

#charge per call for 200 to 300 is 0.75


#charge per call for 300 to 400 is 1


#charge per call for calls greater than 400 is 1.5


# base price 500
# 18% GST







a=int(input("Enter the Calls:"))
b=0
c=0
d=0
Total=0
if (a<=100):
    b=0
    c=0
    d=c + 500
    e=(c + 500)*0.18
    print("No charges for first 100 calls")
if(a >100 and a<=200):
    b=a-100
    c=b*0.5
    d=c + 500
    e=(c + 500)*0.18
if (a>200 and a<=300):
    b=a-200
    c=b*0.75
    d=c+50+500
    e=(c+50+500)*0.18
if (a>300 and a<=400):
    b=a-300
    c=b*1
    d=c +50+75+ 500
    e=(c +50+75+ 500)*0.18
if (a>400):
    b=a-400
    c=b*1.5
    d=c+50+75+100+500
    e=(c+50+75+100+500)*0.18
Total=d+e
print("Payable Amount is", Total)

