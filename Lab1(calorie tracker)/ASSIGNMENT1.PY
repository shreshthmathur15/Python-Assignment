import datetime
import os

#CALORIE CHART

calorie_chart = {
    "Egg": 78,
    "Rice": 200,
    "Roti": 120,
    "Dal": 180,
    "Paneer": 265,
    "Chicken": 165,
    "Apple": 95,
    "Banana": 105,
    "Milk": 150,
}



#INTERFACE

print("\n" + "="*60)
print("🌟✨ DAILY CALORIE TRACKER CLI ✨🌟".center(60))
print("="*60)
print(r"""
      🥗   🍎   🍔   🍕   🥚   🍗   🥛
   Track your meals, count your calories, 
     and stay within your daily goals!  
""")
print("="*60 + "\n")




#INPUT DATA

meals = []
calories = []

num_meals = int(input("👉 How many meals do you want to enter today? "))

for i in range(num_meals):
    meal_name = input(f"\nEnter meal {i+1} name 🍽️ : ").capitalize()

    while True:
        choice = input(f"Enter calories for {meal_name} OR press 'c' to see chart 🔥: ").lower()
        
        if choice == 'c':
            print("\n📖 Food Calorie Chart:")
            print("-"*40)
            for food, cal in calorie_chart.items():
                print(f"{food:<25} {cal} cal")
            print("-"*40)
        else:
            try:
                cal_amount = float(choice)
                break
            except ValueError:
                print("Invalid input. Enter a number or press 'c' to check chart.")
    
    meals.append(meal_name)
    calories.append(cal_amount)




#CALCULATION OF CALORIES

total_calories = sum(calories)
avg_calories = total_calories / len(calories)

daily_limit = float(input("\n Enter your daily calorie limit: "))

if total_calories > daily_limit:
    status_msg = f"You exceeded your limit by {total_calories - daily_limit:.2f} calories!"
else:
    status_msg = f"Great! You are within your limit. You have {daily_limit - total_calories:.2f} calories left."




#OUTPUT

print("\n" + "="*60)
print("📊 DAILY CALORIE SUMMARY 📊".center(60))
print("="*60)

print(f"{'Meal Name':<25}{'Calories'}")
print("-"*60)
for meal, cal in zip(meals, calories):
    print(f"{meal:<25}{cal}")
print("-"*60)
print(f"{'TOTAL':<25}{total_calories}")
print(f"{'AVERAGE':<25}{avg_calories:.2f}")
print("-"*60)
print(status_msg)
print("="*60)


#SAVE FOR SESSION

save_choice = input("\n💾 Do you want to save this session log? (yes/no): ").lower()

if save_choice == "yes":
    timestamp = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    filename = f"calorie_log_{timestamp}.txt"
    
    with open(filename, "w", encoding="utf-8") as f:
        f.write("="*60 + "\n")
        f.write(f"Calorie Tracker Log - {timestamp}\n")
        f.write("="*60 + "\n")
        f.write(f"{'Meal Name':<25}{'Calories'}\n")
        f.write("-"*60 + "\n")
        for meal, cal in zip(meals, calories):
            f.write(f"{meal:<25}{cal}\n")
        f.write("-"*60 + "\n")
        f.write(f"{'TOTAL':<25}{total_calories}\n")
        f.write(f"{'AVERAGE':<25}{avg_calories:.2f}\n")
        f.write(status_msg + "\n")
        f.write("="*60 + "\n")
    
    print(f"\n✅ Session saved successfully as '{filename}'.")


