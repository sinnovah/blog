# Installation

- Fork this repository and clone it to your local machine.
- This repository is configured to automatically lint, unit test, and deploy to a hosted server using GitHub Actions whenever code is pushed to the main branch. If you prefer not to set up a production environment, you can simply delete the `.github/workflows/deploy.yml` file.

    However, if you'd like to set up the current deployment workflow, follow these steps:
    - Set up SSH keys on your hosting server, you will need to read the relevant documentation provided by your hosting provider.
    - Add the public key to your GitHub repository:
        - Go to your repo > Settings > Deploy keys.
        - Add a New Deploy Key and paste in the public SSH key.
        - Click Add key.
    - Add secrets to GitHub Actions
    Go to your GitHub repository, and under Settings > Secrets and variables > Actions, create the following:
        - `SSH_PRIVATE_KEY`: Paste your private SSH key here.
        - `USERNAME`: Your hosting username.
        - `SERVER`: Your domain name (e.g., `yourawesomeblog.com`).
        - `PORT`: The SSH port for your server (default is `22` but sometimes hosting providers change this).
        - `BACKEND_PATH`: The path to your server directory where you want the app backend to be deployed. It is recommended to use a directory that is above the `public_html` or `www` directory if you have access.
        - `FRONTEND_PATH`: The path to your server directory where you want the frontend public static files to be deployed. Likely the path to the `public_html` or `www` directory on your server.
        - Push the changes to the main GitHub branch, and the CI/CD pipeline will deploy the blog to your server.
- Create and activate a virtual environment: Run the following in your terminal.
    - Windows:
        ```
        python -m venv venv
        .\venv\Scripts\activate
        ```
    - macOS/Linux:
        ```
        python3 -m venv venv
        source venv/bin/activate
        ```
- Install the required dependencies:
    - For development environment:
        ```
        pip install -r requirements-dev.txt
        ```
    - For production environment:
        ```
        pip install -r requirements.txt
        ```

- Run the following terminal command to start the blog:
    `python app.py`