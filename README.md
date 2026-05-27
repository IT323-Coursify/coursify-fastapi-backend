# Project Title
Coursify: A Personalized Course Recommendation System

## Project Description
Coursify is a personalzed college course recommendation system designed for Senior High School (SHS) sutdents in the Philippines. The system helps students identify suitable college degree programs based on their RIASEC
interests, Big Five personality traits (OCEAN), and academic performance in core subjects such as Mathematics, Science, English, and Abstract Reasoning.The platform uses a Random Forest machine learning model to analyze
student assessment data and geneate ranked course recommendations. Coursify aims to reduce mismatched college enrollments, course shifting, and dropoutrates by providing data-driven career guidance.

## Features
1. Authentication & User Management

Feature	Description
Registration	Email verification with 6-digit OTP (10-min expiry)
Login	JWT-based authentication, 7-day expiry
Password Reset	OTP-based flow with short-lived reset token
Profile Management	Update username, grade level, strand
Role System	user → admin → superadmin hierarchy

2. Assessment Engine

Feature	Description
RIASEC Test	60 questions (10 per code) → 5-point Likert scale
Big Five Test	40 questions (8 per trait) → with reverse scoring
Aptitude Test	48 questions (4 subjects × 12 questions) → multiple choice
Random Sampling	Questions shuffled per user from active pool

3. ML Course Recommendation

Feature	Description
Model	RandomForest Classifier
Input Features	20-dimensional vector (RIASEC 6 + Big5 5 + Aptitude 4 + Strand 5)
Output	Top 5 courses with confidence percentages
Artifacts	Model, scaler, label encoder, feature names (joblib)

4. Admin Dashboard

Endpoint	Access	Purpose
/analytics	Admin+	User stats, registration trends, role/strand breakdown
/analytics/courses	Admin+	Most-recommended courses, per-strand rankings
/analytics/assessments	Admin+	Submission stats, avg aptitude/RIASEC scores
/questions	Admin+	CRUD operations on question pools
/users	Superadmin only	Paginated user list with role/status updates
/audit-log	Superadmin only	Role & status change history
/export/users	Superadmin only	CSV export of all users

5. Question Management

Three question pools with distinct schemas:

Pool	Fields
RIASEC	text, subcategory (6 codes), active
Big Five	text, subcategory (5 traits), reverse_scored, active
Aptitude	text, subject, topic, difficulty, options (A-D), correct_answer, active

## Technology Stack
Frontend Technologies

Web Application

* React
* HTML5
* CSS3
* JavaScript
* GitHub Pages (deployment)

Mobile Application

* React Native
* Expo
* Android & iOS support

⸻

Backend Technologies

* FastAPI
* Python
* Uvicorn ASGI Server
* Pydantic (data validation)
* Motor Async Driver

⸻

Database Technologies

* MongoDB

⸻

Machine Learning Technologies

* scikit-learn
* Random Forest Classifier
* Joblib (model serialization)

⸻

APIs and Communication

* REST API
* JSON data format
* HTTPS/TLS communication
* JWT Authentication

⸻

Cloud Services and Deployment

* Render (Backend Hosting)
* GitHub Pages (Frontend Hosting)
* MongoDB Atlas (Cloud Database)
* Planned Docker Containerization

⸻

Security Technologies

* JWT (JSON Web Tokens)
* bcrypt password hashing
* HTTPS/SSL encryption
* Pydantic validation
* Planned SlowAPI rate limiting

⸻

Development Tools

* Postman (API testing)
* Docker (planned deployment/containerization)
* Git/GitHub for version control

  
## System Architecture
<img width="1179" height="1204" alt="66830543-87e7-46a9-be7d-e0bfa750b619" src="https://github.com/user-attachments/assets/fb0d2ef5-d6c3-4813-954e-95d4edd5e965" />

## Installation & Setup

## Deployment Link
https://coursify-web-mzls.onrender.com/
https://coursify-fastapi-backend-1.onrender.com/
https://drive.google.com/file/d/1KVlR_xhUrL87Eb8BF9vENUXHQWB4bY8B/view
## Test Account

## Team Members and Roles
Pailanan, Joana Mae B.
Lao, Dwight Ashley P.
Rodano, Audrick

## Known Limitations

## Screenshots



