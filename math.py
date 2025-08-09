import random
import time

operators = ['+', '-', '*']
min_operand = 3
max_operand = 12
total = 10

def generate():
    left = random.randint(min_operand, max_operand)
    right = random.randint(min_operand, max_operand)
    operator = random.choice(operators)
    expr = f"{left} {operator} {right}"
    answer = eval(expr)
    return expr, answer

wrong = 0
input("Press Enter to start...")
print("____________")

start = time.time()

for i in range(total):
    expr, answer = generate()
    while True:
        guess = input(f"Problem #{i+1}: {expr} = ")
        try:
            if int(guess) == answer:
                break
            else:
                wrong += 1
                print("Incorrect, try again!")
        except ValueError:
            print("Please enter a number.")

end = time.time()
total_time = end - start

print("____________")
print(f"NICE WORK! Finished in {total_time:.2f} seconds with {wrong} wrong attempt(s).")
