import tkinter as tk
from tkinter import messagebox
import datetime

# Colors - Light dual shade pink and white
BG_COLOR = "#FFF0F5"
LIGHT_PINK = "#FFB6C1"
MEDIUM_PINK = "#FF91A4"
DARK_PINK = "#E75480"
WHITE = "#FFFFFF"
SOFT_WHITE = "#FFF8FA"

# Main window
window = tk.Tk()
window.title("🌸 Sakhi — Your Health Companion")
window.geometry("480x620")
window.configure(bg=BG_COLOR)
window.resizable(False, False)

# Title
title_label = tk.Label(
    window,
    text="🌸 SAKHI",
    font=("Georgia", 32, "bold italic"),
    bg=BG_COLOR,
    fg=DARK_PINK
)
title_label.pack(pady=10)

subtitle_label = tk.Label(
    window,
    text="Your Personal Health Companion",
    font=("Georgia", 11, "italic"),
    bg=BG_COLOR,
    fg=MEDIUM_PINK
)
subtitle_label.pack()

# Separator
separator = tk.Frame(window, height=2, bg=LIGHT_PINK)
separator.pack(fill="x", padx=20, pady=10)

# Period date input
date_label = tk.Label(
    window,
    text="Enter your last period date:",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=DARK_PINK
)
date_label.pack(pady=5)

date_entry = tk.Entry(
    window,
    font=("Arial", 12),
    width=20,
    justify="center",
    bg=SOFT_WHITE,
    fg=DARK_PINK,
    relief="solid",
    bd=1
)
date_entry.insert(0, "dd-mm-yyyy")
date_entry.pack(pady=5)

# Result frame
result_frame = tk.Frame(
    window,
    bg=SOFT_WHITE,
    bd=1,
    relief="solid"
)
result_frame.pack(padx=20, pady=10, fill="x")

next_period_label = tk.Label(
    result_frame,
    text="Next Period: --",
    font=("Arial", 11, "bold"),
    bg=SOFT_WHITE,
    fg=DARK_PINK
)
next_period_label.pack(pady=5)

days_label = tk.Label(
    result_frame,
    text="Days Remaining: --",
    font=("Arial", 11),
    bg=SOFT_WHITE,
    fg=MEDIUM_PINK
)
days_label.pack(pady=5)

# Mood selection
mood_label = tk.Label(
    window,
    text="How are you feeling today? 💭",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=DARK_PINK
)
mood_label.pack(pady=5)

mood_var = tk.StringVar(value="Happy 😊")
moods = ["Happy 😊", "Sad 😔", "Anxious 😰", "Tired 😴", "Normal 😐"]

mood_frame = tk.Frame(window, bg=BG_COLOR)
mood_frame.pack()

for mood in moods:
    tk.Radiobutton(
        mood_frame,
        text=mood,
        variable=mood_var,
        value=mood,
        bg=BG_COLOR,
        fg=DARK_PINK,
        selectcolor=LIGHT_PINK,
        activebackground=BG_COLOR,
        font=("Arial", 10)
    ).pack(side="left", padx=5)

# Separator 2
separator2 = tk.Frame(window, height=1, bg=LIGHT_PINK)
separator2.pack(fill="x", padx=20, pady=8)

# Symptom selection
symptom_label = tk.Label(
    window,
    text="Any symptoms today? 🌡️",
    font=("Arial", 11, "bold"),
    bg=BG_COLOR,
    fg=DARK_PINK
)
symptom_label.pack(pady=5)

symptom_var = tk.StringVar(value="No symptoms")
symptoms = ["Cramps", "Headache", "Bloating", "Back pain", "No symptoms"]

symptom_frame = tk.Frame(window, bg=BG_COLOR)
symptom_frame.pack()

for symptom in symptoms:
    tk.Radiobutton(
        symptom_frame,
        text=symptom,
        variable=symptom_var,
        value=symptom,
        bg=BG_COLOR,
        fg=DARK_PINK,
        selectcolor=LIGHT_PINK,
        activebackground=BG_COLOR,
        font=("Arial", 10)
    ).pack(side="left", padx=3)

# Separator 3
separator3 = tk.Frame(window, height=1, bg=LIGHT_PINK)
separator3.pack(fill="x", padx=20, pady=8)

# Calculate function
def calculate():
    try:
        date_input = date_entry.get()
        last_period = datetime.datetime.strptime(date_input, "%d-%m-%Y")
        next_period = last_period + datetime.timedelta(days=28)
        today = datetime.date.today()
        days_remaining = (next_period.date() - today).days

        next_period_label.config(
            text=f"🌸 Next Period: {next_period.strftime('%d %B %Y')}"
        )
        days_label.config(
            text=f"⏳ Days Remaining: {days_remaining} days"
        )
    except:
        messagebox.showerror(
            "Oops!!",
            "Please enter date in dd-mm-yyyy format!!\nExample: 16-05-2026"
        )

# Save function
def save_log():
    try:
        today = datetime.date.today()
        with open("sakhi_log.txt", "a") as file:
            file.write(f"\n--- {today} ---\n")
            file.write(f"Mood: {mood_var.get()}\n")
            file.write(f"Symptom: {symptom_var.get()}\n")
        messagebox.showinfo(
            "Saved!! 🌸",
            "Your data has been saved successfully!!\nTake care of yourself!! 💕"
        )
    except:
        messagebox.showerror("Error", "Something went wrong!! Please try again!!")

# Button frame
button_frame = tk.Frame(window, bg=BG_COLOR)
button_frame.pack(pady=10)

# Calculate button
calculate_btn = tk.Button(
    button_frame,
    text="Calculate Next Period 🔮",
    font=("Arial", 12, "bold"),
    bg=MEDIUM_PINK,
    fg=WHITE,
    activebackground=DARK_PINK,
    activeforeground=WHITE,
    padx=15,
    pady=8,
    border=0,
    cursor="hand2",
    command=calculate
)
calculate_btn.pack(side="left", padx=10)

# Save button
save_btn = tk.Button(
    button_frame,
    text="Save Today's Log 💾",
    font=("Arial", 12, "bold"),
    bg=LIGHT_PINK,
    fg=DARK_PINK,
    activebackground=MEDIUM_PINK,
    activeforeground=WHITE,
    padx=15,
    pady=8,
    border=0,
    cursor="hand2",
    command=save_log
)
save_btn.pack(side="left", padx=10)

# Footer
footer = tk.Label(
    window,
    text="Made with 💕 by Navya — for every woman",
    font=("Georgia", 9, "italic"),
    bg=BG_COLOR,
    fg=LIGHT_PINK
)
footer.pack(pady=10)

# Run window
window.mainloop()