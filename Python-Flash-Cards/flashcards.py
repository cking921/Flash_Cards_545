from func import read_student_names, read_bash_dictionaries, combine_dictionaries


# Gather and clean data
student_names = read_student_names()
dictionaries = read_bash_dictionaries()
all_dictionaries = combine_dictionaries(student_names, dictionaries)

# Find and show top 3 largest dictionaries (ties included)
print("Largest dictionaries:")
words_per_student = all_dictionaries.groupby("student_name").agg({"command": "count"})
words_per_student.columns = ["count"]
words_per_student["rank"] = words_per_student["count"].rank(method="min").astype(int)

top_3_largest = words_per_student[words_per_student["rank"] <= 3]
print(top_3_largest[["rank", "count"]].sort_values("rank"))


user_points = 0
strikes = 0

# print out descriptions and pause for user input to simulate flashcards
while True:
    # pull one random row and simplify its pieces to a string
    row = all_dictionaries.sample(1)
    command = row["command"].values[0]
    description = row["description"].values[0]

    print("What bash command relates to the below description?\n")
    print(f"{description}\n")

    user_response = input("(enter to reveal answer; 'quit' to exit)")
    if user_response == command:
        user_points = user_points + 1
        print(f"Correct! You currently have {user_points} points\n")
        continue
    else:
        print(f"Wrong! The correct answer is {command}\n")
        strikes = strikes + 1
        if strikes == 3:
            print("You're out!\n")
            break
    if user_response == "quit":
        break

    
