import os
# Create a virtual environment within your local repository to which you pulled the GitHub repo.
os.system('python3 -m venv BICAMS_norm_venv')

# Activate the virtual environment
os.system('BICAMS_norm_venv\Scripts\activate')

# Install all dependencies
os.system('pip3 install -r dependencies.txt')