# Quiz App - Tutorial for Learn IT

# Questions and possible answers as well as the define for which answer is correct. Make note of the formatting and placement of symbols
questions = [
    {
        "question": "What is the capital of Greece?",
        "options": ['A: Athens', 'B: London', 'C: Berlin', 'D: Madrid'],
        "answer": "A"
    },
    {
        "question": "What is the capital of the UK?",
        "options": ['A: Paris', 'B: London', 'C: Berlin', 'D: Madrid'],
        "answer": "B"
    },
    {
        "question": "What is the capital of Ecuador?",
        "options": ['A: Paris', 'B: London', 'C: Quito', 'D: Madrid'],
        "answer": "C"
    },
    {
        "question": "What is the capital of Sweden?",
        "options": ['A: Paris', 'B: London', 'C: Stockholm', 'D: Madrid'],
        "answer": "C"
    },
    {
        "question": "What is the capital of Italy?",
        "options": ['A: Paris', 'B: London', 'C: Berlin', 'D: Rome'],
        "answer": "D"
    },
    # You can remove this comment or move it down and add more questions. You should enclose each question in their own {} brackets.
]

# This function will define the quiz code on launch
def run_quiz(questions):
    score = 0  # Initialize score to 0 and create a variable "score" to store the value of correct answers

    # Loop through all the questions. This will follow all the questions above until finished
    for question in questions:
        print("\n" + question["question"])  # Print the question
        for option in question["options"]:
            print(option)  # Print all the answer options

        # Get the user's answer
        user_answer = input("Enter your answer (A, B, C, or D): ").strip().upper()

        # Check if the user's answer is correct
        if user_answer == question["answer"]:
            print("Correct!")
            score += 1  # Increment score if correct
        else:
            print("Wrong answer.")

    # Print the final score from the stored variable
    print(f"\nYou got {score} out of {len(questions)} questions correct!")

# Run the quiz
run_quiz(questions)