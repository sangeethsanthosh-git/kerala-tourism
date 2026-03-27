from dataclasses import asdict, dataclass
from datetime import datetime


@dataclass(frozen=True)
class Stat:
    value: str
    label: str


@dataclass(frozen=True)
class Destination:
    name: str
    tagline: str
    description: str
    image: str


@dataclass(frozen=True)
class InfoCard:
    title: str
    description: str


@dataclass(frozen=True)
class ContactInfo:
    label: str
    value: str


@dataclass(frozen=True)
class ContactSubmission:
    name: str
    email: str
    phone: str
    travel_month: str
    message: str
    created_at: str

    @classmethod
    def from_form(cls, form_data):
        return cls(
            name=form_data.get('name', '').strip() or 'Traveler',
            email=form_data.get('email', '').strip() or 'No email provided',
            phone=form_data.get('phone', '').strip(),
            travel_month=form_data.get('travel_month', '').strip(),
            message=form_data.get('message', '').strip() or 'No message provided',
            created_at=datetime.now().isoformat(timespec='seconds'),
        )

    def to_row(self):
        return asdict(self)

    def to_log_dict(self):
        data = self.to_row()
        data.pop('created_at', None)
        return data
