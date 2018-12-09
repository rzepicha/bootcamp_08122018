# temp1=float(input("Podaj temp1: "))
# temp2=float(input("Podaj temp2: "))
# temp3=float(input("Podaj temp3: "))
# temp4=float(input("Podaj temp4: "))
# temp5=float(input("Podaj temp5: "))
# temp6=float(input("Podaj temp6: "))
# temp7=float(input("Podaj temp7: "))
#
# sr=(temp1+temp2+temp3+temp4+temp5+temp6+temp7)/7
#
# print (sr)

#moje rozwiązanie:
i=1
suma=0
while i<=7:
    temp=float(input(f"Podaj temp {i}: "))
    suma+=temp
    i+=1
    if i==8:
        print (suma/7)
        break

#rozwiązanie Rafała:
# ile_dni=7
# temp=0
# i=1
# while i<=ile_dni:
#     temp_i=float(input(f"Podaj temperaturę w dniu {i}: "))
#     temp+=temp_i
#     i+=1
# print ("Średnia temperatura wyniosła: ", temp/ile_dni)