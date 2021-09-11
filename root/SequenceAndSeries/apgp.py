#Code for calculating the first and last term of any AP.

# Let a=First Term of the AP
#And l=Last term of the GP
#d=common difference
#n=number of terms
#We know Formula of AP, an=a+(n-1)d


print("How may I help you!! <3")
print("")
print("Chosse which operation you want to do :")
print("1. Find number of terms when First and last term of AP is given.")

selectOption = input("Please select one of the option :")

#Finding number of terms of a AP

def numberofterms():
    a=float(input("Enter the first term of the AP :"))
    l=float(input("Enter the last :"))
    d=float(input("Enter the common difference :"))

    differenceof1standlastterm=(l-a)
    numberoftermsminus1=differenceof1standlastterm/d
    numberoftermsanswer=numberoftermsminus1+1

    print("The number of terms in the AP is :",numberoftermsanswer)



if (selectOption == '1'):
    numberofterms()




# changes made

