English = float(input("masukan nilai English :"))
MTK = float(input("masukan nilai MTK :"))
Indo = float(input("masukan nilai Indo :"))
IPA = float(input("masukan nilai IPA :"))
IPS = float(input("masukan nilai IPS :"))

A =  (English+MTK+Indo) /3
B =  (English+MTK+Indo+IPA+IPS) /5

if A >=75 :
    print ("anda lulus")
elif B >=70 :
    print ("anda lulus")
elif B <=70 :
    print ("anda tidak lulus")
elif English >=90 and MTK >=90 :
    print ("anda lulus")
else :
    ("anda tidak lulus")



