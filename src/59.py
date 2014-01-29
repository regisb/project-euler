from collections import defaultdict

def get_periodical_numbers(numbers, start_index, period):
    filtered = []
    while start_index < len(numbers):
        filtered.append(numbers[start_index])
        start_index += period
    return filtered

def most_frequent_element(elements):
    max_count = 0
    count = defaultdict(int)
    most_frequent_element = None
    for element in elements:
        count[element] += 1
        if count[element] > max_count:
            max_count = count[element]
            most_frequent_element = element
    return most_frequent_element

def decrypt(numbers, keys):
    key_count = len(keys)
    text = ""
    for index, number in enumerate(numbers):
        key = keys[index % key_count]
        text += chr(key^number)
    return text

if __name__ == "__main__":
    text = open("cipher1.txt").read()
    numbers = map(int, text.split(","))
    keys = []
    for i in range(0, 3):
        filtered = get_periodical_numbers(numbers, i, 3)
        frequent_code = most_frequent_element(filtered)
        for key in range(ord('a'), ord('z') + 1):
            if key^frequent_code == ord("e") or key^frequent_code == ord("a") or key^frequent_code == ord(" "):
                break
        print chr(key)
        keys.append(key)
    text = decrypt(numbers, keys)
    print text
    print sum(map(ord, text))
