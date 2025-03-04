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
- pnpm (version 6 or higher) see -> https://pnpm.io/installation
- Python (version 3.8 or higher) and uv ->  https://docs.astral.sh/uv/getting-started/installation/

*** Both `pnpm` and `uv` are available with homebrew

## Setup Instructions

### Backend Setup
These steps create a django backend with sqlite database to serve Vue app frontend
1. Navigate to the backend directory:
   ```sh
   cd /Users/worawatlawanont/task_repo/ai_block_software_dev/backend
   ```
2. Install dependencies:
   ```sh
   uv sync
   uv lock
   ```
3. Apply migrations:
   ```sh
   uv run python manage.py migrate
   ```
4. Start the development server:
   ```sh
   uv run python manage.py runserver
   ```

### Frontend Setup
1. Navigate to the frontend directory:
   ```sh
   cd /Users/worawatlawanont/task_repo/ai_block_software_dev/frontend
   ```
2. Install dependencies:
   ```sh
   pnpm install
   ```
3. Start the development server:
   ```sh
   pnpm run dev
   ```

## License
This project is licensed under the MIT License.
