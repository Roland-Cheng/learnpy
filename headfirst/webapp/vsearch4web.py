from flask import Flask, render_template, request, escape


def search4letters(phrase: str, letters: str = 'aeiou') -> set:
    return set(letters).intersection(set(phrase))


def log_request(req: 'flask_request', res: str) -> None:
    with open('vsearch.log', 'a') as log:
        print(req.form, file=log, end='|')
        print(req.remote_addr, file=log, end='|')
        print(req.user_agent, file=log, end='|')
        print(res, file=log)


app = Flask(__name__)


@app.route('/search4', methods=['POST'])
def do_search() -> 'html':
    phrase = request.form['phrase']
    letters = request.form['letters']
    results = search4letters(phrase, letters)
    log_request(request, results)
    return render_template(
        'results.html',
        the_title='the results',
        the_phrase=phrase,
        the_letters=letters,
        the_results=results,
    )


@app.route('/')
@app.route('/entry')
def entry_page() -> 'html':
    return render_template('entry.html', the_title='welcome')


@app.route('/viewlog')
def log_page() -> 'html':
    contents = []
    with open('vsearch.log', 'r') as log:
        for line in log:
            contents.append([])
            for item in line:
                contents[-1].append(escape(item))
    titles = ('Form Data', 'Remote_Addr', 'User_agent', 'Resulta')
    return render_template(
        'viewlog.html',
        the_title='view log',
        the_row_title=titles,
        the_data=contents,
    )
    return contents


if __name__ == '__main__':
    app.run(debug=True)
