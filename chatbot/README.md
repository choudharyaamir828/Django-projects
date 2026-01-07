# Real-Time Chatbot with Django Channels

A real-time chatbot application built using Django Channels, WebSockets, and Redis for bidirectional communication between users and an AI-powered chatbot.

## 🚀 Features

- Real-time bidirectional communication via WebSockets
- Connection status indicator
- Responsive and modern UI
- Redis-backed channel layer for scalability

## 🛠️ Technologies Used

- **Django 5.2.8** - Web framework
- **Django Channels 4.0+** - WebSocket support
- **Redis** - Message broker and channel layer
- **Daphne** - ASGI server
- **JavaScript** - Frontend WebSocket client
- **SQLite** - Database (default)

## 📋 Prerequisites

- Python 3.8 or higher
- Docker Desktop (for Redis)
- pip (Python package manager)

## ⚙️ Installation & Setup

### 1. Clone or Extract the Project

```bash
cd chatbot
```

### 2. Create Virtual Environment

```bash
# Create virtual environment
python -m venv env

# Activate virtual environment
# On Windows:
env\Scripts\activate
# On Mac/Linux:
source env/bin/activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**requirements.txt:**

```
Django>=5.2
channels>=4.0.0
channels-redis>=4.1.0
redis>=4.5.0
daphne>=4.0.0
```

### 4. Install and Run Redis

**Using Docker (Recommended):**

```bash
docker run -d -p 6379:6379 --name redis-chatbot redis:latest
```

**Verify Redis is running:**

```bash
docker ps
```

### 5. Run Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Create Superuser (Optional - for Admin Panel)

```bash
python manage.py createsuperuser
```

### 7. Start Development Server

```bash
python manage.py runserver
```

## 🌐 Usage

### Access the Chatbot

Open your browser and navigate to:

```
http://127.0.0.1:8000/
```

## 📁 Project Structure

```
chatbot/
├── chatbot/                 # Project settings
│   ├── settings.py         # Django settings
│   ├── asgi.py             # ASGI configuration
│   ├── urls.py             # Main URL routing
│   └── wsgi.py
├── chat/                    # Chat application
│   ├── consumers.py        # WebSocket consumer
│   ├── routing.py          # WebSocket URL routing
│   ├── models.py           # Database models
│   ├── views.py            # HTTP views
│   ├── urls.py             # App URL routing
│   ├── admin.py            # Admin configuration
│   └── templates/
│       └── chat/
│           ├── index.html  # Main chat interface
│   
├── manage.py
├── requirements.txt
└── README.md
```

## 🧪 Testing

### Test WebSocket Connection

1. Open the chatbot in your browser
2. Check that status shows "Connected" (green)
3. Send a test message (e.g., "hello")
4. Verify bot responds in real-time

### Test Message Persistence

1. Send several messages
2. Close and reopen the browser
3. Messages should load from history

### Test Redis Connection

```bash
# In terminal
docker exec -it redis-chatbot redis-cli ping
# Should return: PONG
```

## 🔧 Configuration

### Redis Settings

Edit `chatbot/settings.py`:

```python
CHANNEL_LAYERS = {
    'default': {
        'BACKEND': 'channels_redis.core.RedisChannelLayer',
        'CONFIG': {
            "hosts": [('127.0.0.1', 6379)],
        },
    },
}
```

### ASGI Application

```python
ASGI_APPLICATION = 'chatbot.asgi.application'
```

## 🐛 Troubleshooting

### WebSocket Connection Failed

- Ensure Redis is running: `docker ps`
- Check server started with ASGI: Look for "Starting ASGI/Daphne" in console
- Verify `daphne` is first in `INSTALLED_APPS`

### Redis Connection Error

```bash
# Restart Redis container
docker restart redis-chatbot

# Check Redis logs
docker logs redis-chatbot
```

### Port Already in Use

```bash
# Kill process on port 8000
# Windows:
netstat -ano | findstr :8000
taskkill /PID <PID> /F

# Mac/Linux:
lsof -ti:8000 | xargs kill -9
```

## 🎨 Customization

### Modify AI Responses

Edit `chat/consumers.py` in the `generate_ai_response` method:

```python
async def generate_ai_response(self, user_message):
    # Add your AI/ML model integration here
    # Currently uses simple keyword matching
    pass
```

### Change UI Theme

Edit `chat/templates/chat/index.html` CSS styles in the `<style>` section.

## 🚀 Deployment Considerations

For production deployment:

1. Set `DEBUG = False` in settings.py
2. Configure `ALLOWED_HOSTS`
3. Use production-grade Redis server
4. Set up proper database (PostgreSQL recommended)
5. Configure static files with whitenoise or CDN
6. Use environment variables for secrets
7. Deploy with Gunicorn + Daphne or use cloud services

## 📦 Docker Management Commands

```bash
# Stop Redis
docker stop redis-chatbot

# Start Redis
docker start redis-chatbot

# Restart Redis
docker restart redis-chatbot

# Remove Redis container
docker rm -f redis-chatbot
```


.
