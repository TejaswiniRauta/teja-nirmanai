---

# Teja NirmanAI

Teja NirmanAI is a modern web-based home construction assistance platform designed to simplify construction planning for users with little or no technical knowledge.
The platform combines cost estimation, AI guidance, and construction-related utilities into a single, easy-to-use interface.

---

## Problem Statement

Home construction is complex due to:

* Lack of cost transparency
* Confusion about material requirements
* Difficulty finding workers and tools
* No technical guidance for non-experts

Teja NirmanAI aims to solve these problems using *web technology + AI assistance*.

---

## Features

### Construction Cost Estimation

* User inputs built-up area in square feet
* Generates approximate construction cost instantly
* Helps in early budget planning and decision-making

### Material Requirement Estimation (Under Development)

* Calculates approximate quantities of:

  * Cement
  * Steel rods
  * Bricks
  * Sand
* Designed to be extended with real-time market pricing

### AI Chatbot Assistant

* AI-powered chatbot integrated using Together.ai
* Helps users with:

  * Construction-related questions
  * Cost estimation doubts
  * Material planning queries
* Currently runs locally due to free hosting limitations

### Worker Hiring Module (Planned)

* Connects homeowners with nearby skilled labourers
* Simplifies workforce discovery for construction work

### Nearby Material Shops (Planned)

* Displays nearby construction material shops
* Reduces dependency on middlemen

### Tools for Rent or Purchase (Planned)

* Browse construction tools
* Option to rent or buy tools directly from the platform

---

## Technology Stack / Skills Used

### Frontend

* HTML
* CSS
* JavaScript

### Backend

* Python
* Flask (API development)

### AI Integration

* Together.ai (LLM-based chatbot)
* Prompt-based construction guidance

### Tools & Platforms

* Git & GitHub
* GitHub Pages (Frontend Hosting)
* VS Code

---

## Estimation Logic (How It Works)

The cost estimator follows a simple and transparent approach:

Estimated Construction Cost
= Built-up Area (sq ft) × Average Cost per Sq Ft

This allows users to:

* Quickly understand budget range
* Avoid contractor overpricing
* Plan finances before execution

---

## Project Workflow

1. User enters construction area
2. Estimator calculates approximate budget
3. User explores materials, tools, and services
4. AI chatbot assists with construction queries
5. Future updates will include payments and notifications

---

## Project Status

### Frontend

* Completed
* Hosted live on GitHub Pages

### Backend

* Flask-based backend developed
* AI chatbot functional locally
* Cloud deployment pending

### Estimator

* Basic version implemented
* Planned upgrade for real-time material pricing

---

## Installation & Setup (Local)

### Prerequisites

* Python 3.9 or above
* Git installed

### Steps

1. Clone the repository
   git clone [https://github.com/tejaswinirauta/teja-nirmanai.git](https://github.com/tejaswinirauta/teja-nirmanai.git)

2. Navigate to project directory
   cd teja-nirmanai

3. Install backend dependencies
   pip install flask

4. Run backend server
   python app.py

5. Open index.html in browser for frontend

---
```

## Project Structure

Teja-NirmanAI
├── index.html
├── script.js
├── style.css
├── README.md
├── backend/
│   └── app.py
├── pages/
│   ├── estimator.html
│   └── chatbot.html
├── assets/
│   ├── images/
│   └── icons/
└── testmap.html

```
---

## Live Demo

[https://tejaswinirauta.github.io/teja-nirmanai](https://tejaswinirauta.github.io/teja-nirmanai)

---

## Future Enhancements

* Deploy backend on Google Cloud or Render
* Integrate UPI payment gateway
* Voice-based AI assistant
* Live worker notifications
* Real-time material price integration
* User authentication and dashboard

---

## Use Cases

* First-time home builders
* Users planning construction budgets
* Non-technical users needing guidance
* Small residential construction projects

---

## Developer 

Tejaswini Rauta
Aspiring Full-Stack Developer
Focused on building real-world, AI-powered solutions using web technologies.

---

## License

MIT License

---
