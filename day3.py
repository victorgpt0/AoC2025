joltages = []

with open("day3-input", "r", encoding="utf-8") as file:
    for line in file:
        print(line.strip(), end='\n')
        line = int(line.strip())
        digits = []
        while line: # extract digits from whole number
            digits.append(line % 10)
            line //= 10
        digits.reverse()

        print(digits)

        # Task 1
        # # use suffix_max scan to find largest two-digit number
        # suffix_max = [0] * (len(digits))
        # max_so_far = -1

        # # fill suffix_max array from right to left
        # for d in range(len(digits)-1, -1, -1):
        #     if digits[d] > max_so_far:
        #         max_so_far = digits[d]
        #     suffix_max[d] = max_so_far
    
        # print("suffix_max:", suffix_max)

        # joltage = -1

        # # for each digit, combine with max digit to the right
        # for i in range(0, len(digits)-1):
        #     right_digit = suffix_max[i+1]
        #     n = digits[i] * (10) + right_digit
        #     if n > joltage:
        #         joltage = n

        # joltages.append((joltage))

        # Task 2
        result = []
        start = 0
        for pick in range(12):
            # allowed search window size decreases as we pick more digits
            end_exclusive = len(digits) - (12-pick) + 1
            window = digits[start:end_exclusive]
            max_digit = max(window)
            result.append(max_digit)
            start += window.index(max_digit) + 1 # next pick must come after this index
        
        joltage = int(''.join(str(d) for d in result)) # combine digits into whole number
        joltages.append(joltage)

print("joltages:", joltages, "sum:", sum(joltages))

