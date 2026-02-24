x = "Whats good"

def func1():
    x = "Hello"
    def func2():
        x = "Greetings"
        print("Inner:", x)
    print("Outer:", x)
    func2()
func1()

print("Global:", x)

