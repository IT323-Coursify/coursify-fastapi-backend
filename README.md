## Coursify FastAPI Backend
All API requests include a Bearer token in the Authorization header. The ProtectedRoute component checks coursify_role from localStorage before rendering any route, redirecting unauthorized users to the appropriate fallback.

## Installation & Setup
Prerequisites
•	Node.js v18 or higher
•	npm or yarn
•	Coursify backend running locally or deployed (see backend README)

1. Clone the repository
git clone https://github.com/yourusername/coursify-web.git
cd coursify-web

2. Install dependencies
npm install

3. Configure the API
Create a .env file in the project root:
REACT_APP_API_URL=http://localhost:8000
Replace the value with your deployed backend URL if not running locally.

4. Start the development server
npm start
The app will be available at http://localhost:3000/coursify-web

5. Build for production
npm run build
The optimized build output will be in the build/ folder, ready for static hosting.

Note: The basename is set to /coursify-web in the router. If you deploy to a different path or domain root, update the basename prop in App.js accordingly.

## Known Limitations
•	Admin and superadmin roles are web-only — The mobile version of Coursify only supports the student role. Logging in with admin or superadmin credentials on the mobile app will not grant access to any admin features

•	Email delivery in deployment — OTP verification and password reset emails use Gmail SMTP which requires outbound ports 465 or 587. Most cloud hosting providers block these ports, causing connection timeouts in production. Locally this works fine since the machine can connect directly. The proper solution for production is to replace Gmail SMTP with a dedicated email API service such as SendGrid or Mailgun

•	Assessment results not editable — Once an assessment is submitted it is permanently stored; there is no way to retake or delete a specific attempt from the UI

•	No real-time updates — The analytics dashboard and user management table require a manual page refresh to reflect the latest data


## Coursify Backend
## Project Description
Coursify Backend is the shared FastAPI server that powers both the Coursify Web and Coursify Mobile applications. It handles user authentication, psychometric assessment scoring, machine learning course recommendations, AI-generated profile summaries, and role-based admin operations.
It is built with Python and FastAPI, uses MongoDB Atlas as the database, and exposes a REST API consumed by both frontend platforms via JWT-authenticated requests.

## Features
•	User Authentication — Registration with email OTP verification, login, JWT token issuance, forgot password with reset code, and password reset

•	Role-Based Access Control — Three-tier role system (user, admin, superadmin) enforced via FastAPI middleware dependencies on all protected endpoints

•	Assessment Engine — Randomized question delivery across RIASEC, Big Five, and Aptitude collections; server-side scoring with reverse-scoring support for Big Five

•	ML Course Recommendations — scikit-learn model accepts RIASEC raw scores, Big Five trait means, aptitude percentages, and strand to return top 5 ranked courses with confidence scores

•	AI Profile Summaries — Google Gemini API generates personalized counselor-style summaries from scored assessment data

•	Assessment History — Stores all completed assessment results per user; returns full score breakdowns including RIASEC, Big Five, aptitude, and recommendations

•	Admin Analytics — Aggregated user statistics, registration trends, strand/grade breakdowns, and role distribution with date range filtering

•	User Management — Superadmin endpoints for listing, searching, filtering, role updating, and status toggling of user accounts

•	Audit Logging — Every role change and status change is recorded with actor, timestamp, and new value inside the user document

•	CSV Export — Streams all user data as a downloadable CSV file

•	Account Seeding — CLI scripts to seed superadmin and admin accounts interactively

## Technology Stack
Layer	Technology

API Framework	FastAPI (Python)

Database	MongoDB Atlas

Async DB Driver	Motor

Authentication	JWT via python-jose

Password Hashing	Passlib / bcrypt

Request Validation	Pydantic

Email (local)	Gmail SMTP via smtplib / aiosmtplib

ML Model	scikit-learn

AI Summaries	Google Gemini (google-generativeai)

Environment	python-dotenv

Hosting	Render

## System Architecture
                    ┌─────────────────────────────────┐
                    │       Coursify Web (React)       │
                    │       Coursify Mobile (Expo)     │
                    └────────────────┬────────────────┘
                                     │
                          REST API — Bearer JWT
                                     │
                    ┌────────────────▼────────────────┐
                    │         FastAPI Backend          │
                    │                                  │
                    │  ┌──────────────────────────┐   │
                    │  │        API Routers        │   │
                    │  │                           │   │
                    │  │  /api/auth/*              │   │
                    │  │    register, verify,      │   │
                    │  │    login, profile,        │   │
                    │  │    forgot-password,       │   │
                    │  │    reset-verify,          │   │
                    │  │    reset-password         │   │
                    │  │                           │   │
                    │  │  /api/assessment/*        │   │
                    │  │    questions, submit,     │   │
                    │  │    results/latest,        │   │
                    │  │    results/history        │   │
                    │  │                           │   │
                    │  │  /api/admin/*             │   │
                    │  │    analytics, users,      │   │
                    │  │    users/{id}/role,       │   │
                    │  │    users/{id}/status,     │   │
                    │  │    audit-log,             │   │
                    │  │    export/users           │   │
                    │  │                           │   │
                    │  │  /api/ai/*                │   │
                    │  │    profile-summary        │   │
                    │  └────────────┬─────────────┘   │
                    │               │                  │
                    │  ┌────────────▼─────────────┐   │
                    │  │     Role Middleware       │   │
                    │  │  require_admin()          │   │
                    │  │  require_superadmin()     │   │
                    │  │  get_current_user()       │   │
                    │  └──────────────────────────┘   │
                    └───┬──────────────┬───────────┬───┘
                        │              │           │
           ┌────────────▼──┐  ┌────────▼──────┐  ┌▼──────────────────┐
           │ MongoDB Atlas │  │  scikit-learn │  │  Google Gemini AI  │
           │               │  │   ML Model    │  │                    │
           │  collections: │  │               │  │  Input: scored     │
           │  users        │  │  Input:       │  │  RIASEC + BigFive  │
           │  questions_   │  │  riasec_raw   │  │  + aptitude +      │
           │    riasec     │  │  bigfive_raw  │  │  strand            │
           │  questions_   │  │  aptitude_pct │  │                    │
           │    bigfive    │  │  strand       │  │  Output: 3–4 line  │
           │  questions_   │  │               │  │  profile summary   │
           │    aptitude   │  │  Output:      │  └───────────────────┘
           │  assessment_  │  │  top 5 courses│
           │    results    │  │  + confidence │
           └───────────────┘  └───────────────┘
                                      │
                             ┌────────▼────────┐
                             │   Gmail SMTP     │
                             │  OTP + Password  │
                             │  Reset Emails    │
                             └─────────────────┘
Assessment scoring flow:
1.	Client submits strand, RIASEC answers, Big Five answers, and aptitude answers
2.	Backend fetches question documents from MongoDB to resolve subcategories and correct answers
3.	RIASEC raw scores are summed per code; Big Five means are computed per trait with reverse scoring applied; aptitude correct counts are converted to percentages
4.	Scored data is passed to the scikit-learn ML model which returns top 5 ranked courses
5.	Full result document is stored in assessment_results collection
6.	Recommendations are returned to the client immediately

## Installation & Setup
Prerequisites
•	Python 3.10 or higher
•	MongoDB Atlas account (or local MongoDB instance)
•	Google Gemini API key
•	Gmail account with App Password enabled (for local email testing)

1. Clone the repository
git clone https://github.com/yourusername/coursify-backend.git
cd coursify-backend

2. Create and activate a virtual environment
python -m venv venv

# Windows
venv\Scripts\activate

# macOS / Linux
source venv/bin/activate

3. Install dependencies
pip install -r requirements.txt

4. Configure environment variables
Create a .env file in the project root:
MONGO_URI=your_mongodb_connection_string
JWT_SECRET=your_jwt_secret_key
GEMINI_API_KEY=your_google_gemini_api_key
SMTP_EMAIL=your_email@gmail.com
SMTP_PASSWORD=your_gmail_app_password
FRONTEND_URL=http://localhost:3000

5. Seed the superadmin account
python seed_superadmin.py
You will be prompted to enter a username, email, and password. If the email already exists, the account will be upgraded to superadmin.

6. Seed an admin account (optional)
python seed_admin.py

7. Run the development server
uvicorn main:app --reload
The API will be available at http://localhost:8000
Interactive API docs are accessible at http://localhost:8000/docs

## Known Limitations
•	Email delivery in deployment — Gmail SMTP requires outbound ports 465 or 587, which most cloud hosting providers (including Render's free tier) block. This causes connection timeouts when sending OTP and password reset emails in production. Locally, email delivery works because the machine connects directly. The correct solution for production is to replace Gmail SMTP with a dedicated email API service such as SendGrid or Mailgun, which deliver email over HTTPS (port 443) instead

•	In-memory OTP storage — Pending registrations and password reset codes are stored in Python dictionaries (pending_users, reset_codes) in memory. This means they are lost on server restart and will not work correctly if the backend is scaled to multiple instances. A production-ready solution would store these temporarily in MongoDB or Redis with a TTL index

•	ML model is static — The scikit-learn model is loaded once at startup from a local file. It does not retrain automatically as new assessment data accumulates

•	Admin and superadmin roles are web-only — The mobile application supports the student role only. Admin and superadmin credentials will authenticate successfully via the API but the mobile app does not implement any admin UI or navigation

## Deployment Links
https://coursify-fastapi-backend-1.onrender.com/

## Screenshots
FastAPI 
<img width="1920" height="1080" alt="Screenshot (15)" src="https://github.com/user-attachments/assets/7fdefe7b-cca4-449a-ad76-9b5093a1e63d" />













