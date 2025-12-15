
first_bit = """*Below is my explanation for solving this daily challenge and below that is the original challenge in freeCodeCamp! Check the accompanying "solution.py" file for the actual solution code. I built the solution in the online IDE found at "https://www.programiz.com/python-programming/online-compiler/".*

****

***Explanation here!***

****"""

link = "paste-link-here"
problem = """paste-problem-here"""
solutions = """paste-solutions-here"""

# ALL THE LOGIC OR WHATEVER
problem = problem.split("\n")
linked_line = f"## [{problem[0]}]({link})"
problem[0] = linked_line+"\n"
new_problem = ''
for item in problem:
    new_problem+=(item+"\n")
divider = "****"
solutions = solutions.split("\n")
solution_result = ""

for line in solutions:
    new_line = f"    {line[7:]}\n"
    solution_result+=new_line

# THE OUTPUT!!!
output = first_bit+"\n"+new_problem+"\n"+divider+"\n"+solution_result
print(output)
