# Tuple immutability
Task_4=( 10,20,30, 10.5, 100)
try:
    Task_4[0] = 15 
except TypeError as e:
    print(f"Error: {e}")