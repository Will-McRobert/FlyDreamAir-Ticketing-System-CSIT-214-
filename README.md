# FlyDreamAir-Ticketing-System-CSIT-214-
A simple ticketing and customer management system built for FlyDreamAir as part of the company's digital transformation. Made using the Django web framework for Python.

## Overview
Django is a high-level Python web framework with a focus on simplifying and streamlining the web development process. We have decided to use Django due to its clean and rapid development philosophy, as well as its strong security measures and extensive scalability. 

The following key features form the core of our FlyDreamAir Django web application:

- Django Models 
  - Models serve as the definitive source of the application's data 
  - Each model serves as a database table, and are written as Python classes that can be accessed within the application
  - Removes the hassle of manually creating a database, greatly simplifying and reducing development time
- Django Views
  - Views are Python functions that receive web requests, and return web responses
  - Custom pages can be created and returned for different types of requests (e.g. a custom 404 Not Found template)
- Django URLs
  - The application views can be mapped to specific URL paths within the application (e.g. site/flightbooking)
  - This provides a high level of control over the arrangement and location of site pages and functionality
