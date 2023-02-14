O.Ádám- 1, T.Ricsi- 2.
file = open("vizes.txt","r")



#1 O.Ádám
viz=open("ujproci.txt", "w")
file_data=[]
telepules = []

for telepules in file:
    if jatek[-1] == "\n":
        file_data.append(telepules[:-1].split("\t"))
    else:
         file_data.append(telepules[:-1].split("\t"))

del file_data[0]

for i in range(len(file_data)):
    telepules.append(file_data[i][1])

print("Ennyi településen mértek vizet: ",(len(telepules)))
print(len(telepules))

#2 T.Richárd
osszeg=0
for i in range(len(Lvíz)):
   osszeg += int(Lvíz[i][3])

print("Itt és akkor mérték a legmagasabb vízállást ", round(osszeg/len(Lvíz),2))


Lvíz = []

for i in file:
      if(i[-1]=='\n'):
        Lvíz.append(i[:-1].split('\t'))


del Lvíz[0]


for i in range(len(Lvíz)):
    csere = ''


