for bot in $(cat config.json | jq -r 'to_entries[] | "\(.key),\(.value.source)"'); do
  name=$(echo $bot | cut -d',' -f1); \
  source=$(echo $bot | cut -d',' -f2); \
  git clone $source $name; \
  cd $name && pip install --no-cache-dir -r requirements.txt && cd ..; \
done




# Step-by-Step Explanation
# Loop Through Entries in config.json:

#/////////////////////////////////////////////////////////
# bash
# Copy code

# for bot in $(cat config.json | jq -r 'to_entries[] | "\(.key),\(.value.source)"');
# cat config.json reads the content of the config.json file.
# jq -r parses the JSON file and extracts key-value pairs. Specifically:
# to_entries[] iterates through all key-value pairs in the JSON.
# "\(.key),\(.value.source)" creates a string in the format key,source, where key is the repository name and source is the Git URL.

# The for loop iterates through each of these formatted strings.
# Extract the Repository Name and Source URL:

#/////////////////////////////////////////////////////////////
# bash
# Copy code

# name=$(echo $bot | cut -d',' -f1);
# source=$(echo $bot | cut -d',' -f2);

# echo $bot | cut -d',' -f1 extracts the repository name (before the comma).
# echo $bot | cut -d',' -f2 extracts the Git source URL (after the comma).
# Clone the Repository:

#///////////////////////////////////////////////////////////
# bash
# Copy code

# git clone $source $name;
# git clone clones the repository from the source URL into a folder named $name.
# Install Python Dependencies:

# bash
# Copy code

# cd $name && pip install --no-cache-dir -r requirements.txt && cd ..;
# cd $name navigates into the cloned repository's directory.
# pip install --no-cache-dir -r requirements.txt installs Python dependencies listed in the requirements.txt file, without caching the packages to save space.
# cd .. returns to the original directory to process the next repository.

# Repeat for All Entries in config.json: The loop continues for every repository defined in config.json.

