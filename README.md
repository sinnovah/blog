# A lightweight blog

# Installation

## Installation with a CI/CD pipeline
This repository is set up to automatically deploy to a hosted server using GitHub Actions when code is pushed to the main branch. To set this up, you will need to do the following:
1. Fork this repository and clone it to your local machine.
2. Set up SSH keys on your hosting server, you will need to read the relevant documentation provided by your hosting provider.
3. Add the public key to your GitHub repository:
    - Go to your repo > Settings > Deploy keys.
    - Add a New Deploy Key and paste in the public SSH key.
    - Click Add key.
4. Add secrets to GitHub Actions
Go to your GitHub repository, and under Settings > Secrets and variables > Actions, create the following:
    - ```SSH_PRIVATE_KEY```: Paste your private SSH key here.
    - ```USERNAME```: Your hosting username.
    - ```SERVER```: Your domain name (e.g., ```yourawesomeblog.com```).
    - ```PORT```: The SSH port for your server (default is ```22``` but sometimes hosting providers change this).
    - ```PATH```: The path to your server directory where you want the blog to be deployed. It is recommended to use a directory that is above the ```public_html``` or ```www``` directory if you have access.

## Installation without a CI/CD pipeline
1. Fork this repository and clone it to your local machine.
2. Delete the ```.github\workflows\deploy.yml``` file. This will allow you to run the blog locally without automatically deploying it to a server.