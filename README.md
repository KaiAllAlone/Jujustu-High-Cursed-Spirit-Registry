# Jujutsu High Cursed Spirit Registry

## Overview

Jujutsu High Cursed Spirit Registry is a Flask-based web application that allows users to document, share, and explore cursed spirit encounters. The project was built to understand the fundamentals of backend development using Flask, while also creating a themed, content-driven platform inspired by the world of Jujutsu Kaisen.

The application demonstrates how a full-stack web system is structured, including user authentication, database modeling, dynamic content rendering, and user interaction features.

## Inspiration

The idea for this project comes from the anime and manga series "Jujutsu Kaisen", where sorcerers encounter and document cursed spirits. This application imagines a digital registry used by students of Jujutsu High to log encounters, track dangerous entities, and share information with others.

From a technical perspective, the goal was to move beyond theoretical learning and build a practical, end-to-end web application that integrates multiple core concepts of Flask and web development.

## Features

- User authentication (registration, login, logout)
- Create, view, and manage cursed spirit encounters
- User-specific profile pages with their encounters
- Dynamic rendering using Jinja2 templates
- Flash messages for user feedback
- Structured database models using SQLAlchemy
- Responsive UI built with Bootstrap

## Tech Stack

- Backend: Flask
- Database: SQLite with SQLAlchemy ORM
- Frontend: HTML, CSS, Bootstrap
- Authentication: Flask-Login

## Project Architecture

The project follows a modular Flask structure to maintain separation of concerns and scalability.

```
project/
│── app/
│   │── __init__.py        # Application factory and configuration
│   │── models.py          # Database models (User, Encounter)
│   │── routes.py          # Application routes and logic
│   │── forms.py           # WTForms for validation and input handling
│   │── templates/         # Jinja2 templates
│   │── static/            # CSS, JS, and images
│
│── instance/              # Instance-specific data (e.g., database file)
│── migrations/            # Database migration files
│── run.py                 # Entry point for running the app
│── config.py              # Configuration settings
```

## Core Concepts Demonstrated

- **Routing and Views**: Handling HTTP requests and responses using Flask routes
- **Template Inheritance**: Reusable layouts using Jinja2
- **Authentication Flow**: Session management with Flask-Login
- **ORM Usage**: Database abstraction with SQLAlchemy
- **Form Handling**: Validation and secure data submission using WTForms
- **Separation of Concerns**: Organized code structure for scalability

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/<your-username>/<your-repo>.git
   cd <your-project-folder>
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate   # Linux/Mac
   venv\Scripts\activate      # Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Initialize the database (if applicable):
   ```bash
   flask db upgrade
   ```

5. Run the application:
   ```bash
   flask run
   ```

## Usage

- Register a new user account
- Log in to access personalized features
- Add new cursed spirit encounters
- Browse encounters created by other users
- View individual user profiles and their submissions

## Future Improvements

- Upvote and downvote system for encounters
- Comment system for discussions
- Search and filtering functionality
- Image upload for encounters
- REST API for external integrations
- Deployment to a cloud platform

## Learning Outcomes

This project was developed to gain hands-on experience with:

- Building a complete Flask application from scratch
- Structuring scalable backend systems
- Managing user authentication and se