import pyperclip


def main():
    while True:
        s = input("> ")
        pyperclip.copy(s)

        if s.lower() == "exit":
            break

        print(f"Copied to clipboard: {s}")


if __name__ == "__main__":
    main()
