def a():
    print("jestem w funkcji a")

    def b():
        print("jestem w funkcji b")

    def c():
            print ("Jestem w funkcji c")

    print(locals())
    print(globals())
    b()
    c()
a()
print("Na zewnątrz", globals())