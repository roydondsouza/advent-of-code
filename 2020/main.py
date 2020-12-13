def day1():
    for i in range(0, len(numbers)-1):
        for j in range(i, len(numbers)): 
            if numbers[i] + numbers[j] == 2020:
                print("day 1\nNumbers: {},{}\nProduct: {}".format(numbers[i], numbers[j], numbers[i]* numbers[j]))
                break

def day2():
    for i in range(0, len(numbers)-2):
            for j in range(i, len(numbers)-1): 
                if numbers[i] + numbers[j] < 2020 :
                    for k in range(j, len(numbers)): 
                        if numbers[i] + numbers[j] + numbers[k] == 2020:
                            print("day 2\nNumbers: {},{},{}\nProduct: {}".format(numbers[i], numbers[j], numbers[k], numbers[i]* numbers[j]*numbers[k]))
                            break

try:
    f = open('inputs/day1')
    lines = f.readlines()
    numbers =[int(e.strip()) for e in lines]

    print(numbers)
        
    day1()
    day2()

finally:
    f.close()

