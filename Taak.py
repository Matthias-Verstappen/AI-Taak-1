import streamlit as st
from itertools import permutations

# Function to solve the cryptarithmetic puzzle
def solve_cryptarithmetic(first_factor, second_factor, result, operation):
    # Combine all three parts into a single puzzle with the selected operation
    if operation == "+":
        puzzle = f"{first_factor} + {second_factor} = {result}"
    elif operation == "-":
        puzzle = f"{first_factor} - {second_factor} = {result}"
    elif operation == "*":
        puzzle = f"{first_factor} * {second_factor} = {result}"
    elif operation == "/":
        puzzle = f"{first_factor} / {second_factor} = {result}"
    else:
        return None  # Unsupported operation

    # Extract unique letters from the puzzle
    letters = set(filter(str.isalpha, puzzle))

    # Generate permutations of digits for the letters (0-9)
    digit_permutations = permutations(range(10), len(letters))

    # Checks every expression created in the map to see if it is correct
    # The map contains a dictionary with the key-value pairs of letters and numbers
    for perm in digit_permutations:
        digit_map = dict(zip(letters, perm))
        if evaluate_expression(puzzle, digit_map, operation):
            return digit_map

    return None

# Function to evaluate the expression with the digit mapping
def evaluate_expression(expression, digit_map, operation):
    # Replace letters with digits from the digit_map in the expression, this way it becomes a mathematical expression instead of words
    for letter, digit in digit_map.items():
        expression = expression.replace(letter, str(digit))

    # Split the expression into operands and evaluate based on the selected operation, strip off whitespace
    left_operand, right_operand = expression.split('=')
    left_operand = left_operand.strip()
    right_operand = right_operand.strip()

    # Check if the mathematical expression is correct, if so, return True
    try:
        if operation == "+":
            return eval(left_operand) == eval(right_operand)
        elif operation == "-":
            return eval(left_operand) == eval(right_operand)
        elif operation == "*":
            return eval(left_operand) == eval(right_operand)
        elif operation == "/":
            return eval(left_operand) == eval(right_operand)
        else:
            return False
    except:
        return False

# Custom function to format the equation with values
def format_equation_with_values(first_factor, second_factor, result, operation, solution):
    formatted_equation = ""
    if operation == "+":
        first_number = "".join([str(solution[char]) for char in first_factor])
        second_number = "".join([str(solution[char]) for char in second_factor])
        result_number = "".join([str(solution[char]) for char in result])
        formatted_equation = f"{first_number} + {second_number} = {result_number}"
    elif operation == "-":
        formatted_equation = f"{solution[first_factor[0]]}{solution[first_factor[1]]} - {solution[second_factor[0]]}{solution[second_factor[1]]} = {solution[result[0]]}{solution[result[1]]}{solution[result[2]]}"
    elif operation == "*":
        first_number = "".join([str(solution[char]) for char in first_factor])
        second_number = "".join([str(solution[char]) for char in second_factor])
        result_number = "".join([str(solution[char]) for char in result])
        formatted_equation = f"{first_number} * {second_number} = {result_number}"
    elif operation == "/":
        formatted_equation = f"{solution[first_factor[0]]}{solution[first_factor[1]]} / {solution[second_factor[0]]}{solution[second_factor[1]]} = {solution[result[0]]}{solution[result[1]]}{solution[result[2]]}{solution[result[3]]}"
    return formatted_equation

# Streamlit UI
st.title("Cryptarithmetic Puzzle Solver")

first_factor = st.text_input("Enter the first factor (e.g., 'TO'):")
second_factor = st.text_input("Enter the second factor (e.g., 'GO'):")
result = st.text_input("Enter the result (e.g., 'OUT'):")
operation = st.selectbox("Select the arithmetic operation:", ["+", "-", "*", "/"])

if st.button("Solve Puzzle"):
    if not first_factor or not second_factor or not result:
        st.error("Please enter all three parts of the puzzle.")
    elif operation not in ["+", "-", "*", "/"]:
        st.error("Please select a valid arithmetic operation.")
    else:
        solution = solve_cryptarithmetic(first_factor, second_factor, result, operation)

        if solution:
            st.success("Solution found:")

            # Format the equation with values from the solution
            formatted_equation = format_equation_with_values(first_factor, second_factor, result, operation, solution)

            # Display the equation as it was filled in
            st.write(f"{first_factor} {operation} {second_factor} = {result}")

            # Display the formatted equation with numbers filled in
            st.write(f"{formatted_equation}")

            # Display the letter-number pairs
            st.write(f"Letter-Number Mapping:")
            for letter, digit in solution.items():
                st.write(f"{letter} = {digit}")
        else:
            st.error("No solution found.")
