# AI Block Software Development

This project is a full-stack application with a Vue.js frontend and a Django backend. The frontend allows developers to create AI blocks using prompts, and the backend handles the processing and data management.

## Tech Stack
### Backend
- Django
- Django REST framework

### Frontend
- Vue.js
- Vue CLI

## Prerequisites

- Node.js (version 14 or higher)
- npm (version 6 or higher)
- Python (version 3.8 or higher)

## Setup Instructions

### Backend Setup
1. Navigate to the backend directory:
   ```sh
   cd /Users/worawatlawanont/task_repo/ai_block_software_dev/backend
   ```
2. Create a virtual environment:
   ```sh
   python -m venv venv
   ```
3. Activate the virtual environment:
   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```
4. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
5. Apply migrations:
   ```sh
   python manage.py migrate
   ```
6. Start the development server:
   ```sh
   python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```sh
   cd /Users/worawatlawanont/task_repo/ai_block_software_dev/frontend
   ```
2. Install dependencies:
   ```sh
   npm install
   ```
3. Start the development server:
   ```sh
   npm run serve
   ```

## Development

For development purposes, you can run the application locally using the following commands:

### Backend
1. Install dependencies:
   ```sh
   pip install -r requirements.txt
   ```
2. Start the development server:
   ```sh
   python manage.py runserver
   ```

### Frontend
1. Install dependencies:
   ```sh
   npm install
   ```
2. Start the development server:
   ```sh
   npm run serve
   ```

## License
This project is licensed under the MIT License.