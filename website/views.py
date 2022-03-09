from flask import Blueprint, render_template, request
import random

views = Blueprint('views', __name__)


@views.route('/', methods=['GET', 'POST'])
def hello():
    greetings = ["Hello", "Bonjour", "Hola", "Privet", "Nǐ hǎo", "Ciao",
                 "Konnichiwa", "Guten Tag", "Oi", "Anyoung", "Ahlan", "Bula"]

    if request.method == 'GET':
        index = random.randrange(0, len(greetings))
        greeting = greetings[index]

    return render_template("hello.html", greeting=greeting, length=len(greetings))
