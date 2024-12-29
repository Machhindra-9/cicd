from flask import Flask, request

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        name = request.form.get('name')
        return f"<h1>Hello, {name}!</h1><p>Thank you for submitting the form.</p>"
    return '''
        <h1>Welcome to the One Page App</h1>
        <form method="post">
            <label for="name">Enter your name:</label>
            <input type="text" id="name" name="name" required>
            <button type="submit">Submit</button>
        </form>
    '''

# Run the application
if __name__ == '__main__':
    app.run(host="0.0.0.0", port=4000, debug=True)
