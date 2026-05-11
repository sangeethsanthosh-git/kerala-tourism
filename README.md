# Kerala Tourism

A Flask-based tourism website for Kerala with a cinematic, responsive frontend and a structured backend. The project blends a "tradition meets modern" visual direction with a practical enquiry workflow that stores contact requests in CSV.

## View Live(demo)

https://kerala-tourism-qpa1.onrender.com

## Overview

This project is built as a content-rich tourism experience rather than a basic multi-page demo. It includes:

- A redesigned image-driven landing page
- A destinations page with curated regional storytelling
- A heritage page focused on Kerala culture and atmosphere
- A premium contact flow with enquiry submission handling
- A structured backend using config, services, repositories, and route registration
- CSV-based persistence for contact enquiries

## Highlights

- Responsive layout for desktop, tablet, and mobile
- Shared design system across all main pages
- Hero slideshow with rotating images
- Rich use of local Kerala travel imagery
- Clean Flask app factory setup
- Contact form submissions printed in the terminal as a dictionary
- Contact form submissions saved to `contacts.csv`
- Render deployment support with `requirements.txt` and `render.yaml`

## Tech Stack

- Python
- Flask
- Jinja2
- HTML
- Tailwind CSS via CDN
- CSV for lightweight storage
- Gunicorn for production serving

## Project Structure

```text
kerala-tourism/
|-- app.py
|-- backend/
|   |-- __init__.py
|   |-- config.py
|   |-- content.py
|   |-- models.py
|   |-- routes.py
|   |-- repositories/
|   |   `-- contact_repository.py
|   `-- services/
|       |-- contact_service.py
|       `-- content_service.py
|-- templates/
|   |-- base.html
|   |-- home.html
|   |-- destinations.html
|   |-- about.html
|   |-- contact.html
|   |-- contact_success.html
|   |-- greet.html
|   `-- category_item.html
|-- static/
|   |-- images/
|   `-- styles/
|-- requirements.txt
|-- render.yaml
|-- README.md
`-- .gitignore
```

## Backend Architecture

The backend is organized to keep logic separate from presentation:

- `app.py`
  Thin entrypoint that creates the Flask app.
- `backend/__init__.py`
  App factory and dependency wiring.
- `backend/config.py`
  Centralized configuration, including the CSV storage path.
- `backend/routes.py`
  Route registration for all pages and form submission flow.
- `backend/services/`
  Application logic for site content and contact handling.
- `backend/repositories/`
  Persistence layer for writing enquiries to CSV.
- `backend/models.py`
  Small dataclass-based models for content and submissions.

## Routes

| Route | Description |
| --- | --- |
| `/` | Home page |
| `/destinations` | Destination showcase |
| `/about` | Kerala heritage and culture page |
| `/contact` | Contact and trip enquiry form |
| `/greet/<name>` | Simple dynamic greeting page |
| `/category/<int:categoryid>/<item>` | Dynamic category display page |
| `/base` | Base layout preview page |

## Local Development

### 1. Clone the repository

```bash
git clone https://github.com/sangeethsanthosh-git/kerala-tourism.git
cd kerala-tourism
```

### 2. Create a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the app

```bash
python app.py
```

### 5. Open it in your browser

```text
http://127.0.0.1:5000/
```

## Contact Form Storage

Contact submissions are stored in a local CSV file.

- File name: `contacts.csv`
- Created automatically on first use
- Ignored by Git through `.gitignore`

Saved columns:

- `name`
- `email`
- `phone`
- `travel_month`
- `message`
- `created_at`

Example terminal output on form submission:

```python
{
    'name': 'Anu',
    'email': 'anu@example.com',
    'phone': '9876543210',
    'travel_month': 'October-March',
    'message': 'Need a scenic and cultural route'
}
```

## Deployment on Render

This project is prepared for Render deployment.

Included files:

- `requirements.txt`
- `render.yaml`

Current production command:

```bash
gunicorn app:app
```

Suggested Render settings:

- Runtime: `Python`
- Build Command: `pip install -r requirements.txt`
- Start Command: `gunicorn app:app`

### Important note about CSV storage on Render

If you deploy on Render's free web service plan, local file storage is not persistent across redeploys or restarts. That means `contacts.csv` should be treated as temporary unless you mount persistent storage on a paid plan.

If you want CSV persistence in production:

1. Use a paid Render plan with persistent disk support.
2. Mount a persistent disk.
3. Set `CONTACTS_CSV_PATH` to your mounted file path.

Example:

```text
CONTACTS_CSV_PATH=/opt/render/project/src/data/contacts.csv
```

## Design Direction

The frontend is designed around a "tradition meets modern" aesthetic:

- Warm earthy palette with forest green, spice gold, and sand tones
- Editorial serif headings with tighter spacing
- Large immersive image sections
- Glassmorphism and soft layered panels
- Responsive layouts that feel premium instead of generic

## Future Improvements

- Add admin or dashboard views for saved enquiries
- Move enquiry storage from CSV to a production database when needed
- Add form validation feedback for the user
- Add SEO metadata and social preview tags
- Add image optimization for faster production loading

## Author

Created by Sangeeth Santhosh.
