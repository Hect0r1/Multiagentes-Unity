from flask import Flask
import sys
import random

app = Flask(__name__)

@app.route("/")
def principal():
    puntos = []

    # loop para generar carritos internos
    for i in range(10):
        if i >= 0 and i <= 4:
            puntos.append({"id": i + 1, "x": random.uniform(-12, 13), "y": random.uniform(0, 10), "z": random.uniform(-11, -5)})
        
        else:
            puntos.append({"id": i + 1, "x": random.uniform(130, 100), "y": random.uniform(0, 10), "z": random.uniform(-12, -6)})

    return {"carros": puntos}