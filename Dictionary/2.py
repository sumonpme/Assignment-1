# Accessing dictionary values using their keys
Task_1 = {"name": "Ahmed","age": 30,"course": "mining engineering"}
print("Created dictionary:" , Task_1)
name=Task_1["name"]
age=Task_1.get("age")
print("Name", name)
print("Age", age)