from ..models import ContactSubmission


class ContactService:
    def __init__(self, repository):
        self.repository = repository

    def submit(self, form_data):
        submission = ContactSubmission.from_form(form_data)
        self.repository.save(submission)
        return submission

    def list_submissions(self):
        return self.repository.list_all()
