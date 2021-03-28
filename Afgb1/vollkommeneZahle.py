def abund(n):
    for p in range(0,n):
        i = 1
        while i<p:
            liste = []
            sum = 0
            for i in range(2,n+1):
                if p%i == 0:
                    zahl = p/i
                    liste.append(zahl)

            for item in liste:
                item = int(item)
                sum+=item

            if sum == p:
                print("@", p, " ist eine vollkommene Zahl.")
            elif sum > p:
                print("∆", p, " ist eine abundante Zahl.")
            else:
                print("•", p, " ist eine defiziente Zahl.")


            i+=1

abund(50)
