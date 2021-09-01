"""Inputing two numbers to complete mathematical operations"""

left = input("Left-hand side: ")
right = input("Right-hand side: ")
left_int = int(left)
right_int = int(right)
result = int(left_int ** right_int)
result0 = int(left_int / right_int)
result1 = int(left_int // right_int)
result2 = int(left_int % right_int)
print("left, ** , right, is ,result")
print("left, / , right, is, result0")
print("left, //, right, is, result1")
print("left, %, right ,is, result2")

_author_ = "730395174"