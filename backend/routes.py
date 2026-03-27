from flask import redirect, render_template, request, session, url_for


def register_routes(app):
    content_service = app.extensions['content_service']
    contact_service = app.extensions['contact_service']
    admin_email = app.config['ADMIN_EMAIL'].strip().lower()

    def is_admin_authenticated():
        return session.get('admin_email') == admin_email

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

    def admin_login():
        if is_admin_authenticated():
            return redirect(url_for('admin_submissions'))

        error = None
        if request.method == 'POST':
            email = request.form.get('email', '').strip().lower()
            if email == admin_email:
                session['admin_email'] = email
                return redirect(url_for('admin_submissions'))

            error = 'Only the configured admin email can access this page.'

        return render_template('admin_login.html', error=error, page_key='admin')

    def admin_submissions():
        if not is_admin_authenticated():
            return redirect(url_for('admin_login'))

        submissions = list(reversed(contact_service.list_submissions()))
        return render_template(
            'admin_submissions.html',
            submissions=submissions,
            admin_email=app.config['ADMIN_EMAIL'],
            page_key='admin',
        )

    def admin_logout():
        session.pop('admin_email', None)
        return redirect(url_for('admin_login'))

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
    app.add_url_rule('/admin/login', endpoint='admin_login', view_func=admin_login, methods=['GET', 'POST'])
    app.add_url_rule('/admin/submissions', endpoint='admin_submissions', view_func=admin_submissions)
    app.add_url_rule('/admin/logout', endpoint='admin_logout', view_func=admin_logout)
    app.add_url_rule('/greet/<name>', endpoint='greet', view_func=greet)
    app.add_url_rule(
        '/category/<int:categoryid>/<item>',
        endpoint='category_item',
        view_func=category_item,
    )
