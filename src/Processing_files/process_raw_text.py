from src.intermediate_objects.final_result import FinalResult

def process_raw_text(final_result):
    final_result.is_question = is_question(final_result.text_after_correction)
    final_result.num_words = count_words(final_result.text_after_correction)
    final_result.text_size_chars = count_characters(final_result.text_after_correction)
    final_result.speach_rate_wps = get_speach_rate_wps(final_result.num_words, final_result.duration)
    # final_result.speaker_turn_id not implemented yet, as it requires tracking multiple speakers and their turns in the conversation, which is a more complex task that may involve speaker diarization techniques.
    return final_result


def is_question(text):
    for index in range(len(text)-1, -1, -1):
        if text[index] == '?':
            return True
        elif text[index] == ' ':
            continue
        else:
            return False
        
def count_words(text): # 
    return len(text.split(' ')) # This is a simple word count based on spaces. It may not be the most efficient method

def count_characters(text):
    char_count = 0
    for char in text:
        if ord(char) > 64 and ord(char) < 91 or ord(char) > 96 and ord(char) < 123: # Only count letters, ignore spaces and punctuation
            char_count += 1
    return char_count

def get_speach_rate_wps(word_count, duration):
    if duration > 0:
        return word_count / duration
    else:
        return 0
    
