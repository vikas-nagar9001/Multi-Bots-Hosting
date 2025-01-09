import os
import subprocess
import json
import time

# Load bot configuration from config.json
with open("config.json", "r") as jsonfile:
    bots = json.load(jsonfile)

bot_processes = []

# Iterate through each bot defined in the config.json
for bot_name, bot_config in bots.items():
    
    # Add a small sleep between each bot to avoid overloading the platform
    time.sleep(5)

    # Log start for this bot
    print(f"Starting setup for bot: {bot_name}")

    # Set the environment variables for this bot (if any)
    for env_name, env_value in bot_config['env'].items():
        os.environ[env_name] = env_value
    
    bot_dir = f"/app/{bot_name}"
    requirements_file = os.path.join(bot_dir, 'requirements.txt')
    bot_file = os.path.join(bot_dir, bot_config['run'])

    # Check if the bot directory exists
    if not os.path.exists(bot_dir):
        print(f"Error: Directory for {bot_name} does not exist at {bot_dir}. Skipping bot.")
        continue

    # Log and install bot dependencies (if any)
    print(f"Installing dependencies for {bot_name}...")
    try:
        subprocess.run(['pip', 'install', '--no-cache-dir', '-r', requirements_file], check=True)
        print(f"Dependencies installed successfully for {bot_name}")
    except subprocess.CalledProcessError as e:
        print(f"Error installing dependencies for {bot_name}: {e}")
        continue

    # Run the bot's main script
    print(f"Starting {bot_name} bot with {bot_file}")
    try:
        # Start the bot in a subprocess
        p = subprocess.Popen(['python3', bot_file], cwd=bot_dir, env=os.environ)
        bot_processes.append(p)
        print(f"Successfully started bot: {bot_name}")
    except Exception as e:
        print(f"Error starting bot {bot_name}: {e}")
        continue

# Wait for all bot processes to complete
for p in bot_processes:
    p.wait()

print("All bots have been started successfully.")
