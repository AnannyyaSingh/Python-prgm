#Mixed Scope
a = 10

def func1():
    a = 20

    def func2():
        nonlocal a
        a = 30
        print(f"Func2 a: {a}")

    func2()
    print(f"Func1 a: {a}")

func1()
print(f"Global a: {a}")
