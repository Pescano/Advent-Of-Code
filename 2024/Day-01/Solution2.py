def calculate_result(dictionary, list1):
    result = 0
    for i in range(len(list1)):
        if list1[i] in dictionary:
            result += dictionary[list1[i]] * list1[i]
    return result

def Generate_dict(list2):
    dictionary = {}
    for i in range(len(list2)):
        if list2[i] in dictionary:
            dictionary[list2[i]] += 1
        else:
            dictionary[list2[i]] = 1
    return dictionary

def get_input(file_name):
    try:
        with open(file_name, 'r') as file:
            lines = file.readlines()
            list1, list2 = [], []
            for line in lines:
                part1, part2 = line.split()
                list1.append(int(part1))
                list2.append(int(part2))
            return list1, list2
    except FileNotFoundError:
        print("The file " + file_name + " does not exist.")
        exit()

if __name__ == "__main__":
    list1, list2 = get_input('input.txt')
    dictionary = Generate_dict(list2)
    result = calculate_result(dictionary, list1)
    print(result)

