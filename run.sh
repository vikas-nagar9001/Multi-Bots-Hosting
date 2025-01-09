#!/bin/bash

echo "Starting the bot setup process..."

# Loop through each bot in the config.json file
for bot in $(cat config.json | jq -r 'to_entries[] | "\(.key),\(.value.source)"'); do
  name=$(echo $bot | cut -d',' -f1)
  source=$(echo $bot | cut -d',' -f2)

  # Start processing the bot
  echo "Processing bot: $name from $source"

  # Clone the repository
  echo "Cloning repository for $name..."
  if git clone $source $name; then
    echo "Successfully cloned repository for $name"
  else
    echo "Error cloning repository for $name" >&2
    continue # Skip to the next bot if cloning fails
  fi

  # Navigate to the bot's directory and install dependencies
  echo "Installing dependencies for $name..."
  if cd $name && pip install --no-cache-dir -r requirements.txt; then
    echo "Dependencies installed successfully for $name"
  else
    echo "Error installing dependencies for $name" >&2
    cd ..  # Return to the previous directory
    continue # Skip to the next bot if installation fails
  fi

  # Go back to the main directory
  cd ..
done

echo "Bot setup process completed."
