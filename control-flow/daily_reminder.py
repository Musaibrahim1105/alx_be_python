task = input("Enter your task: ")
priority = input("Priority (high/medium/low): ")
time_bound = input("Is it time-bound? (yes/no): ")

match priority:
    case "high":
        if time_bound == "yes":
           print(f"Reminder: '{task}' is a {priority} priority task that requires immediate attention today!")
        else:
           print(f"Reminder: '{task}' is a high priority task. Try to complete it as soon as possible.")
    case "medium":
        if time_bound == "yes":
           print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today!")
        else:
           print(f"Reminder: '{task}' is a medium priority task that requires immediate attention today! please complete it when you can")
    case "low":
        if time_bound == "yes":
           print(f"Note: '{task}' is a {priority} priority task. Consider completing it when you have free time.")
        else:
           print(f"Note: '{task}' is a low priority task. Consider completing it when you have free time.")
    case _:
        print("Invalid priority entered. Please choose high, medium, or low.")