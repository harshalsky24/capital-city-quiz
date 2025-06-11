ECHO is on.
# Capital City Quiz App

A fun quiz web app to test your knowledge of world capitals. Built with **Django (REST API)** and **Vue.js** frontend.

---

## Tech Stack

- Backend: Django, Django REST Framework
- Frontend: Vue.js 3, Axios
- External API: [CountriesNow API](https://countriesnow.space/api/v0.1/countries/capital)

---
### Clone the Repository

```bash
git clone https://github.com/harshalsky24/capital-city-quiz.git

## Quick Start

### Backend Setup (Django)

```bash
cd backend
python -m venv env
source env/bin/activate  # Windows: env\Scripts\activate
pip install -r requirements.txt
python manage.py runserver

Server runs at: http://127.0.0.1:8000/api/

### Frontend Setup (Vue.js)
cd frontend
npm install
npm run serve

App runs at: http://localhost:8080/

## Endpoints
Method	    Endpoint	Description
GET	    /api/country/	Get a random country
POST	/api/check/	    Validate capital answer


## Project Structure
capital-quiz-project/
├── backend/
│   ├── quiz/ (Django app)
│   └── requirements.txt
├── frontend/
│   ├── src/App.vue
│   └── package.json

