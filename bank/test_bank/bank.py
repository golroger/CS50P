def main():

    print("$"+str(value(input("greeting : "))))


def value(g):
    g = g.lower()
    g = g.replace(" ", "")
    gg = g[0:5]

    if gg == "hello":
        return 0
    elif gg[0] == "h":
        return 20
    else:
        return 100


if __name__ == "__main__":
    main()
