# Kerala Tourism

A simple Flask web application that showcases Kerala tourism through a clean multi-page website. The project includes a home page, destination highlights, an about page, and a contact form for trip enquiries.

## Features

- Multi-page Flask app with beginner-friendly structure
- Tourism-themed pages for `Home`, `Destinations`, `About`, and `Contact`
- Contact form with a success page after submission
- Submitted contact form data printed to the terminal as a Python dictionary
- Reusable static assets for illustrations and styling

## Tech Stack

- Python
- Flask
- HTML
- CSS
- Jinja templates

## Project Structure

```text
kerala-tourism/
|-- app.py
|-- README.md
|-- file.csv
|-- static/
|   |-- images/
|   `-- styles/
`-- templates/
    |-- about.html
    |-- base.html
    |-- category_item.html
    |-- contact.html
    |-- contact_success.html
    |-- destinations.html
    |-- greet.html
    `-- home.html
```

## Routes

| Route | Description |
| --- | --- |
| `/` | Home page |
| `/destinations` | Kerala destination highlights |
| `/about` | About the project |
| `/contact` | Contact form page |
| `/greet/<name>` | Simple dynamic greeting page |
| `/category/<int:categoryid>/<item>` | Dynamic category item page |
| `/base` | Base layout preview page |

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/sangeethsanthosh-git/kerala-tourism.git
cd kerala-tourism
```

### 2. Create and activate a virtual environment

On Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```bash
pip install Flask
```

### 4. Run the app

```bash
python app.py
```

### 5. Open in browser

```text
http://127.0.0.1:5000/
```

## Contact Form Behavior

When the contact form is submitted:

- The user is shown a thank-you page
- The submitted form values are printed in the terminal as a dictionary

Example terminal output:

```python
{
    'name': 'Anu',
    'email': 'anu@example.com',
    'phone': '9876543210',
    'travel_month': 'December',
    'message': 'Need a trip plan'
}
```

## Future Improvements

- Save contact form submissions to a database or CSV
- Add deployment configuration for Render or GitHub Pages alternatives
- Improve form validation and flash messages
- Add screenshots and a live demo link

## Author

Created by Sangeeth Santhosh.
