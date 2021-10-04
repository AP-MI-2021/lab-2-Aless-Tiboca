
def get_temp(temp, tip, convers):

    """Functia face conversia din diferite baze de temperatura (C, F, K)

    Args:
        temp ([float]): [valoarea initiala de temperatura]
        tip ([string]): [tipul valorii initiale]
        convers ([string]): [tipul de temperatura in care se face conversia]

    Returns:
        [float]: [returneaza conversia intre tipurile precizate]
    """

    if convers==tip:
         return temp
    if convers=="K":
        if tip=="C":
            return (temp + 273.15)
        else:
            return ((temp + 459.67) * 5/9)
    elif convers=="F":
        if tip=="K":
            return ((temp * 9/5) - 459.67)
        else:
            return ((temp * 9/5) + 32)
    else:
        if tip=="K":
            return (temp - 273.15)
        else:
            return ((temp - 32) * 5/9)                         

def test_get_temp():
    assert get_temp(0, "C", "K") == 273.15
    assert get_temp(75, "C", "C") == 75
    assert get_temp(20, "K", "F") == -423.67


def cmmdc(m, n):
    while m!=n:
        if m>n: 
            m = m - n
        else: 
            n = n - m
    return m   

def cmmmc(m, n):
    if m == 0 or n == 0:
        return 0
    return m * n // cmmdc(m, n)


def get_cmmmc(list):
    min_mul = 1
    for i in list:
        min_mul = cmmmc(min_mul, i)
    return min_mul 

def test_get_cmmmc():
    print(" ")
    list1 = [4, 5, 9, 8]
    list2 = [0, 1, 5, 6]
    list3 = [4, 2, 8, 16]
    assert get_cmmmc(list1) == 360
    assert get_cmmmc(list2) == 0
    assert get_cmmmc(list3) == 16


def main ():
    
    test_get_cmmmc()
    test_get_temp()

    while True:
        print("""
            Alegeti:
            1. Faceti conversia intre doua scari de temperatura.
            2. Cmmmc dintre n numere.
            x. Iesire.
                """)
        a = input("Introduceti o optiune: ")
        if a == '1':
           temp = float(input("Dati o temperatura: "))
           scara1 = input("Dati scara in care este temperatura: ") 
           scara2 = input("Dati scara in care vreti sa faceti conversia: ")
           print("Conversia din scara " + scara1 + " in scara " + scara2 + " este: " + str(get_temp(temp,scara1,scara2))) 
        elif a == '2' :
            list = []
            nr = int(input("Dati nr. de numere a sirului: "))
            print("Dati elementele sirului:")
            for i in range(nr):
                aux = int(input())
                list.append(aux)
            print("Cmmmc al elementelor listei este: " + str(get_cmmmc(list)))    
        elif a == 'x':
            break 
        else:
            print("Optiune gresita! Mai incercati.")

if __name__ == '__main__':
    main()    
