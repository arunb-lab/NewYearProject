marks = {
    "Aarav": 85,
    "Nisha": 92,
    "Bibek": 78
}

topper = max(marks, key=marks.get)
print("Topper:", topper, "with", marks[topper])
