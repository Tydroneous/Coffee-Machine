age = int(input())

if age <= 40:
    if age <= 16:
        print("Lion King")
    elif age <= 25:
        print("Trainspotting")
    else:
        print("Matrix")
else:
    if age <= 60:
        print("Pulp Fiction")
    else:
        print("Breakfast at Tiffany's")
