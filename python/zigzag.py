import time
import sys


def zigzag():

    indent = 0
    indenting = True

    try:
        while True:
            print(" " * indent, end="")            # end="" to avoid automatically printing a newline after the spaces
            print("***")
            time.sleep(0.1)

            if indenting:
                indent += 1
                if indent == 20:
                    indenting = False

            else:
                indent -= 1
                if indent == 0:
                    indenting = True

    except KeyboardInterrupt:
        sys.exit()


print(zigzag())
