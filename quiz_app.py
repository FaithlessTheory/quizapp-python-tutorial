# Quiz App - Tutorial for Learn IT

# Questions and possible answers as well as the define for which answer is correct. Make note of the formatting and placement of symbols
questions = [
    {
        "question": "What is the capital of Greece?",
        "options": ['A: Athens', 'B: Thessaloniki', 'C: Patras', 'D: Larissa'],
        "answer": "A"
    },
    {
        "question": "What is the capital of the UK?",
        "options": ['A: Manchester', 'B: London', 'C: Birmingham', 'D: Cardiff'],
        "answer": "B"
    },
    {
        "question": "What is the capital of Ecuador?",
        "options": ['A: Salinas', 'B: Guayaquil', 'C: Quito', 'D: Ambato'],
        "answer": "C"
    },
    {
        "question": "What is the capital of Sweden?",
        "options": ['A: Helsingborg', 'B: Malmö', 'C: Stockholm', 'D: Gothenburg'],
        "answer": "C"
    },
    {
        "question": "What is the capital of Italy?",
        "options": ['A: Paris', 'B: Naples', 'C: Vatican', 'D: Rome'],
        "answer": "D"
    },
    {
        "question": "What is the capital of the USA?",
        "options": ['A: New York', 'B: Seattle', 'C: LA', 'D: Washington DC'],
        "answer": "D"
    },
    {
        "question": "What is the capital of the France?",
        "options": ['A: Paris', 'B: Marseille', 'C: Lyon', 'D: Nantes'],
        "answer": "A"
    },
    {
        "question": "What is the capital of Germany?",
        "options": ['A: Berlin', 'B: Frankfurt', 'C: Dresden', 'D: Hamburg'],
        "answer": "A"
    },
    {
        "question": "What is the capital of Russia?",
        "options": ['A: St Petersburg', 'B: Tver', 'C: Moscow', 'D: Sochi'],
        "answer": "C"
    },
    {
        "question": "What is the capital of New Zealand?",
        "options": ['A: Auckland', 'B: Christchurch', 'C: Rotorua', 'D: Wellington'],
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