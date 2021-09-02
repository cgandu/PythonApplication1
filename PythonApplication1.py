
#1 Agrupo x usuario
#2 Ordeno cronologicamente SECUENCIAS
#3 Arma y agrupa secuencias 
#4 Obtiene frecuencias correspondientes
#5 Ordena por frecuencia desc

logFile = open("fakelog.txt", "r")
unique_user_list, users_keys = [], []

for line in logFile:    # Unpack de registros del log
    user_id, time_stamp, page = line.strip().split(",")
    users_visits = [user_id, time_stamp, page]
    unique_user_list.append(users_visits)    
    if user_id not in users_keys: #obtengo lista de usuarios unicos
        users_keys.append(user_id)

users_dict = {k: [] for k in users_keys} # Arma dict de usuarios y sus respectivas page visits y timestamps

# Se busca que secuencias de 3 visitas fueron realizadas ==> agrega visita para c/ usuario y reordena cronologica/timestamp 
for user in unique_user_list:
    user_id, time_stamp, page = user
    users_dict[user_id].append((time_stamp, page))
    users_dict[user_id] = sorted(users_dict[user_id])

triplets_frequencies, triplets_combinations, triplets_to_sort = [], [], []

for userId in users_dict:    
    # para los usuarios con 3 o mas visitas, arma secuencias/triplet y agrupa
    if len(users_dict[userId]) > 2 :
        for i in range(len(users_dict[userId])-2):
            triplet = (users_dict[userId][i][1], users_dict[userId][i+1][1], users_dict[userId][i+2][1])
          
            if triplet in triplets_combinations:
                triplets_frequencies[triplets_combinations.index(triplet)] += 1
            else:
                triplets_frequencies.append(1)
                triplets_combinations.append(triplet)

for t, f in zip(triplets_combinations, triplets_frequencies):
    triplets_to_sort.append([f, t])

top10 = sorted(triplets_to_sort, reverse = True)[:10]
print(top10)
