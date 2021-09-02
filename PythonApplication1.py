
logFile = open("fakelog.txt", "r")

lista=[]
llaves = []

for linea in logFile:    
    user_id, time_stamp, pagina = linea.strip().split(",")
    users_visits = [user_id, time_stamp, pagina]
    lista.append(users_visits)
    if user_id not in llaves:
        llaves.append(user_id)

thisdict = {k: [] for k in llaves} #dict de usuarios y respectivas visitas


for x in lista:
    usr, ts, url = x
    thisdict[usr].append((ts, url))
    thisdict[usr] = sorted(thisdict[usr])


triplet_freq = []
triplet_comb = []

for entry in thisdict:
    
    if len(thisdict[entry]) > 2 :
        for i in range(len(thisdict[entry])-2):
            triplet = (thisdict[entry][i][1], thisdict[entry][i+1][1], thisdict[entry][i+2][1])
          
            if triplet in triplet_comb:
                triplet_freq[triplet_comb.index(triplet)] += 1
            else:
                triplet_freq.append(1)
                triplet_comb.append(triplet)

triplets_to_sort = []
for t, f in zip(triplet_comb, triplet_freq):
    triplets_to_sort.append([f, t])

top10 = sorted(triplets_to_sort, reverse = True)[:10]

print(top10)