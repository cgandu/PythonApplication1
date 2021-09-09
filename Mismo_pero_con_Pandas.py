import pandas as pd

def find_top_ten(route: str):
    df = pd.read_csv(route, header=None, names=["users", "time_stamps", "pages"])
    sorted_df = df.sort_values(by=["users", "time_stamps"], ignore_index=True)
    agg_sorted_df = sorted_df.groupby("users").agg({"pages": lambda x: [*x]})

    occurring_triplets, occurring_triplets_count, triplets_to_sort = [], [], []

    def count_triplets(a):
        if len(a) > 2:
            for i in range(len(a)-2):            
                triplet = tuple(a[i:i+3])
                if triplet not in occurring_triplets:
                    occurring_triplets.append(triplet)
                    occurring_triplets_count.append(1)
                else:
                    occurring_triplets_count[occurring_triplets.index(triplet)] +=1
        
    for users_visit_history in agg_sorted_df["pages"]:
        count_triplets(users_visit_history)

    for triplet, frequency in zip(occurring_triplets, occurring_triplets_count):
        triplets_to_sort.append([triplet, frequency])
    
    triplets_to_sort.sort(key=lambda x: x[1], reverse=True)
    #print(triplets_to_sort[:10])
    new_df = pd.DataFrame([x[0] for x in triplets_to_sort])
    new_df.columns = ["1st Page", "2nd Page", "3rd Page"]
    return new_df.iloc[0:10]
find_top_ten("fakelog.txt")
