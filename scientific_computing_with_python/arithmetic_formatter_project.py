def arithmetic_arranger(problems, show_answers=False):
    # Check for more than 5 probems
    if len(problems) > 5:
        return "Error: Too many problems."

    # Creating list to format problems
    top_lines = []
    bottom_lines = []
    dash_lines = []
    result_lines = []
    
    for problem in problems:
        # Split the problem into 3 parts

        parts = problem.split()
        if len(parts) != 3:
            return "Error: Invalid problem format."
        
        operand1, operator, operand2 = parts
        
        # Validate operator
        if operator not in ['+', '-']:
            return "Error: Operator must be '+' or '-'."
        
        # Validate operands that contain only digits
        if not operand1.isdigit() or not operand2.isdigit():
            return "Error: Numbers must only contain digits."
        
        # Validate operand length, making sure its 4 or less numbers
        if len(operand1) > 4 or len(operand2) > 4:
            return "Error: Numbers cannot be more than four digits."
        
        # Calculate the result if needed based on the option in the func
        if show_answers:
            if operator == '+':
                result = str(int(operand1) + int(operand2))
            else:
                result = str(int(operand1) - int(operand2))
        
        # Width needed for alignment
        max_width = max(len(operand1), len(operand2)) + 2
        
        # Build each line - making them right aligned
        top_lines.append(operand1.rjust(max_width))
        bottom_lines.append(operator + ' ' + operand2.rjust(max_width - 2))
        dash_lines.append('-' * max_width)
        
        if show_answers:
            result_lines.append(result.rjust(max_width))
    
    # Combine all lines with 4 spaces between problems
    arranged_problems = '    '.join(top_lines) + '\n'
    arranged_problems += '    '.join(bottom_lines) + '\n'
    arranged_problems += '    '.join(dash_lines)
    
    if show_answers:
        arranged_problems += '\n' + '    '.join(result_lines)
    
    return arranged_problems
