print("🖤 Discipline Tracker 🖤")

name = input("What do I call you? ")

score = 0
completed = []
skipped = []

positive_habits = [
    ("Workout", 2),
    ("Study", 2),
    ("Eat clean", 2),
    ("Sleep 7+ hours", 1)
]

negative_habits = [
    ("Binge junk food", -1),
    ("Waste time on social media", -1)
]

print(f"\nAlright {name}, let's check your discipline today.\n")

# Positive habits
for habit, points in positive_habits:
    answer = input(f"Did you {habit}? (y/n): ").lower()

    if answer == "y":
        score += points
        completed.append(habit)
        print(f"+{points} points!\n")
    else:
        skipped.append(habit)

# Negative habits
for habit, points in negative_habits:
    answer = input(f"Did you {habit}? (y/n): ").lower()

    if answer == "y":
        score += points
        skipped.append(habit)
        print(f"{points} points!\n")

# Custom habit
add_custom = input("\nDo you want to add a custom habit today? (y/n): ").lower()

if add_custom == "y":
    habit = input("Enter your habit: ")
    points = int(input("How many points is it worth? "))

    answer = input(f"Did you {habit}? (y/n): ").lower()

    if answer == "y":
        score += points
        completed.append(habit)

# Results
print("\n📊 Daily Summary")

print("\n✔ Completed habits:")
for habit in completed:
    print("-", habit)

print("\n✘ Skipped habits:")
for habit in skipped:
    print("-", habit)

print(f"\nYour Discipline Score: {score}")

# Rank system
if score <= 0:
    rank = "Lost Soul 💀"
elif score <= 3:
    rank = "Beginner 🌱"
elif score <= 5:
    rank = "Warrior ⚔️"
else:
    rank = "Elite Discipline 🔥"

print("Rank:", rank)

# Reflection
reflection = input("\nWhat is ONE thing you'll improve tomorrow? ")
print("Good. Improve daily. 🖤")