import json
def load_data (filename):
    with open (filename,"r") as f:
        data = json.load(f)
    return data

def clean_data(data):
    cleaned_data = []
    unique_users = set()
    
    # clean rating
    text_to_num = {"one":1,"two":2,"three":3,"four":4,"five":5}
    for users in data:
        raw_rating = str(users["rating"].strip().lower())
        if raw_rating in text_to_num:
            raw_rating = text_to_num[raw_rating]
        users["rating"] = raw_rating
        #print(raw_rating)
        
        # handling missing data
        raw_age = users.get("age")
        if (raw_age == None):
            users["age"] = None
        #print(raw_age)
        
        # handling duplicate data
        if (users["name"] in unique_users):
            continue
        unique_users.add(users["name"])
        cleaned_data.append(users)
    print(cleaned_data)


data = load_data("E:\\Material\\Coding\\Python\\Data\\data.json")
clean_data(data)
     