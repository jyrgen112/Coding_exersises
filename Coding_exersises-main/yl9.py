a = float(input("A: "))
b = float(input("B: "))
c = float(input("c: "))

if a >= b + c or b >= a + c or c >= a + b:
    print("Sukest kolmnurka ei ole olemas!")
elif a == b and b != c or a == c and a != b or b == c and b != a:
    print("Kolmnurk on võrdhaarne")
elif a == b and b == c:
    print("Kolmnurk on võrdkülgne")
else:
    print("Kolmnurk on errikülgne")