def main():
    #write your code below this line
    countOfNegativeNumbers = 0

    while True:
      number = int(input("Give a number:"))

      if (number == 0):
        break

      if (number<0):
        countOfNegativeNumbers = countOfNegativeNumbers + 1

    print("Number of negative numbers: " + str(countOfNegativeNumbers))

if __name__ == '__main__':
    main()
