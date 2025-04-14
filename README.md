# Citenet: Visualizing Citation Networks

Citenet is a web-based tool that visualizes the interconnections between research papers through their citation networks. Using a tree-like structure, it enables researchers to trace foundational works, discover new ideas, and identify research gaps by exploring cited and citing papers interactively. Built with Django, PostgreSQL, and D3.js, Citenet integrates the Semantic Scholar API to fetch paper data and provides features like dynamic search, responsive graphs, user authentication, and graph history management.

## Features

- **Dynamic Search**: Search for papers with real-time suggestions powered by the Semantic Scholar API.
- **Interactive Visualization**: Generate responsive, tree-like citation graphs using D3.js, with node highlighting and tooltip-based title copying.
- **User Authentication**: Sign in, sign out, and reset passwords via email (using SMTP2GO).
- **Graph Management**: Save generated graphs, view them in a history section, and delete as needed.
- **Admin Panel**: Manage users through Django’s built-in admin interface.
- **Responsive Design**: Adapts to various screen sizes for accessibility.
- **Testing**: Backend and API endpoints tested with Postman.

## Tech Stack

- **Backend**: Django
- **Database**: PostgreSQL (SQLite used in development, as per `db.sqlite3`)
- **Frontend Visualization**: D3.js
- **API**: Semantic Scholar API (accessed via Axios with rate limiting)
- **Mailing Service**: SMTP2GO
- **Deployment**: Render platform
- **Static Files**: CSS (`main.css`) and JavaScript (`search_suggestion.js`)

## Project Structure

```
raviteja-112-citenet/
└── citeNet/
    ├── db.sqlite3                  # SQLite database (development)
    ├── manage.py                   # Django management script
    ├── accounts/                   # Authentication app
    │   ├── forms.py                # User forms (login, registration)
    │   ├── models.py               # User-related models
    │   ├── urls.py                 # Authentication URLs
    │   ├── views.py                # Authentication views
    │   ├── migrations/             # Database migrations
    │   └── ...
    ├── citeNet/                    # Project settings
    │   ├── settings.py             # Django configuration
    │   ├── urls.py                 # Project-wide URL routing
    │   ├── wsgi.py                 # WSGI entry point
    │   └── ...
    ├── core/                       # Main application logic
    │   ├── models.py               # Graph and history models
    │   ├── urls.py                 # Core URLs (search, graph, history)
    │   ├── views.py                # Core views
    │   ├── migrations/             # Database migrations
    │   └── ...
    ├── static/                     # Static assets
    │   ├── css/
    │   │   └── main.css            # Styling
    │   └── js/
    │       └── search_suggestion.js # Search suggestion logic
    └── templates/                  # HTML templates
        ├── layout.html             # Base template
        ├── accounts/               # Authentication templates
        │   ├── login.html
        │   ├── register.html
        │   ├── password_reset.html
        │   └── ...
        ├── core/                   # Core templates
        │   ├── search_suggestions.html
        │   ├── tree.html
        │   ├── history.html
        │   └── ...
        ├── partials/               # Reusable components
        │   ├── navbar.html
        │   └── sidebar.html
        └── registration/           # Password reset email templates
```

## Prerequisites

- Python 3.8+
- PostgreSQL (for production; SQLite used in development)
- A Semantic Scholar API key or you can use public endpoints
- An SMTP2GO account for email services

## Installation

1. **Clone the Repository**  
   ```bash
   git clone https://github.com/[your-username]/raviteja-112-citenet.git
   cd raviteja-112-citenet/citeNet
   ```

2. **Set Up a Virtual Environment**  
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
   *Note*: If `requirements.txt` is not included, install Django and other dependencies manually:
   ```bash
   pip install django psycopg2-binary requests
   ```

4. **Configure Environment Variables**  
   Create a `.env` file in the `citeNet/` directory and add:
   ```plaintext
   SECRET_KEY=your_django_secret_key
   DEBUG=True
   SEMANTIC_SCHOLAR_API_KEY=your_api_key
   SMTP2GO_API_KEY=your_smtp2go_key
   DATABASE_URL=sqlite:///db.sqlite3  # Replace with PostgreSQL URL for production
   ```

5. **Run Migrations**  
   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

6. **Collect Static Files**  
   ```bash
   python manage.py collectstatic
   ```

7. **Create a Superuser (for Admin Panel)**  
   ```bash
   python manage.py createsuperuser
   ```

8. **Run the Development Server**  
   ```bash
   python manage.py runserver
   ```
   Access the app at `http://localhost:8000`.

## Usage

1. **Sign Up or Log In**: Create an account or log in to access Citenet’s features.
2. **Search for a Paper**: Use the search bar to find a paper. Suggestions appear dynamically.
3. **Generate a Citation Graph**: Select a paper to visualize its citation network as an interactive tree.
4. **Interact with the Graph**: Highlight nodes, copy titles via tooltips, or save the graph for later.
5. **View History**: Check the history section to revisit or delete saved graphs.
6. **Admin Access**: Visit `/admin` with superuser credentials to manage users.

## Deployment

To deploy on Render:
1. Push the repository to GitHub.
2. Create a new web service on Render, selecting the repository.
3. Configure environment variables (as in `.env`).
4. Set the build command: `pip install -r requirements.txt && python manage.py migrate`.
5. Set the start command: `gunicorn citeNet.wsgi:application`.

## Testing

- **Backend and API**: Use Postman to test endpoints (e.g., search, graph generation).
- **Frontend**: Manually verify graph rendering, responsiveness, and tooltip functionality.
- **Authentication**: Test login, registration, and password reset flows.

## Contributing

Contributions are welcome! To contribute:
1. Fork the repository.
2. Create a feature branch (`git checkout -b feature-name`).
3. Commit changes (`git commit -m "Add feature"`).
4. Push to the branch (`git push origin feature-name`).
5. Open a pull request.



