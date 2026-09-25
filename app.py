from typing import Any
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

@app.route("/greet/<first>")
def greet(first):
    return f"Cześć, {first}!"

@app.route("/user/<first>/<last>")
def user(first, last):
    return f"Użytkownik: {first} {last}"

@app.route("/add/<int:a>/<int:b>")
def add(a, b):
    return f"{a} + {b} = {a + b}"

@app.route("/divide/<int:a>/<int:b>")
def divide(a, b):
    if b == 0:
        return "Nie dzielimy przez zero", 400
    return f"{a} / {b} = {a / b}"

@app.route("/welcome")
def welcome():
    name = request.args.get("name", "nieznajomy")
    time = request.args.get("time", type=int)
    if time is not None and time < 12:
        return f"Dzień dobry, {name}!"
    return f"Witaj, {name}!"

@app.route("/links")
def links():
    return url_for("produkt", id=5)

@app.route("/old-address")
def old():
    return redirect(url_for("index"))

@app.route("/product/<int:id>")
def product(id):
    if id not in PRODUCTS:
        abort(404)
    return f"Produkt: {PRODUCTS[id]}"

if __name__ == "__main__":
    app.run(debug=True)
