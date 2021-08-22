def function(*args, **kwargs):
    for items in args:
        print(items)
    for key, value in kwargs.items():
        print(f"{key} is a {value}")


ls = ["Harry", "Marry", "Carry", "Larry"]
dt = {"Harry": "Monitor", "Marry": "Coordinator", "Carry": "Sports Teacher", "Larry": "Instructor"}
function(*ls, **dt)
