from ..content import ABOUT_CONTENT, CONTACT_CONTENT, DESTINATIONS_CONTENT, HOME_CONTENT


class SiteContentService:
    def base_context(self):
        return {'page_key': 'base'}

    def home_context(self):
        return {'page_key': 'home', **HOME_CONTENT}

    def destinations_context(self):
        return {'page_key': 'destinations', **DESTINATIONS_CONTENT}

    def about_context(self):
        return {'page_key': 'about', **ABOUT_CONTENT}

    def contact_context(self):
        return {'page_key': 'contact', **CONTACT_CONTENT}
