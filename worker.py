import os
import subprocess
import json
import time
import pkg_resources

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

    # Check if bot config has the required fields
    if 'env' not in bot_config or 'run' not in bot_config:     
        print(f"Check env and run command in config.json  for bot {bot_name}")
        print(f"Missing required fields in configfile for bot {bot_name}. Skipping bot.")
        continue

    # Set the environment variables for this bot (if any)
    for env_name, env_value in bot_config['env'].items():
        os.environ[env_name] = env_value
    
    # Set the bot directory path
    bot_dir = os.path.join(bot_name)  # Adjust the path accordingly
    requirements_file = os.path.join(bot_dir, 'requirements.txt')
    # For cross-platform compatibility, use os.path.join
    bot_file = os.path.join(bot_dir, bot_config['run'])
    print(f"current bot directory: {bot_dir}")
    print(f"full path with excutable file: {bot_file}")


    # Check if the bot directory exists
    if not os.path.exists(bot_dir):
        print(f"Error: Directory for {bot_name} does not exist at {bot_dir}. Skipping bot.")
        continue

    # Check if dependencies are already installed
    try:
        with open(requirements_file, 'r') as f:
            required_packages = f.readlines()

        installed = pkg_resources.working_set
        installed_packages = {pkg.key for pkg in installed}

        # Check for each required package
        needs_install = False
        for req in required_packages:
            package = req.strip().split('==')[0].lower()
            if package not in installed_packages:
                needs_install = True
                break

        # If any package is missing, install the dependencies
        if needs_install:
            print(f"Installing dependencies for {bot_name}...")
            subprocess.run(['pip', 'install', '--no-cache-dir', '-r', requirements_file], check=True)
            print(f"Dependencies installed successfully for {bot_name}")
        else:
            print(f"Dependencies already installed for {bot_name}. Skipping installation.")
    
    except Exception as e:
        print(f"Error reading {requirements_file} for {bot_name}: {e}")
        continue

    # Run the bot's main script
    print(f"Command to run: python {bot_file}")
    print(f"Starting {bot_name} bot with {bot_file}")
    try:
        # Start the bot in a subprocess
        p = subprocess.Popen(['python', bot_file], env=os.environ)
        bot_processes.append(p)
        print(f"Successfully started bot: {bot_name}")
    except Exception as e:
        print(f"Error starting bot {bot_name}: {e}")
        continue

# Wait for all bot processes to complete
  
for p in bot_processes:
    p.wait()

print("All bots have been started successfully.")
