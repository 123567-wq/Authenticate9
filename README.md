# Authenticate9
# E-commerce Automation Framework

## Overview

This project is a comprehensive automation framework designed to automate the process of searching for a product on Amazon.in and Flipkart.in, navigating through the purchase process, and comparing the lowest-cost product available on both platforms. It includes frontend and backend automation, performance testing, and security testing.

## Technologies Used

- **Programming Language:** Python / JavaScript
- **Frontend Automation:** Cypress
- **Backend Automation:** Requests (Python)
- **Performance Testing:** Locust
- **Security Testing:** OWASP ZAP
- **Version Control:** Git
- **CI/CD:** GitHub Actions

## Setup Instructions

### Prerequisites

- Node.js (for Cypress)
- Python 3.x (for backend automation and Locust)
   
## Install Cypress dependencies:

- npm install
  
### Open Cypress:

-npm run test:ecommerce.spec.js

### Backend Automation

-python3 ecomm_python.py

### Run locust:

-locust -f performance_test.py

### OWASP ZAP:

-zap-cli quick-scan --start-url http://amazon.com --scanners all
-zap-cli quick-scan --start-url http://flipkart.com --scanners all


