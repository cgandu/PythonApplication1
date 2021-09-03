
#1 Agrupo x usuario
#2 Ordeno cronologicamente SECUENCIAS
#3 Arma y agrupa secuencias 
#4 Cuenta frecuencia
#5 Ordena por frecuencia

def find_top_ten(route: str) -> list:

    f = open(route, "r")
    unique_user_list, users_keys = [], []

    for line in f:    # Unpack de registros
        user_id, time_stamp, page = line.strip().split(",")
        users_visits = [user_id, time_stamp, page]
        unique_user_list.append(users_visits)    
        if user_id not in users_keys: 
            users_keys.append(user_id)

    users_dict = {k: [] for k in users_keys}

    # Ordena secuencias de visitas 
    for user in unique_user_list:
        user_id, time_stamp, page = user
        users_dict[user_id].append((time_stamp, page))
        users_dict[user_id] = sorted(users_dict[user_id])

    triplets_frequencies, triplets_combinations, triplets_to_sort = [], [], []

    for user_page_visits in users_dict:    
        # para los usuarios con 3 o mas visitas, arma secuencias/triplet y agrupa
        if len(users_dict[user_page_visits]) > 2 :
            for i in range(len(users_dict[user_page_visits])-2):
                triplet = tuple(page_visit[1] for page_visit in users_dict[user_page_visits][i:i+3])
          
                if triplet not in triplets_combinations:
                    triplets_frequencies.append(1)
                    triplets_combinations.append(triplet)
                
                else:
                    triplets_frequencies[triplets_combinations.index(triplet)] += 1

    for triplets, frequency in zip(triplets_combinations, triplets_frequencies):
        triplets_to_sort.append([triplets, frequency])

    triplets_to_sort.sort(key=lambda x: x[1], reverse=True )
    return (triplets_to_sort[:10])

print("Triplets & frequency:")
print(find_top_ten("fakelog.txt"))
