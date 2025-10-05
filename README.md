# Multi-Bots-Hosting

A Docker-based hosting solution for running multiple Telegram bots simultaneously. This project allows you to configure, deploy, and manage multiple bot instances from a single platform with automatic dependency management and environment variable configuration.

## 🚀 Features

- **Multi-Bot Support**: Host multiple Telegram bots simultaneously
- **Automatic Setup**: Clone repositories and install dependencies automatically
- **Docker Support**: Containerized deployment for easy scaling
- **Environment Management**: Individual environment variables for each bot
- **Web Interface**: Simple Flask web interface for monitoring
- **Auto-Ping**: Built-in ping service to keep the system alive
- **Private Repository Support**: Handle both public and private repositories with token authentication

## 📁 Project Structure

```
Multi-Bots-Hosting/
├── app.py              # Flask web application
├── worker.py           # Bot worker process manager
├── ping_server.py      # Keep-alive ping server
├── config.json         # Bot configuration file
├── requirements.txt    # Python dependencies
├── run.sh             # Setup script for bot repositories
├── Dockerfile         # Docker container configuration
└── README.md          # Project documentation
```

## ⚙️ Configuration

### config.json Structure

The `config.json` file defines all your bots and their configurations:

```json
{
  "bot-name": {
    "source": "https://github.com/username/bot-repo.git",
    "env": {
      "BOT_TOKEN": "your-bot-token",
      "API_ID": "your-api-id",
      "API_HASH": "your-api-hash",
      "SESSION_STRING": "your-session-string"
    },
    "run": "main.py"
  }
}
```

#### Configuration Fields:
- **source**: Git repository URL (supports both public and private repos)
- **env**: Environment variables specific to this bot
- **run**: Entry point file for the bot (e.g., `main.py`, `bot.py`)

#### Private Repository Access:
For private repositories, use token authentication:
```json
"source": "https://username:token@github.com/username/private-repo.git"
```

## 🛠️ Installation & Setup

### Method 1: Docker (Recommended)

1. **Clone the repository:**
   ```bash
   git clone https://github.com/vikas-nagar9001/Multi-Bots-Hosting.git
   cd Multi-Bots-Hosting
   ```

2. **Configure your bots:**
   Edit `config.json` with your bot configurations

3. **Build and run with Docker:**
   ```bash
   docker build -t multi-bots-hosting .
   docker run -d -p 10000:10000 multi-bots-hosting
   ```

### Method 2: Local Setup

1. **Prerequisites:**
   - Python 3.9+
   - Git
   - jq (for JSON parsing in bash)

2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Setup bots:**
   ```bash
   chmod +x run.sh
   ./run.sh
   ``````

## 🏃‍♂️ Running on Windows

### Using PowerShell:

1. **Install WSL (Windows Subsystem for Linux)** if not already installed:
   ```powershell
   wsl --install
   ```

2. **Run the bash script through WSL:**
   ```powershell
   wsl bash run.sh
   ```
   
## 🔧 How It Works

1. **Setup Phase (`run.sh`)**:
   - Reads bot configurations from `config.json`
   - Clones each bot repository
   - Installs dependencies for each bot

2. **Runtime Phase (`worker.py`)**:
   - Sets environment variables for each bot
   - Checks and installs missing dependencies
   - Starts each bot as a separate process
   - Monitors bot processes

3. **Web Interface (`app.py`)**:
   - Provides a simple web interface on port 10000
   - Shows system status

4. **Keep-Alive (`ping_server.py`)**:
   - Sends periodic ping requests
   - Prevents system from going idle

## 📊 Monitoring

- **Web Interface**: Access `http://localhost:10000` to view the status page
- **Logs**: Check console output for bot startup and error messages
- **Process Status**: The worker script provides detailed logging for each bot

## 🔒 Security Considerations

- **Environment Variables**: Store sensitive tokens and credentials in the `env` section of `config.json`
- **Private Repositories**: Use personal access tokens for private repo access
- **Docker**: Run in isolated containers for better security
- **Secrets Management**: Consider using external secret management for production

## 🐛 Troubleshooting

### Common Issues:

1. **Git Clone Fails**:
   - Check repository URL and access permissions
   - For private repos, ensure token has proper permissions

2. **Dependency Installation Fails**:
   - Verify `requirements.txt` exists in bot repository
   - Check Python version compatibility

3. **Bot Fails to Start**:
   - Verify environment variables are correct
   - Check bot entry point file exists
   - Review bot-specific error messages

4. **Windows Bash Script Issues**:
   - Use WSL for running bash scripts
   - Or use Docker for cross-platform compatibility

### Debug Mode:
Add debug prints in `worker.py` to trace bot startup issues.

## 🚀 Deployment

### Production Deployment:

1. **Use environment variables** instead of hardcoding tokens in `config.json`
2. **Set up proper logging** with log rotation
3. **Use process managers** like systemd or supervisor
4. **Configure reverse proxy** (nginx) for the web interface
5. **Set up monitoring** and alerting for bot health

### Scaling:
- Use Docker Compose for multi-container deployments
- Implement load balancing for high-traffic bots
- Consider using Kubernetes for large-scale deployments

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

**Note**: This project is designed for hosting multiple Telegram bots, but can be adapted for other types of bot applications with minimal modifications.
