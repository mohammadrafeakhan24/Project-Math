import math


# ===================CODE FOR GP TO FIND LAST TERM STARTS ============================


def gp_last_term():
    term_1 = float(input("Enter 1st term of GP: "))
    common_ratio = float(input("Enter common ratio(r): "))
    no_terms = int(input("Enter no. of terms: "))

    # to find last term
    result_gp = term_1 * (int)(math.pow(common_ratio,no_terms-1))
    print(result_gp)


# ====================CODE FOR GP TO FIND LAST TERM END ==============================

#====================CODE FOR GP TO FIND SUM===========================

def gp_sum():
    term_a = float(input("Enter 1st term of GP: "))
    c_ratio = float(input("Enter common ratio: "))
    n_term = int(input("Enter no of term: "))
    
    # checking if r>1 or r<1
    
    if c_ratio > 1.0:
        sn = (term_a)/(c_ratio-1) * ((int)(math.pow(c_ratio,n_term))-1)
        print(sn)
    elif c_ratio < 1.0:
        sn2 = (term_a)/(1-c_ratio) * (1-(int)(math.pow(c_ratio,n_term)))
        print(sn2)
