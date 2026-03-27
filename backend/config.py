import os
from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


class Config:
    CONTACTS_CSV_PATH = Path(
        os.environ.get('CONTACTS_CSV_PATH', BASE_DIR / 'contacts.csv')
    )
    CONTACTS_CSV_HEADERS = (
        'name',
        'email',
        'phone',
        'travel_month',
        'message',
        'created_at',
    )
