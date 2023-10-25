from django.shortcuts import render

# Create your views here.
def zadanie(request):
    if request.method == 'POST':
        a = request.POST.get("A")
        b = request.POST.get("B")
        c = request.POST.get("C")

        try:
            a = int(a)
            b = int(b)
            c = int(c)

            if a > 0 and b > 0 and c > 0:
                if a == b and a == c and b == c:
                    text = "Треугольник равносторонний"
                elif (a*a == (b*b) + (c*c)) or (b*b == (a*a) + (c*c)) or (c*c == (a*a) + (b*b)):
                    text = "Треугольник прямоугольный"
                elif (a == b and (a+b>c)) or (a == c and ( a + c > b)) or (b == c and (b+c>a)):
                    text = "Треугольник равнобедренный"
                elif (a + b > c) and (a + c > b) and (b + c > a):
                    if a**2 > b**2 + c**2 or b**2 > a**2 + c**2 or c**2 > a**2 + b**2:
                        text = "Треугольник тупоугольный"
                    elif a**2 < b**2 + c**2 and b**2 < a**2 + c**2 and c**2 < a**2 + b**2:
                        text = "Треугольник остроугольный"
                    else:
                        text = "Треугольник неопределенный"
                else:
                    text = "Стороны не могут образовать треугольник"
            else:
                text = "Стороны треугольника должны быть положительными числами"
        except ValueError:
            text = "Стороны треугольника должны быть числами"

        data = {
            "text": text,
        }
        return render(request, "main/zadanie.html", data)

    return render(request, "main/zadanie.html")

def answear(request):
    return render(request, "main/zadanie.html")