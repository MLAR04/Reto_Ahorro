#random function and saved amounts
#import separations
import json
import random
from datetime import datetime
import os

def save_data(config_data, new_saved_data):
    json_squeleton={}
    json_squeleton['config'] = config_data
    json_squeleton['saved'] = new_saved_data
    if os.path.isfile("saved.json"):
        with open("saved.json",'w') as saved_file:
            json.dump(json_squeleton,saved_file)
            saved_file.close()
    else:
        print("No existe el archivo para guardar la informacion")
    



def select_random_input():
   if os.path.isfile("saved.json"):
      with open("saved.json",'r') as saved_file:
        file_data = json.load(saved_file)
        config_data = file_data["config"]
        all_saved_data = [ data for data in file_data["saved"]]
        print(len(all_saved_data))
        new_save={}
        if len(all_saved_data) < 1:
            #modificar!!!!
            if config_data["valid_max_amount"]:
               random_amount = random.randrange(20, config_data["max_amount"],5)
            else:   
                random_amount = random.randrange(20, int(config_data["total_amount"]/2), 5)
            print("You need to save:",random_amount)
            new_save = {
               "amout":random_amount,
               "date": str(datetime.now()),
               "remaining": int(config_data["total_amount"]) - random_amount
            }
            new_data_index = len(all_saved_data)
            file_data["saved"][new_data_index] = new_save
        elif len(all_saved_data) == config_data["separations"]-1:
            print("You need to save:", file_data["saved"][str(len(all_saved_data))]["remaining"])
            print("Is the Lastone!!!")
            new_save = {
               "amout":file_data["saved"][str(len(all_saved_data))]["remaining"],
               "date": str(datetime.now()),
               "remaining": 0
            }
            new_data_index = len(all_saved_data)+1
            file_data["saved"][new_data_index] = new_save
        elif 1 < len(all_saved_data) < config_data["separations"]:
            alredy_used_amounts =[]
            print(file_data)
            for data in file_data["saved"]:
                print(data)
                alredy_used_amounts.append(int(data['amount']))
            if config_data["valid_max_amount"]:
               random_amount = random.randrange(1, config_data["max_amount"])
            else:   
                random_amount = random.randrange(1, int(config_data["total_amount"]/2))
            while random_amount in alredy_used_amounts:
                if config_data["valid_max_amount"]:
                    random_amount = random.randrange(20, config_data["max_amount"],5)
                else:   
                    random_amount = random.randrange(20, int(config_data["total_amount"]/2),5)
            print("You need to save:",random_amount)
            new_save = {
               "amout":random_amount,
               "date": str(datetime.now()),
               "remaining": int(config_data["total_amount"]) - random_amount
            }
            new_data_index = len(all_saved_data)+1
            file_data["saved"][new_data_index] = new_save
        else:
           print("You alredy end this challenge!!")
        save_data(config_data, file_data['saved'])

select_random_input()