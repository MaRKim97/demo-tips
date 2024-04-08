import speech_recognition as sr

# Initialize recognizer class (for recognizing the speech)
recognizer = sr.Recognizer()

# Set up the microphone
with sr.Microphone() as source:
    print("Please wait. Calibrating microphone for 1 second!")
    # listen for 1 second and create the ambient noise energy level
    recognizer.adjust_for_ambient_noise(source, duration=1)
    print("Microphone is now listening for input up to 5 seconds")
    audio = recognizer.listen(source, phrase_time_limit=5)
    #audio = recognizer.listen(source)

    # Write audio to a WAV file
    with open("rec.wav", "wb") as f:
        f.write(audio.get_wav_data())

print("Audio has been saved as 'rec.wav'.")
