E = 2.71828182

def e_to_x(x):
    return E ** x

def compound_interest(ammount):
    return ammount*E

def main():
    print(e_to_x(5))
    print(compound_interest(5))

main()