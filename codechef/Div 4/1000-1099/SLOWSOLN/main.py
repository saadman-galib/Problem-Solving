t = int(input())

for _ in range(t):
    maxT, maxN, sumN = map(int, input().split())
    result = 0

    while(True):
        if sumN <= maxN:
            break
        else:

            result += maxN ** 2
            sumN -= maxN
        maxT -= 1
    
    print(result)



# # Function to find the maximum value of the expression
# def max_value(maxT, maxN, sumN):
#     # Initialize the result to zero
#     result = 0
#     # Loop from maxN to 1
#     for N in range(maxN, 0, -1):
#         # Calculate the number of test cases that can have this value of N
#         T = min(maxT, sumN // N)
#         # Update the result with the value of the expression for these test cases
#         result += T * (N ** 2)
#         # Update the remaining number of test cases and sum of N
#         maxT -= T
#         sumN -= T * N
#         # If there are no more test cases or sum of N left, break the loop
#         if maxT == 0 or sumN == 0:
#             break
#     # Return the result
#     return result

# # Read the number of test cases
# T = int(input())
# # Loop for each test case
# for _ in range(T):
#     # Read the values of maxT, maxN, and sumN
#     maxT, maxN, sumN = map(int, input().split())
#     # Find and print the maximum value of the expression
#     print(max_value(maxT, maxN, sumN))


# not solved
