---

# Teja NirmanAI

Teja NirmanAI is a *modern web-based home construction assistance platform* designed to simplify construction planning for users with little or no technical knowledge of construction.
It combines *cost estimation, AI guidance, and practical tools* to make home construction smarter and more transparent.

---

## Overview

Building a home often involves confusion around cost, materials, labour, and tools.
Teja NirmanAI aims to solve this problem by providing a *single digital platform* where users can:

* Estimate construction costs
* Understand material requirements
* Get AI-based guidance
* Explore labour and tools (planned features)

---

## Key Features

### Construction Cost Estimation

* Users enter the built-up area (in square feet)
* System generates an estimated construction budget
* Simple and transparent estimation logic

### Material Requirement Calculator (In Progress)

* Calculates approximate quantities of:

  * Cement
  * Steel rods
  * Bricks
  * Sand
* Designed for future integration with live market rates

### Worker Hiring (Planned)

* Connect homeowners with nearby skilled labourers
* Simplifies worker discovery for construction tasks

### Nearby Material Shops (Planned)

* Helps users locate nearby construction material suppliers
* Reduces dependency on middlemen

### Tools for Rent or Purchase (Planned)

* Explore modern construction tools
* Rent or buy tools directly through the platform

### AI Chatbot Assistant

* Integrated AI chatbot using Together.ai
* Assists users with:

  * Construction queries
  * Cost estimation doubts
  * Material-related questions
* Currently works locally due to free hosting limitations

---

## Project Status

### Frontend

* Fully developed
* Hosted on GitHub Pages as a live demo

### Backend

* Built using Flask
* AI chatbot integration working locally
* Cloud deployment pending

### Estimator

* Basic estimator implemented
* Planned upgrade for real-time market-based pricing

---

## Estimation Approach

The estimator follows a *clear and user-friendly logic*:

Estimated Cost = Built-up Area (sq ft) × Average Cost per Sq Ft

This approach allows users to:

* Get an early budget idea
* Plan finances before contacting contractors
* Avoid overestimation and confusion

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

## Future Development Goals

* Deploy backend on Google Cloud or Render
* Integrate UPI payment gateway for:

  * Tool bookings
  * Worker payments
* Enable voice-based AI assistant
* Live notification system for nearby workers
* Exact material calculator using real-time market rates

---

## Use Cases

* First-time home builders
* Users planning construction budgets
* People with limited construction knowledge
* Small-scale residential projects

---

## Author

Tejaswini Rauta
Aspiring Full-Stack Developer
Passionate about building *real-life impactful solutions* using AI and web technologies.

---

## License

MIT License

---


---
