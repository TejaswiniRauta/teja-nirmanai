Teja NirmanAI
Teja NirmanAI is a construction tools and services web application designed to simplify the house construction process for owners, workers, and suppliers.

Overview
People planning to build their homes often have no idea about the total cost, materials needed, or nearby suppliers. This project aims to solve these problems by providing:

Construction Cost Estimator – Calculates estimated cost based on area and shows required materials like cement, rods, sand, etc.

Labour Hire System – Helps workers find nearby work opportunities and allows owners to hire them easily.

Shop Locator – Displays nearby shops for construction materials.

Tools Marketplace – Lists construction tools available for purchase or rent.

AI Assistant – Answers user queries instantly for construction-related doubts.

Features
Responsive frontend using HTML, CSS, and JavaScript

Flask backend with Together AI integration for the chatbot

Tools price filters, categories, and user ratings

Worker and shop pages with live location maps

Payment breakdown system

Dark mode toggle

SEO optimized pages

Current Status
Frontend: Completed and hosted live [Add your GitHub Pages link here]

Backend: Developed and tested locally. Live deployment pending due to free cloud limitations.

Future Development
Fully implement the estimator system with item-wise breakdowns

Live worker booking and verification system

Real-time shop stock and price updates

Online payment gateway integration

Voice-enabled AI assistant for hands-free usage

AI Assistant Details
Backend: Flask (Python)

Model Provider: Together AI

Integration: togather_io.py handles API communication

Status: Live deployment pending; works perfectly on local server

Project Structure
arduino
Copy code
teja-nirmanai/
├── frontend/
│   ├── index.html
│   ├── ai.html
│   ├── workers.html
│   ├── shops.html
│   ├── tools.html
│   ├── payment.html
│   ├── css/
│   │   └── style.css
│   └── js/
│       └── main.js
└── backend/
    ├── app.py
    ├── config.py
    ├── requirements.txt
    ├── togather_io.py
    ├── templates/
    │   └── tools.html
    └── .gitignore
How to Run Locally
Clone the repository:

bash
Copy code
git clone https://github.com/TejaswiniRauta/teja-nirmanai-backend.git
cd teja-nirmanai-backend
Install dependencies:

nginx
Copy code
pip install -r requirements.txt
Run the server:

nginx
Copy code
python app.py
Open your browser at:

arduino
Copy code
http://localhost:5000/
Author
Tejaswini Rauta
[LinkedIn profile link:-https://www.linkedin.com/in/tejaswini-rauta-76a327279?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app]

Note
This project is a demo to showcase full-stack development skills focused on solving real-life construction problems. The backend is fully functional locally and will be deployed live once suitable free hosting is available.

⭐ Thank you for checking out this project.


