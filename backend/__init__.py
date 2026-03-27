from flask import Flask

from .config import BASE_DIR, Config
from .repositories.contact_repository import ContactCSVRepository
from .routes import register_routes
from .services.contact_service import ContactService
from .services.content_service import SiteContentService


def create_app(config_overrides=None):
    app = Flask(
        __name__,
        template_folder=str(BASE_DIR / 'templates'),
        static_folder=str(BASE_DIR / 'static'),
    )
    app.config.from_object(Config)

    if config_overrides:
        app.config.update(config_overrides)

    contact_repository = ContactCSVRepository(
        csv_path=app.config['CONTACTS_CSV_PATH'],
        headers=app.config['CONTACTS_CSV_HEADERS'],
    )

    app.extensions['contact_repository'] = contact_repository
    app.extensions['contact_service'] = ContactService(contact_repository)
    app.extensions['content_service'] = SiteContentService()

    register_routes(app)
    return app
