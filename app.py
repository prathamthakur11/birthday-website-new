from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

reasons = [
    "You make my world brighter",
    "Your smile heals my worst days",
    "You believe in me like no one else",
    "You are my safe place",
    "You make life fun",
    "You’re the reason I love mornings",
    "You’re more than I ever dreamed of",
    "You make love real for me",
    "You laugh at my worst jokes",
    "You’re a beautiful soul inside and out",
    "You inspire me every day",
    "You show me what real love means",
    "You care about the small things",
    "You’re incredibly strong and kind",
    "You’re thoughtful and loving",
    "You understand me without words",
    "You’re my best friend too",
    "You’re my forever home"
]

@app.route('/')
def home():
    now = datetime.now()
    birthday = datetime(now.year, 7, 18)
    if now > birthday:
        birthday = datetime(now.year + 1, 7, 18)
    delta = birthday - now
    return render_template("index.html", countdown=delta.days, reasons=reasons)
