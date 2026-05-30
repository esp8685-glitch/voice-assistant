from wifi import connect
from display import show
from ha_client import ask

connect()

show("WiFi OK")

while True:

    text = input("Utle midagi: ")

    show(
        "Said:\n" +
        text
    )

    answer = ask(text)

    show(
        "Vastus:\n" +
        answer
    )

    print(answer)