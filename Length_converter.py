start_length = float(input("Starting Length in your unit without the letters: "))
print("Type in the corresponding letter for each unit: K for Kilometers, M for Miles, ME for Meters and F for feet")
starting_unit = input("Starting Unit: ").lower()
final_unit = input("To what unit would you like to convert to?: ").lower()

if (starting_unit == "k" or starting_unit == "kilometers") and (final_unit == "m" or final_unit == "miles"):
    result = start_length / 1.609
    print(f"{start_length} kilometers is equal to {round(result, 2)} miles.")
elif (starting_unit == "k" or starting_unit == "kilometers") and (final_unit == "f" or final_unit == "feet"):
    result = start_length * 3280.84
    print(f"{start_length} kilometers is equal to {round(result, 2)} feet.")
elif (starting_unit == "k" or starting_unit == "kilometers") and (final_unit == "me" or final_unit == "meters"):
    result = start_length * 1000
    print(f"{start_length} kilometers is equal to {round(result, 2)} meters.")

elif (starting_unit == "m" or starting_unit == "miles") and (final_unit == "k" or final_unit == "kilometers"):
    result = start_length * 1.60934
    print(f"{start_length} miles is equal to {round(result, 2)} kilometers.")
elif (starting_unit == "m" or starting_unit == "miles") and (final_unit == "f" or final_unit == "feet"):
    result = start_length * 5280
    print(f"{start_length} miles is equal to {round(result, 2)} feet.")
elif (starting_unit == "m" or starting_unit == "miles") and (final_unit == "me" or final_unit == "meters"):
    result = start_length * 1609.34
    print(f"{start_length} miles is equal to {round(result, 2)} meters.")

elif (starting_unit == "me" or starting_unit == "meters") and (final_unit == "k" or final_unit == "kilometers"):
    result = start_length / 1000
    print(f"{start_length} meters is equal to {round(result, 2)} kilometers.")
elif (starting_unit == "me" or starting_unit == "meters") and (final_unit == "m" or final_unit == "miles"):
    result = start_length / 1609
    print(f"{start_length} meters is equal to {round(result, 2)} miles.")
elif (starting_unit == "me" or starting_unit == "meters") and (final_unit == "f" or final_unit == "feet"):
    result = start_length * 3.28084
    print(f"{start_length} meters is equal to {round(result, 2)} feet.")

elif (starting_unit == "f" or starting_unit == "feet") and (final_unit == "me" or final_unit == "meters"):
    result = start_length / 3.28084
    print(f"{start_length} feet is equal to {round(result, 2)} meters.")
elif (starting_unit == "f" or starting_unit == "feet") and (final_unit == "k" or final_unit == "kilometers"):
    result = start_length / 3281
    print(f"{start_length} feet is equal to {round(result, 2)} kilometers.")
elif (starting_unit == "f" or starting_unit == "feet") and (final_unit == "m" or final_unit == "miles"):
    result = start_length / 5280
    print(f"{start_length} feet is equal to {round(result, 2)} miles.")
