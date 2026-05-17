# Base class for each users 
# we would draw all the users from a csv file in order to make the data analysis more efficient, and we would update the csv file after each meeting to keep track of the users' data
class User:
    def __init__(self, id_user, name, spoken_times, total_words, average_speach_rate, average_time_taken, number_questions):
        self.id_user = id_user # the position of the user in the csv file, which will be used to update the user's data in the csv file
        self.name = name # the name of the user
        self.spoken_times = spoken_times # how many times the user spoke in total
        self.total_words = total_words # how many words the user spoke in total
        self.average_speach_rate = average_speach_rate
        self.average_time_taken = average_time_taken # the average time taken by the user for each speech
        self.number_questions = number_questions # how many questions the user asked in total
