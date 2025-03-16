def set_goal():
    goal = float(input("Set your goal (e.g., running miles): "))
    return goal

def track_progress(goal):
    total_miles = 0.0

    while total_miles < goal:
        print(f"Total Miles Run: {total_miles:.2f}")
        miles_run = float(input("Enter miles run today (0 to quit): "))

        if miles_run == 0:
            break

        total_miles += miles_run
        if total_miles >= goal:
            print("Congratulations! You've reached your goal.")
            break

    print(f"Goal: {goal} miles")
    print(f"Total Miles Run: {total_miles:.2f}")
    print("Progress: {:.2f}%".format((total_miles / goal) * 100))

def main():
    print("Goal Tracker Program")
    user_goal = set_goal()
    track_progress(user_goal)

if __name__ == "__main__":
    main()
