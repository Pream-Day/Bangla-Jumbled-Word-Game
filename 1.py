import tkinter as tk
import random

# Bangla jumbled words and their correct answers
jumbled_words = {
    'রামআ': 'আমরা',
    'বালাং': 'বাংলা',
    'তেখে': 'খেতে',
    'পেআল': 'আপেল',
    'মকলা': 'কমলা',
    'রাপেয়া': 'পেয়ারা',
    'মআ': 'আম',
     
    
}

# Function to shuffle a word
def shuffle_word(word):
    word_list = list(word)
    random.shuffle(word_list)
    return ''.join(word_list)

# Function to check if the entered word is correct
def check_word():
    entered_word = entry.get()
    current_jumbled_word = jumbled_words[current_word_label.cget("text")]
    
    if entered_word == current_jumbled_word:
        result_label.config(text="Correct!", fg="green")
    else:
        result_label.config(text="Incorrect!", fg="red")
    
    # Show the correct answer
    answer_label.config(text=f"Correct Answer: {current_jumbled_word}", fg="blue")

# Function to update the jumbled word
def update_word():
    word_list = list(jumbled_words.keys())
    random.shuffle(word_list)
    current_word = word_list[0]
    current_jumbled_word = shuffle_word(jumbled_words[current_word])
    current_word_label.config(text=current_word)
    entry.delete(0, tk.END)
    result_label.config(text="")
    answer_label.config(text="")

# Create the main window
root = tk.Tk()
root.title("Bangla Jumbled Word Game") 
root.configure(bg="lightblue")
root.geometry("500x500")

#App Name
name_label =tk.Label(root, text="বাংলা জাম্বলড ওয়ার্ড গেম",font=("Time New Roman", 20,"bold"))
name_label.place(x=25,y=30,height=50,width=450)


# word Labels
current_word_label = tk.Label(root, text="", font=("Time New Roman", 20), bg="lightblue")
current_word_label.place(x=25,y=100,height=50,width=450)

#entry labels
entry = tk.Entry(root, font=("Time New Roman", 14))
entry.place(x=150,y=150,height=50,width=200)

#result labels
result_label = tk.Label(root, text="", font=("Time New Roman", 16), fg="green", bg="lightblue")
result_label.place(x=100,y=250,height=20,width=300)

#answer labels
answer_label = tk.Label(root, text="", font=("Time New Roman", 16), bg="lightblue")
answer_label.place(x=100,y=270,height=50,width=300)

#Buttons
check_button = tk.Button(root, text="Check", command=check_word, font=("Time New Roman", 14), bg="green", fg="white")
check_button.place(x=180,y=350,height=50,width=120)


next_button = tk.Button(root, text="Next", command=update_word, font=("Time New Roman", 14), bg="blue", fg="white")
next_button.place(x=180,y=420,height=50,width=120)

# Initialize the game
update_word()

root.mainloop()
