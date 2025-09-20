

class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        # Define a function to calculate the result of the given operator between two numbers
        def calc(left, right, operator):
            if operator == '+':
                return left + right
            elif operator == '-':
                return left - right
            elif operator == '*':
                return left * right

        # Define the main function to calculate all possible results
        def diffWaysToComputeHelper(inputStr):

            # If the input string only has digits, return a list with that number
            if inputStr.isdigit():
                return [int(inputStr)]

            # Initialize the output list
            outputList = []

            # Iterate through each character of the input string and check if it is an operator or not
            for i in range(len(inputStr)):
                if inputStr[i] in ['+', '-', '*']:

                    # Recursively call the `diffWaysToCompute()` function for the left and right substrings of the operator
                    leftResults = diffWaysToComputeHelper(inputStr[:i])
                    rightResults = diffWaysToComputeHelper(inputStr[i + 1:])

                    # Combine the results using the operator
                    for left in leftResults:
                        for right in rightResults:
                            outputList.append(calc(left, right, inputStr[i]))

            # Return the output list
            return outputList

        # Call the helper function
        return diffWaysToComputeHelper(inputStr)