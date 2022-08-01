# Take N integers as input, and store in list (keep reading till user types "end")
list_of_num = []
while True:
    input_text = input("Enter value :")
    if input_text == "end":
        break
    converted_val = int(input_text) # TBD : validation
    list_of_num.append(converted_val)

print(list_of_num)