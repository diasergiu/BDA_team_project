import src.intermediate_objects.users_list as users_list
import csv

# gets the users from the cvs file and put them into a dictionary, where the key is the name of the user and the value is the user object
def get_users(filename: str = "list_users.csv"): # not tested yet
    with open(filename, "r", encoding="utf-8") as file:
        reader = csv.DictReader(file)
        my_dict_users = {}
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
    

def save_user(user: users_list.User, filename: str = "list_users.csv"): # not tested yet
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow([user.name, user.spoken_times, user.total_words, user.average_speach_rate, user.average_time_taken, user.number_questions])

def update_user(user: users_list.User, my_dict_users, filename: str = "list_users.csv"): # not done yet, completly unfunctional
    users = get_users(filename)
    users[user.name] = user
    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["name", "spoken_times", "total_words", "average_speach_rate", "average_time_taken", "number_questions"])
        