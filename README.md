### Scheduling Python scripts with GitHub Actions


This repository contains Python scripts running as cron job with GitHub Actions. There are several fun use cases for 

this. Also since github provides 2000mins/month of gihub actions under its free tier, these can be used in several 

automation projects.


#### Common Basics
Scripts in this repository are meant for different use cases, however they have some similarities

* Environment variables can either be accessed within the main script or referenced as secrets saved within github
* A log file is updated at the succesful execution of the script at its scheduled time
* A workflow YAML file that configures each job in a given script.We can have multiple files for each project in the .github/   workflows folder. So far it is within the limit of a free tier account.


#### Example: Twitter trends

An example script implemented uses `twitter API` to obtain the most trending tweets of the day based on `number of views` for given location,it further logs the response in a `status.log`, and automatically pushes the changes to this repo.

-  `main.py` : Implement script 
- `.github/workflows/actions.yml` : Inspect and configure cron job in GitHub Action 
-  `requirements.txt` : Installs and use third party packages
- `Secret environment variables`: Stores `twitter API`  in github refernced inside the `actions.yml` and `main.py`files

