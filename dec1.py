file_path = "/Users/iananderson/Desktop/adventofcode2023/input.txt"
sum = 0
with open(file_path, 'r') as file:
    for line in file:
        original_string = line.strip()
        numbers_only_string = "".join([i for i in original_string if i.isdigit()])
        first_digit = numbers_only_string[0]
        last_digit = numbers_only_string[-1]
        answer = first_digit + last_digit
        #print(answer)
        sum = sum + int(answer)

print(sum)