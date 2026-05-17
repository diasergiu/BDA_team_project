import csv
import os
from src.intermediate_objects.final_result import FinalResult

def save_transcript(transcript, filename="raw_transcript.txt"):
    with open(filename, "a", encoding="utf-8") as f:
        f.write(transcript + "\n")  


HEADER = ["timestamp", "name_speaker", "raw_text", "text_after_correction", "is_question", "num_words", "text_size_chars", "speaker_turn_id"]

def save_final_result(final_result: FinalResult, filename: str = "final_results.csv"):
    write_header = not os.path.exists(filename)
    with open(filename, "a", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        if write_header:
            writer.writerow(HEADER)
        writer.writerow(final_result.to_csv_row())