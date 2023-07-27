from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data for books (you can replace this with your own data or connect to a database)
books = [
    {"title": "Book 1", "author": "Author 1", "genre": "Genre 1"},
    {"title": "Book 2", "author": "Author 2", "genre": "Genre 2"},
    # Add more books as needed
]

@app.route('/')
def index():
    return render_template('index.html', books=books)

@app.route('/add_book', methods=['GET', 'POST'])
def add_book():
    if request.method == 'POST':
        title = request.form['title']
        author = request.form['author']
        genre = request.form['genre']
        new_book = {"title": title, "author": author, "genre": genre}
        books.append(new_book)
        return redirect(url_for('index'))
    return render_template('add_book.html')

if __name__ == '__main__':
    app.run(debug=True)
