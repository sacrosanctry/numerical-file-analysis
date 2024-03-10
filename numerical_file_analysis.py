import time


def swap_lists_if_first_shorter(max_sequence: list[list], number: int) -> None:
    if len(max_sequence[0]) > len(max_sequence[1]):
        max_sequence[1].clear()
        max_sequence[0], max_sequence[1] = max_sequence[1], max_sequence[0]
    else:
        max_sequence[0].clear()
    max_sequence[0].append(number)


def find_max_sequence_and_sum(filename: str) -> (list[int], int, list[int], list[int]):
    max_growth = [[], []]
    max_decrease = [[], []]

    with open(filename) as file:
        first_number = int(file.readline().strip())
        max_growth[0].append(first_number)
        max_decrease[0].append(first_number)

        numbers = [first_number]
        numbers_sum = first_number

        for line in file:
            number = int(line.strip())
            numbers_sum += number
            numbers.append(number)

            if not max_growth[0] or number > max_growth[0][-1]:
                max_growth[0].append(number)
            else:
                swap_lists_if_first_shorter(max_growth, number)

            if not max_decrease[0] or number < max_decrease[0][-1]:
                max_decrease[0].append(number)
            else:
                swap_lists_if_first_shorter(max_decrease, number)

    return numbers, numbers_sum, max(max_growth, key=len), max(max_decrease, key=len)


def find_statistics(numbers: list[int], numbers_sum: int) -> (int, int, int | float, int | float):
    numbers.sort()
    min_num = numbers[0]
    max_num = numbers[-1]
    median_num = (numbers[len(numbers) // 2] if len(numbers) % 2 != 0
                  else (numbers[len(numbers) // 2] + numbers[len(numbers) // 2 - 1]) / 2)
    average_num = numbers_sum / len(numbers)

    return min_num, max_num, median_num, average_num


if __name__ == "__main__":
    file_name = "10m.txt"

    start_time = time.time()

    numbers_list, summed_numbers, max_growing_sequence, max_decreasing_sequence = find_max_sequence_and_sum(file_name)
    min_number, max_number, median_number, average_number = find_statistics(numbers_list, summed_numbers)

    execution_time = time.time() - start_time

    print(f"{max_number = }\n{min_number = }\n"
          f"{median_number = }\n{average_number = }\n\n"
          f"{max_growing_sequence = }\n{max_decreasing_sequence = }\n")
    print(f"execution time: {execution_time:.2f} seconds")
