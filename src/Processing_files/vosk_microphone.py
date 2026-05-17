"""Simple Vosk example.

This records from the microphone, transcribes speech with Vosk, prints the
transcript, and saves it to transcript.txt.
"""

import json
import queue
from datetime import datetime
import sounddevice as sd
from vosk import Model, KaldiRecognizer
import time 


MODEL_PATH = "vosk-model-en-us-0.22-lgraph"
SAMPLE_RATE = 16000
OUTPUT_FILE = "transcript.txt"

q = queue.Queue()


def callback(indata, frames, time, status):
    if status:
        print(status)
    q.put(bytes(indata))


model = Model(MODEL_PATH)
recognizer = KaldiRecognizer(model, SAMPLE_RATE)

def record_and_transcribe():
    print("Start speaking. Press Ctrl+C to stop.")
    start_time = time.perf_counter()
    full_text = ""

    try:
        with sd.RawInputStream(
            samplerate=SAMPLE_RATE,
            blocksize=8000,
            dtype="int16",
            channels=1,
            callback=callback,
        ):
            while True:
                data = q.get()

                if recognizer.AcceptWaveform(data):
                    result = json.loads(recognizer.Result())
                    text = result.get("text", "")
                    if text:
                        print("You said:", text)
                        full_text += text + " "

    except KeyboardInterrupt:
        print("\nStopped recording.")
    end_time = time.perf_counter()
    # Very important: get the final remaining text.
    final_result = json.loads(recognizer.FinalResult())
    final_raw_text = final_result.get("text", "")
    duration = end_time - start_time
    return final_raw_text, duration