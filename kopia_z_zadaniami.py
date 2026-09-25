from flask import Flask, request, url_for, redirect, abort

app = Flask(__name__)

PRODUCTS = {
    1: "Laptop",
    2: "Myszka",
    3: "Klawiatura"
    }

@app.route("/")
def index():
    return "Strona główna"

@app.route("/start")
def start():
    return redirect(url_for("index"))

@app.route("/about")
def about():
    return "Jesteśmy klasą 4 Technik Programista. Robimy Sklep."

@app.route("/contact")
def contact():
    return "Napisz: sklep@example.com"

@app.route("/secret")
def secret():
    return "Brak dostępu", 403

@app.route("/api/status")
def status():
    return {"ok": True, "wersja": "0.1"}

@app.route("/greetings/<first>")
def greetings(first):
    return f"Cześć, {first}!"

@app.route("/greetings/<first>/<int:age>")
def greetings_age(first, age):
    return f"Cześć, {first}, masz {age} lat!"

@app.route("/user/<first>/<last>")
def user(first, last):
    return f"Użytkownik: {first} {last}"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"{a} + {b} = {a + b}"

@app.route("/subtract/<int:a>/<int:b>")
def subtract(a, b):
    return f"{a} - {b} = {a - b}"

@app.route("/multipy/<int:a>/<int:b>")
def multiply(a, b):
    return f"{a} * {b} = {a * b}"

@app.route("/divide/<int:a>/<int:b>")
def divide(a, b):
    if b == 0:
        return "Nie dzielimy przez zero", 400
    return f"{a} / {b} = {a / b}"

@app.route("/powerof/<int:a>/<int:b>")
def powerof(a, b):
    return f"{a} ^ {b} = {a ** b}"

@app.route("/table/<int:n>")
def table(n):
    if n < 1 or n > 20:
        return "Liczba musi być w przedziale od 1 do 20", 400
    wiersze = []
    for i in range (1,11):
        wiersze.append(f"{n} x {i} = {n * i}")
    return "<br>".join(wiersze)

        

@app.route("/welcome")
def welcome():
    first = request.args.get("first", "nieznajomy")
    time = request.args.get("time", type=int)
    if time is not None and time < 12:
        return f"Dzień dobry, {first}!"
    return f"Witaj, {first}!"

@app.route("/links")
def links():
    return url_for("produkt", id=5)

@app.route("/old-address")
def lod-address():
    return redirect(url_for("index"))

@app.route("/element/<int:id>")
def element(id):
    if id not in PRODUKTY:
        abort(404)
    return f"Produkt: {PRODUKTY[id]}"

@app.route("/elements")
def elements():
    text = ""
    for id in PRODUCTS:
        text += f"{id}: {PRODUCTS[id]}<br>"
    return text

if __name__ == "__main__":
    app.run(debug=True)
