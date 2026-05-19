import src.Processing_files.get_list_users as Dictionary_manipulator
from src.intermediate_objects import users_list
from src.Processing_files.gemini_correct import ask_gemini_to_correct
from src.Processing_files.vosk_microphone import record_and_transcribe
from src.save_files import save_final_result
from src.intermediate_objects.final_result import FinalResult
from src.Processing_files.process_raw_text import process_raw_text
from datetime import datetime

if __name__ == "__main__":
    dict_users = Dictionary_manipulator.get_users_Dictionary()
    number_of_team_members = int(input("Enter the number of team members speaking: "))
    for _ in range(number_of_team_members):
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") # getting the current datetime
        name = input("Enter the name of the speaker: ") # input your name before you speak
        raw_text, duration = record_and_transcribe() # use vosk to record raw text the from speech and the duration of the speech
        final_result = FinalResult(timestamp, name, raw_text) # put results into an object to pass around
        final_result.time_taken = duration
        print("Original transcript:", raw_text)
        final_result.text_after_correction = ask_gemini_to_correct(raw_text) # use gemini to correct the raw text
        print("Corrected transcript:", final_result.text_after_correction)
        process_raw_text(final_result) # process the text to get the information we want to save

        Dictionary_manipulator.change_user(final_result.name_speaker, dict_users, final_result)

        final_result.speaker_turn_id = dict_users[final_result.name_speaker].spoken_times
        
        Dictionary_manipulator.update_user(dict_users) # update the user in the dictionary with the new information we got from the final result

        save_final_result(final_result) # save the final result to a csv file
