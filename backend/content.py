from .models import ContactInfo, Destination, InfoCard, Stat


HOME_CONTENT = {
    'hero': {
        'title': 'Escape to Serenity',
        'subtitle': 'Where the backwaters meet the sky and the soul finds its rhythm.',
        'cta_label': 'Explore Destinations',
        'cta_link': '/destinations',
        'image': 'images/1.jpg',
    },
    'intro': {
        'eyebrow': 'The Emerald of India',
        'title': 'A Journey Through Tradition',
        'description': (
            'From the tranquil backwaters of Alleppey to the spice-scented hills of '
            'Munnar, Kerala offers a kaleidoscope of landscapes. Witness the ancient '
            'dance form of Kathakali, indulge in Ayurvedic healing, and taste the '
            'richness of Malabari spices.'
        ),
        'image': 'images/2.jpg',
    },
    'stats': (
        Stat(value='600km', label='Coastline'),
        Stat(value='44', label='Rivers'),
    ),
    'gallery_images': [f'images/{index}.jpg' for index in range(1, 6)],
    'featured_destinations': (
        Destination(
            name='Munnar',
            tagline='Mist-covered tea plantations and rolling hills.',
            description='A cool escape wrapped in tea gardens and mountain air.',
            image='images/3.jpg',
        ),
        Destination(
            name='Alleppey',
            tagline='Slow living on traditional Kettuvallam houseboats.',
            description='Kerala backwaters with relaxing canal journeys and village views.',
            image='images/4.jpg',
        ),
        Destination(
            name='Wayanad',
            tagline='Untamed wildlife and ancient spice trails.',
            description='A nature-rich destination filled with forests, waterfalls, and spice routes.',
            image='images/5.jpg',
        ),
    ),
}

DESTINATIONS_CONTENT = {
    'featured_destinations': (
        Destination(
            name='Munnar',
            tagline='Tea gardens and fresh mountain air.',
            description='Known for tea gardens, winding roads, and fresh mountain air.',
            image='images/munnar.svg',
        ),
        Destination(
            name='Alleppey',
            tagline='Peaceful backwater houseboats.',
            description='Famous for houseboats and peaceful canals.',
            image='images/alleppey.svg',
        ),
        Destination(
            name='Kovalam',
            tagline='Golden sand and coastal views.',
            description='A laid-back destination with scenic beaches and ocean breeze.',
            image='images/kovalam.svg',
        ),
    ),
    'more_destinations': ('Thekkady', 'Wayanad', 'Vagamon', 'Varkala', 'Bekal'),
}

ABOUT_CONTENT = {
    'highlights': (
        InfoCard(
            title='Nature',
            description='Kerala is loved for its mountains, beaches, rivers, forests, and green landscapes.',
        ),
        InfoCard(
            title='Culture',
            description='Visitors enjoy traditional dance forms, local festivals, heritage spaces, and authentic cuisine.',
        ),
        InfoCard(
            title='Relaxation',
            description='From backwater stays to quiet hill retreats, Kerala is perfect for peaceful travel experiences.',
        ),
    )
}

CONTACT_CONTENT = {
    'info_items': (
        ContactInfo(label='Location', value='Trivandrum, Kerala'),
        ContactInfo(label='Phone', value='+91 471 2321132'),
        ContactInfo(label='Email', value='hello@keralatourism.com'),
    ),
    'travel_month_options': (
        ('October-March', 'October - March (Winter)'),
        ('April-May', 'April - May (Summer)'),
        ('June-September', 'June - September (Monsoon)'),
    ),
}
