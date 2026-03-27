from flask import render_template, request


def register_routes(app):
    content_service = app.extensions['content_service']
    contact_service = app.extensions['contact_service']

    def base():
        return render_template('base.html', **content_service.base_context())

    def home():
        return render_template('home.html', **content_service.home_context())

    def destinations():
        return render_template(
            'destinations.html',
            **content_service.destinations_context(),
        )

    def about():
        return render_template('about.html', **content_service.about_context())

    def contact():
        if request.method == 'POST':
            submission = contact_service.submit(request.form)
            print(submission.to_log_dict(), flush=True)
            return render_template(
                'contact_success.html',
                name=submission.name,
                page_key='contact',
            )

        return render_template('contact.html', **content_service.contact_context())

    def greet(name):
        return render_template('greet.html', name=name)

    def category_item(categoryid, item):
        return render_template(
            'category_item.html',
            categoryid=categoryid,
            item=item,
        )

    app.add_url_rule('/base', endpoint='base', view_func=base)
    app.add_url_rule('/', endpoint='home', view_func=home)
    app.add_url_rule('/destinations', endpoint='destinations', view_func=destinations)
    app.add_url_rule('/about', endpoint='about', view_func=about)
    app.add_url_rule('/contact', endpoint='contact', view_func=contact, methods=['GET', 'POST'])
    app.add_url_rule('/greet/<name>', endpoint='greet', view_func=greet)
    app.add_url_rule(
        '/category/<int:categoryid>/<item>',
        endpoint='category_item',
        view_func=category_item,
    )
