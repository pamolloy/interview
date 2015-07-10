#!/usr/bin/env python
#
#   sum-depth-nested-list/solution.py
#

# Examples consisting of the list and output
examples = [
    ([[1, 1], 2, [1, 1]], 10),
    ([1, [4, [6]]], 27)
]

def sum_depth(nested_list, depth=0):
    """A recursive solution that sums the product of multiplying each element
       by its depth"""

    total = 0

    if type(nested_list) is int:
        return depth * nested_list
    else:
        for ele in nested_list:
            total += sum_depth(ele, depth+1)

    return total

if __name__ == "__main__":
    for solve in [sum_depth]:
        print("Solution: {name}\n{doc}\n".format(
                name=solve.__name__, doc=solve.__doc__))
        for example, solution in examples:
            try:
                result = solve(example)
                message = "Example: {example}\nResult: {result}\nSolution: {solution}".format(
                        example=example, result=result, solution=solution)
                assert solution == result
                print("{0}\nSUCCESS\n".format(message))
            except AssertionError:
                print("{0}\nFAILURE\n".format(message))

