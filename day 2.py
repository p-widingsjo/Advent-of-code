# Getting data
with open('input_d02.txt') as file:
    rounds = [i.replace(" ", "") for i in file.read().strip().split("\n")]

results = {
    "AX":4, "AY":8, "AZ":3, 
    "BX":1, "BY":5, "BZ":9, 
    "CX":7, "CY":2, "CZ":6 
}


total_score_p1 = 0
for round in rounds:
    total_score_p1 += results[round]


# DESIRED results
# Changed the values of the results depending on the rules
# X = LOSS, Y = DRAW, Z = WIN
# (got values looking at table above)
desired_results = {
    "AX":3, "AY":4, "AZ":8, 
    "BX":1, "BY":5, "BZ":9, 
    "CX":2, "CY":6, "CZ":7 
}

total_score_p2 = 0
for round in rounds:
    total_score_p2 += desired_results[round]

# Answers
print("Answer to part 1: ", total_score_p1)
print("Answer to part 2: ", total_score_p2)