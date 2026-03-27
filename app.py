from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/base')
def base():
    return render_template('base.html')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/destinations')
def destinations():
    return render_template('destinations.html')


@app.route('/about')
def about():
    return render_template('about.html')


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        contact_data = {
            'name': request.form.get('name', '').strip(),
            'email': request.form.get('email', '').strip(),
            'phone': request.form.get('phone', '').strip(),
            'travel_month': request.form.get('travel_month', '').strip(),
            'message': request.form.get('message', '').strip(),
        }
        print(contact_data, flush=True)

        name = contact_data['name'] or 'Traveler'
        return render_template('contact_success.html', name=name)

    return render_template('contact.html')


@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)


@app.route('/category/<int:categoryid>/<item>')
def category_item(categoryid, item):
    return render_template('category_item.html', categoryid=categoryid, item=item)


if __name__ == '__main__':
    app.run(debug=True)
