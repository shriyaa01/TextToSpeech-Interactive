import os

# Function to convert text to speech using PowerShell and .NET Framework
def say(text):
    os.system(f'PowerShell -Command "Add-Type -AssemblyName System.Speech; (New-Object System.Speech.Synthesis.SpeechSynthesizer).Speak(\'{text}\')"')

# Continuous loop for user interaction
while True:
    # Prompt the user to input text
    x = input("What do you want me to say? ")
    
    # Check if the user wants to quit
    if x == "quit":
        # Say "Namaste" before exiting
        say("Namaste")
        # Exit the loop
        break
    
    # Convert the user's input to speech
    say(x)

