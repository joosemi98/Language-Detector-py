# Language Detector App

#A simple Python GUI application to detect the language of the input text using the `langdetect` and `langcodes` libraries.

## Características

## Graphical user interface (GUI) with `tkinter`.
## Real-time language detection.
## Error handling 


import language_data

import tkinter as tk
from tkinter import Label, Entry, Button
from langdetect import detect
from langcodes import Language



# Define the main class of the application
class LanguageDetectorApp:
    def __init__(self, master):
        self.master = master
        master.title("Language Detector") # Set the title of the window

        # Create and place a label for the input text
        self.label = Label(master, text="Enter text:")
        self.label.pack()

         # Create and place a text entry field
        self.text_entry = Entry(master, width=40)
        self.text_entry.pack()

        # Create and place a button to detect the language
        self.detect_button = Button(master, text="Detect Language", command=self.detect_language)
        self.detect_button.pack()

                
        # Create and place a label to display the result
        self.result_label = Label(master, text="")
        self.result_label.pack()

    # Define the method to detect the language
    def detect_language(self):
        input_text = self.text_entry.get()

        if input_text.strip():  # Check if the input text is not empty or just whitespace
            try:
                language_code = detect(input_text)
                language_name = Language.get(language_code).display_name('en')  # Specify the language for display name
                self.result_label.config(text=f"The detected language is: {language_name}")
            except Exception as e:
                self.result_label.config(text=f"Error during language detection: {e}")
        else:
            self.result_label.config(text="Please enter some text for language detection.")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageDetectorApp(root)
    root.mainloop()