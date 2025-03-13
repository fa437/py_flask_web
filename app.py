from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/blog')
def blog():
    return render_template('blog.html')

@app.route('/contact')
def contact():
    return render_template('/contact.html')

@app.route('/create_ticket', methods=['GET', 'POST'])
def create_ticket():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        issue = request.form['issue']
        # Process and save the ticket
        return redirect(url_for('success'))  # Redirect after submission
    return render_template('create_ticket.html')

@app.route('/submit_message', methods=['POST'])
def submit_message():
    name = request.form['name']
    email = request.form['email']
    message = request.form['issue']
    
    # Process the form (save to database, log, etc.)
    print(f"Name: {name}, Email: {email}, Message: {message}")

    return redirect(url_for('success'))  # Redirect to success page

@app.route('/success')
def success():
    return "Your message has been submitted successfully!"

if __name__ == '__main__':
    app.run(debug=True)
