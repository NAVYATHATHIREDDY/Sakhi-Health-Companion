import datetime
today = datetime.date.today()
date_input = input("Enter your periods date(dd-mm-yyyy): ")
last_period = datetime.datetime.strptime(date_input, "%d-%m-%Y")
next_period = last_period + datetime.timedelta(days=28)
print("Your next period may be in:-", next_period.date())
days_remaining = (next_period.date() - today).days
print("Remaining days left are:-", days_remaining)

# Mood logger:

print("\n--- How are you feeling today? ---")
print("1. Happy 😊")
print("2. Sad 😔")
print("3. Anxious 😰")
print("4. Tired 😴")
print("5. Normal 😐")

mood_choice = input("Enter your mood (1-5): ")

moods = {
    "1": "Happy 😊",
    "2": "Sad 😔", 
    "3": "Anxious 😰",
    "4": "Tired 😴",
    "5": "Normal 😐"
}

selected_mood = moods[mood_choice]
print("Today's mood logged:-", selected_mood)

# Symptoms logger
print("\n--- Any symptoms today? ---")
print("1. Cramps")
print("2. Headache")
print("3. Bloating")
print("4. Back pain")
print("5. No symptoms")

symptom_choice = input("Enter symptom number (1-5): ")

symptoms = {
    "1": "Cramps",
    "2": "Headache",
    "3": "Bloating",
    "4": "Back pain",
    "5": "No symptoms"
}

selected_symptom = symptoms[symptom_choice]
print("Today's symptom logged:-", selected_symptom)




with open("sakhi_log.txt", "a") as file:
    file.write(f"\n--- {today} ---\n")
    file.write(f"Last Period: {last_period.date()}\n")
    file.write(f"Next Period: {next_period.date()}\n")
    file.write(f"Days Remaining: {days_remaining}\n")
    file.write(f"Mood: {selected_mood}\n")
    file.write(f"Symptom: {selected_symptom}\n")

print("\nData saved to sakhi_log.txt!! ✅")
