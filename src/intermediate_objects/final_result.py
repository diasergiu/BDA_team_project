# base class for the final result of the processing, which will be saved to a csv file
class FinalResult:
    def __init__(self, timestamp: str, name_speaker: str, raw_text: str):
        # Required at creation time — you have these from the transcript
        self.timestamp = timestamp
        self.name_speaker = name_speaker
        self.raw_text = raw_text

        # Populated later after text processing
        self.text_after_correction: str | None = None
        self.is_question: bool | None = None
        self.num_words: int | None = None
        self.text_size_chars: int | None = None
        # self.speaker_turn_id: int | None = None

    def create_final_result(self, timestamp: str, name_speaker: str, raw_text: str) -> FinalResult:
        # how do you make a constructor in python?
        return FinalResult(timestamp, name_speaker, raw_text)

    def to_csv_row(self) -> list:
        return [
            self.timestamp,
            self.name_speaker,
            self.raw_text,
            self.text_after_correction,
            self.is_question,
            self.num_words,
            self.text_size_chars,
            # self.speaker_turn_id,
        ]


