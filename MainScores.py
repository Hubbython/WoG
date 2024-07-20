from flask import Flask, render_template_string
from Utils import SCORES_FILE_NAME, BAD_RETURN_CODE

app = Flask(__name__)

@app.route('/')
def score_server():
    try:
        with open(SCORES_FILE_NAME, 'r') as score_file:
            score = score_file.read().strip()
        score_html = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1>The score is <div id="score">{score}</div></h1>
        </body>
        </html>
        """
    except Exception as e:
        score_html = f"""
        <html>
        <head>
        <title>Scores Game</title>
        </head>
        <body>
        <h1><div id="score" style="color:red">{BAD_RETURN_CODE}</div></h1>
        </body>
        </html>
        """
    return render_template_string(score_html)

if __name__ == '__main__':
    app.run(debug=True, port=5001)
