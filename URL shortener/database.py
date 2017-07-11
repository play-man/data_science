from flask import Flask, request, render_template, redirect
import sqlite3

app = Flask(__name__)

@app.route("/")
def main():
        long_url = request.args.get('url')
    return render_template('index.html')


@app.route('/<short_url>')
def redirect_short_url(short_url):
    decoded_string = toBase10(short_url)
    redirect_url = 'http://localhost:8000'
    with sqlite3.connect('urls.db') as conn:
        cursor = conn.cursor()
        select_row = """
                SELECT URL FROM WEB_URL
                    WHERE ID=%s
                """%(decoded_string)
        result_cursor = cursor.execute(select_row)
        try:
            redirect_url = result_cursor.fetchone()[0]
        except Exception as e:
            print e
    return redirect(redirect_url)