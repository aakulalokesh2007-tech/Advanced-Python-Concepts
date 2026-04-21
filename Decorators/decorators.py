def dec(func):
    def wra():
        print(f"running {func.__name__}")
        func()
        print("complet")
    return wra

@dec
def ye():
    print("ye")

@dec
def wq():
    print("wq")


ye()
wq()
