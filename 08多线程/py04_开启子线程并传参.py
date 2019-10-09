import threading


def main():
    threading.Thread(target=print_txt, args=('hello world',)).start()
    threading.Thread(target=test, args=('hello world', 'hello python')).start()


def print_txt(txt):
    print(txt)


def test(a, b):
    print(a)
    print(b)


if __name__ == '__main__':

    main()

