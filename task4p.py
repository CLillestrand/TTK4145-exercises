from threading import Thread

# Potentially useful thing:
#   In Python you "import" a global variable, instead of "export"ing it when you declare it
#   (This is probably an effort to make you feel bad about typing the word "global")
i = 0


def incrementingFunction():
    global i
    for j in range(0, 1000000):
        i = i + 1


def decrementingFunction():
    global i
    for j in range(0, 1000000):
        i = i - 1


def main():
    # TODO: Something is missing here (needed to print i)
    print (i)

    incrementing = Thread(target=incrementingFunction, args=(), )
    decrementing = Thread(target=decrementingFunction, args=(), )

    # TODO: Start both threads
    incrementing.start()
    decrementing.start()


    incrementing.join()
    decrementing.join()

    print("The magic number is %d" % (i))



main()