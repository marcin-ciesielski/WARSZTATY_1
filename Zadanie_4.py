from flask import Flask, request

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def game():
    form = """
    <h3>Pomyśl sobie liczbę od 0 do 1000, a ja ją zgadnę w max. 10 próbach</h3>
    <form action="/" method="POST">

    <label>Zgaduję, czy to : {}</label>
    <input type="hidden" name="guess" value={}>
    <input type="hidden" name="min" value={}>
    <input type="hidden" name="max" value={}>
    <br/>
    <br/>
    <button type="submit" name="submit_button" value="duzo">Za dużo</button>
    <button type="submit" name="submit_button" value="malo">Za mało</button>
    <button type="submit" name="submit_button" value="traf">Trafiłeś</button>
    <br/>
    {}
    """
    if request.method == "POST":
        min = int(request.form['min'])
        max = int(request.form['max'])
        guess = int(request.form['guess'])
        if request.form['submit_button'] == 'duzo':
            max = guess
            guess = int((max - min) / 2) + min
            return form.format(guess, guess, min, max, '')
        elif request.form['submit_button'] == 'malo':
            min = guess
            guess = int((max - min) / 2) + min
            return form.format(guess, guess, min, max, '')
        elif request.form['submit_button'] == 'traf':
            return form.format(guess, None, None, None, 'Brawo!')
    else:
        min = 0
        max = 1000
        guess = int((max - min) / 2) + min
        return form.format(guess, guess, min, max, '')


app.run(debug=True)