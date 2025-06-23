# 📝 Blog Application

A modern and minimalist blog application built with FastAPI backend and Vue.js frontend - a full-stack project.

## 🚀 Features

- **Modern Frontend**: Vue 3 + Vite + TailwindCSS
- **Fast Backend**: RESTful API with FastAPI
- **Markdown Support**: Blog posts written in markdown format
- **Responsive Design**: Mobile and desktop compatible
- **Dynamic Routing**: SPA experience with Vue Router
- **Real-time Markdown Rendering**: Live rendering with Markdown-it

## 🛠️ Technologies

### Frontend
- **Vue 3** - Modern JavaScript framework
- **Vite** - Fast development environment
- **TailwindCSS** - Utility-first CSS framework
- **Vue Router** - Client-side routing
- **Axios** - HTTP client
- **Markdown-it** - Markdown parser

### Backend
- **FastAPI** - Modern Python web framework
- **CORS Middleware** - Cross-origin resource sharing
- **File-based Storage** - Markdown files

## 📂 Project Structure

```
blog/
├── frontend/                 # Vue.js frontend application
│   ├── src/
│   │   ├── pages/           # Page components
│   │   │   ├── Home.vue     # Home page - blog list
│   │   │   └── Post.vue     # Blog post detail page
│   │   ├── components/      # Reusable components
│   │   ├── assets/          # Static files
│   │   ├── App.vue          # Main app component
│   │   ├── main.js          # Application entry point
│   │   ├── routes.js        # Route definitions
│   │   └── style.css        # Global styles
│   ├── public/              # Static assets
│   ├── package.json         # Frontend dependencies
│   ├── vite.config.js       # Vite configuration
│   └── index.html           # Main HTML file
├── backend/                 # FastAPI backend application
│   ├── posts/               # Blog posts (Markdown files)
│   │   ├── first.md         # Sample blog post
│   │   ├── second.md        # Sample blog post
│   │   └── new.md           # Sample blog post
│   └── main.py              # FastAPI application
└── README.md                # This file
```

## 🚀 Installation & Setup

### Prerequisites
- **Node.js** (v18+)
- **Python** (v3.8+)
- **Bun** (used as package manager)

### 1. Clone the Repository
```bash
git clone <repository-url>
cd blog
```

### 2. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# Linux/Mac:
source venv/bin/activate
# Windows:
# venv\Scripts\activate

# Install FastAPI
pip install fastapi uvicorn
```

### 3. Frontend Setup
```bash
cd frontend

# Install dependencies
bun install
```

### 4. Run the Application

#### Start Backend (Terminal 1):
```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

#### Start Frontend (Terminal 2):
```bash
cd frontend
bun dev
```

### 5. Access the Application
- **Frontend**: http://localhost:5173
- **Backend API**: http://localhost:8000
- **API Documentation**: http://localhost:8000/docs

## 📝 API Endpoints

### Blog Posts
- `GET /posts/` - List all blog posts
- `GET /posts/{post_name}` - Get specific blog post

#### Example API Responses:

**Blog list:**
```json
{
  "posts": ["first", "second", "new"]
}
```

**Blog post detail:**
```json
{
  "content": "# First blog post\n\nThis is blog content"
}
```

## 📄 Adding New Blog Posts

To add a new blog post:

1. Create a new `.md` file in the `backend/posts/` directory
2. Write the content in Markdown format
3. The filename will be used as the URL slug

**Example:** `my-new-post.md` file will be accessible at `/posts/my-new-post` URL.

## 🎨 Frontend Features

- **Responsive Design**: Mobile-first design with TailwindCSS
- **Modern Vue 3**: Uses Composition API and `<script setup>`
- **Markdown Rendering**: Safe HTML rendering with Markdown-it
- **SPA Navigation**: Seamless navigation with Vue Router
- **Loading States**: Dynamic content loading states

## 🔧 Development

### Frontend Development
```bash
cd frontend
bun dev          # Development server
bun build        # Production build
bun preview      # Production preview
```

### Backend Development
```bash
cd backend
uvicorn main:app --reload  # Development with auto-reload
```

## 📄 License

This project is licensed under the MIT License.
