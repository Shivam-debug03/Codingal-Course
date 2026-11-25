# ================================
# My Daily Mood Advisor
# ================================

import datetime

name = input("What is your name? ").strip()
mood = input(
    "How are you feeling today? Happy, sad, tired, stressed, or excited: "
).strip().lower()
energy = int(input("What is your energy level from 1 to 10? "))

# Mood advice
if mood == "happy":
    advice = "Keep spreading your positive energy!"
elif mood == "sad":
    advice = "Talk to someone you trust or do something you enjoy."
elif mood == "tired":
    advice = "Drink water, take a short break, and get some rest."
elif mood == "stressed":
    advice = "Try deep breathing or make a small to-do list."
elif mood == "excited":
    advice = "Use your excitement to start something creative!"
else:
    advice = "Every mood is okay. Take care of yourself today."

# Energy advice
if energy < 3:
    energy_advice = (
        "I am concerned because your energy is very low. "
        "Please drink some water, eat a healthy snack, rest for a little while, "
        "and avoid strenuous activities. If you still feel very tired, "
        "tell someone you trust and consider taking a proper break."
    )
elif energy <= 5:
    energy_advice = (
        "I am a little concerned about your energy level. "
        "Please take a short break, drink water, and try a light activity "
        "such as a walk or a few stretches."
    )
else:
    energy_advice = (
        "Great! You have plenty of energy today. Stay confident, "
        "work on a goal that matters to you, and turn this positive momentum "
        "into something useful. Remember to take small breaks and keep going!"
    )

today = datetime.datetime.now().strftime("%d %B %Y, %I:%M %p")

print("\n================================")
print("DAILY MOOD ADVISOR REPORT")
print("================================")
print("Name:", name)
print("Mood:", mood.title())
print("Energy Level:", energy)
print("Date and Time:", today)
print("Advice:", advice)
print("Energy Advice:", energy_advice)
print("================================")
