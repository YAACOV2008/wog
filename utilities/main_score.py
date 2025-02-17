from flask import Flask, render_template

from utils import BAD_RETURN_CODE, SCORES_FILE_NAME

app = Flask(__name__)


@app.route('/')
def score_server():
    try:
        score_file = open(SCORES_FILE_NAME, mode="r")
        score = (score_file.readlines())
        score = int(score[0])
        return f"""<html>
    <head>
        <title>WOG: Scores</title>
    </head>
    <body>
        <h1>The score is:</h1>
        <div id="score">{score}</div>
    </body>
</html>"""
    except FileNotFoundError:
        return render_template(f'{BAD_RETURN_CODE}.html')


if __name__ == '__main__':
    app.run()
