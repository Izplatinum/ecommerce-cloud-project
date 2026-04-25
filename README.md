\# Scalable E-Commerce API on AWS



This project is a production-style Flask API deployed on AWS EC2.



\## Features



\- Flask backend API

\- Product endpoint: /products

\- Deployed on AWS EC2

\- Gunicorn as production WSGI server

\- systemd service for auto-start

\- Nginx reverse proxy

\- Public endpoint without port 5000



\## Live Endpoint



http://54.162.194.27/products



\## Tech Stack



\- Python

\- Flask

\- Gunicorn

\- Nginx

\- Ubuntu

\- AWS EC2

\- Git \& GitHub



\## API Endpoints



\### Home

/



\### Products

/products



\### Health Check

/health



\## Architecture



User Browser → Nginx → Gunicorn → Flask API → JSON Response



\## What I learned



\- How to build a Flask API

\- How to deploy an app on AWS EC2

\- How to use Git and GitHub

\- How to configure Gunicorn and Nginx

\- How to run an app permanently with systemd

