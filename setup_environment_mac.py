import subprocess
# Create a virtual environment within your local repository to which you pulled the GitHub repo.
subprocess.run('python3 -m venv BICAMS_norm_venv')

# Activate the virtual environment
subprocess.run('source BICAMS_norm_venv/bin/activate')

# Install all dependencies
subprocess.run('pip3 install -r dependencies.txt')