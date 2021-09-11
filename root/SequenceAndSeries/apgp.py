import math

# CODE FOR AP


#Code for calculating the first and last term of any AP.

# Let a=First Term of the AP
#And l=Last term of the GP
#d=common difference
#n=number of terms
#We know Formula of AP, an=a+(n-1)d


print("How may I help you!! <3")
print("")
print("Chosse which operation you want to do :")
print('''1. Find number of terms when First and last term of AP is given.
2. Find last term when first term, number of term and common ratio given    
''')

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







# ============================CODE FOR GP STARTS ============================


def gp_last_term():
    term_1 = float(input("Enter 1st term of GP: "))
    common_ratio = float(input("Enter common ratio(r): "))
    no_terms = int(input("Enter no. of terms: "))

    # to find last term
    result_gp = term_1 * (int)(math.pow(common_ratio,no_terms-1))
    print(result_gp)










# ========================IF STATEMENT FOR EXECUTION OF CODE=========================
if (selectOption == '1'):
    numberofterms()
elif (selectOption == '2'):
    gp_last_term()



