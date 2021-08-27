"""numeric_operators trial 1."""

_author_ = 730319741

left_hand_side: int = int(input("Left-hand side: "))
right_hand_side: int = int(input("Right-hand side: "))
evaluation: int = int(left_hand_side ** right_hand_side)
print(str(left_hand_side) + " ** " + str(right_hand_side) + " is " + str(evaluation))
print(str(left_hand_side) + " / " + str(right_hand_side) + " is " + str(left_hand_side / right_hand_side))
print(str(left_hand_side) + " // " + str(right_hand_side) + " is " + str(left_hand_side // right_hand_side))
print(str(left_hand_side) + " % " + str(right_hand_side) + " is " + str(left_hand_side % right_hand_side))