<h1 align="center">🏄‍♂️ SUPAFAST</h1>

### 🐴 Why
This tutorial should serve as an example of using supabase api to connect to your database instance and build a service to periodically cache and serve consumer credit data on client request. This project covers redis as a caching mechanism, supabase to support our postgres instance, and fastapi for our framework, all deployed on Deta Cloud. 

### ☂️ Setting up your environment

Setup your virtual environment:

```bash
python3 -m venv env 
```

Activating your environment

```zsh 
source env/bin/activate
```

In the root directory run the following:

```bash
pip install -r requirements.txt
```

### 🤖 Starting Redis in development environment

To begin working with redis, run the following command, after completion open a new terminal window.

```zsh
redis-server
```

### 👾 Activating your development server

To start your local server run the following command

```zsh
uvicorn main:app --reload
```

On success of the commad you should see;

```zsh
INFO:     Uvicorn running on http://127.0.0.1:8000 (Press CTRL+C to quit)
INFO:     Started reloader process [13385] using watchgod
INFO:     Started server process [13387]
2022-02-11 19:32:12,509:INFO - Started server process [13387]
INFO:     Waiting for application startup.
2022-02-11 19:32:12,509:INFO - Waiting for application startup.
2022-02-11 19:32:12,510:INFO -  02/11/2022 07:32:12 PM | CONNECT_BEGIN: Attempting to connect to Redis server...
2022-02-11 19:32:12,511:INFO -  02/11/2022 07:32:12 PM | CONNECT_SUCCESS: Redis client is connected to server.
INFO:     Application startup complete.
2022-02-11 19:32:12,511:INFO - Application startup complete.
```