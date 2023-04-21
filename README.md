### Scheduling Python scripts with GitHub Actions


This project shows how to run a Python script as cron job with GitHub Actions. It calls a `twitter API` once a day to obtain the most trending tweets of the day based on `number of views` for given location, logs the response in `status.log`, and automatically pushes the changes to this repo.

- Implement your script in `main.py`
- Inspect and configure cron job in GitHub Action `.github/workflows/actions.yml`
- It can install and use third party packages from `requirements.txt`
- Secret environment variables is used to store `twitter API`, used inside the `actions.yml` and `main.py`files
