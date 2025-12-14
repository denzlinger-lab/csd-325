from random import randint

def average(li: list) -> float:
    avg = 0
    for num in li:
        avg += num
    avg /= len(li)
    return avg

def main():
    li = []
    for _ in range(5):
        li.append(randint(1, 10))

    avg = average(li)
    print(avg)

if __name__ == "__main__":
    main()