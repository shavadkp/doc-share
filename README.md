# DocShare

## Overview

DocShare is a lightweight full-stack document management application built with Django REST Framework and React.

The application allows users to:

* Create documents
* Edit document content using a rich text editor
* Rename documents
* Upload `.txt` and `.md` files as documents
* Share documents with other users
* Persist documents and sharing data in SQLite

---

## Tech Stack

### Frontend

* React
* TypeScript
* Vite
* Axios
* Tiptap Rich Text Editor
* React Router

### Backend

* Django
* Django REST Framework
* Token Authentication

### Database

* SQLite

---

## Features

### Authentication

* Token-based authentication
* User login

### Document Management

* Create document
* Rename document
* Edit document content
* Save and reopen documents

### Rich Text Editing

* Bold
* Italic
* Underline
* Bullet Lists

### File Upload

Supported file types:

* .txt
* .md

Uploaded files are automatically converted into editable documents.

### Sharing

* Document owner
* Share document with another user
* Viewer access

### Persistence

* Documents stored in SQLite
* Rich text content stored as JSON
* Sharing relationships persisted

---

## Local Setup

### Backend

```bash
cd backend

python -m venv venv

venv\Scripts\activate

pip install -r requirements.txt

python manage.py migrate

python manage.py runserver
```

### Frontend

```bash
cd frontend

npm install

npm run dev
```

Frontend:

http://localhost:5173

Backend:

http://localhost:8000

---

## Test Accounts

### Owner

Username: alice

Password: password123

### Viewer

Username: bob

Password: password123

---

## Running Tests

```bash
python manage.py test
```

---

## Deployment

Frontend: Vercel

Backend: Render
