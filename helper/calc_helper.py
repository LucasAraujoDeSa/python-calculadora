def soma(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mult(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

def calc(n1, n2, id):
    calc = [
        {
            "id":1,
            "method": soma
        },
        {
            "id":2,
            "method": sub
        },
        {
            "id":3,
            "method": mult
        },
        {
            "id":4,
            "method": div
        }
    ]

    for i in range(len(calc)):
        if(calc[i]['id'] == id):
            result = calc[i]['method'](n1, n2)

    print(f"\nresultado: {result}")