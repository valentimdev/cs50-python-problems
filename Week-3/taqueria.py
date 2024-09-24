preços={
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}
def main():
    pedido=input("Item: ").title()
    if pedido in preços:
        global total
        total+=preços[pedido]
        print(f"Total: ${total:.2f}")
        main()
    else:
        main()
total=0
while True:
    try:
        main()
    except EOFError and KeyboardInterrupt:
        break