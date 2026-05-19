import os

from src.intermediate_objects.final_result import FinalResult
import src.intermediate_objects.users_list as users_list
import csv

# gets the users from the cvs file and put them into a dictionary, where the key is the name of the user and the value is the user object
def get_users_Dictionary(filename: str = "CSV/list_users.csv"): # not tested yet
    my_dict_users = {}
    # we dont handle the case where the directory dosent exist
    if os.path.exists(filename):
        with open(filename, "r", encoding="utf-8") as file:
            reader = csv.DictReader(file)
            for row in reader:
                user = users_list.User(
                    name=row["name"],
                    spoken_times=int(row["spoken_times"]),
                    total_words=int(row["total_words"]),
                    average_speach_rate=float(row["average_speach_rate"]),
                    average_time_taken=float(row["average_time_taken"]),
                    number_questions=int(row["number_questions"])
                )
                my_dict_users[user.name] = user
    return my_dict_users
    

def save_user(user: users_list.User, filename: str = "CSV/list_users.csv"): # not tested yet , and not used  
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([user.name, user.spoken_times, user.total_words, user.average_speach_rate, user.average_time_taken, user.number_questions])

def update_user(my_dict_users, filename: str = "CSV/list_users.csv"): # not done yet, completly unfunctional
    users = get_users_Dictionary(filename)
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "spoken_times", "total_words", "average_speach_rate", "average_time_taken", "number_questions"])
        for user in my_dict_users.values(): 
            writer.writerow([user.name, user.spoken_times, user.total_words, user.average_speach_rate, user.average_time_taken, user.number_questions])
        

def change_user(user_name : str, my_dict_users, final_result: FinalResult):
    if user_name not in my_dict_users:
        my_dict_users[user_name] = users_list.User(name=user_name, spoken_times=0, total_words=0, average_speach_rate=0.0, average_time_taken=0.0, number_questions=0)
    User = my_dict_users[user_name]
    User.spoken_times += 1
    User.total_words += final_result.num_words
    new_average_speach_rate = User.average_speach_rate * (User.spoken_times - 1) / User.spoken_times + final_result.speach_rate_wps / User.spoken_times
    User.average_speach_rate = new_average_speach_rate
    new_average_time_taken = User.average_time_taken * (User.spoken_times - 1) / User.spoken_times + final_result.duration / User.spoken_times
    User.average_time_taken = new_average_time_taken
    if(final_result.is_question):
        User.number_questions += 1
    
