marks = {}

n = int(input("How many students? "))
for _ in range(n):
    name = input("Name: ")
    score = int(input("Marks: "))
    marks[name] = score

print("\nAll Marks:")
for name, score in marks.items():
    print(name, "->", score)
