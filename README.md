### Scheduling python scripts as cron jobs with GitHub Actions


This repository contains Python scripts running as cron job with GitHub Actions. There are several fun use cases for 

this. Also since github provides 2000mins/month of gihub actions under its free tier, this can be used in several 

automation projects like this one.


#### Common Basics
Scripts in this repository are meant for different use cases, however some similarities may include.

* Credentials and API Keys can be acessed as environment variables within the main script or referenced as secrets saved within github
* A log file that is updated at the succesful execution of the script at its scheduled time
* A workflow YAML file that configures each job in a given script.We can have multiple of such files in the .github/workflows folder. 


#### Example: Twitter_trends.py

An example script implemented uses `twitter API` to obtain the most trending tweets of the day based on `number of views` for given location,it further logs the response in a `twitter_trends.log` file, and automatically pushes the changes to this repo.

-  `twitter_trends.py` : Implement script 
- `.github/workflows/twitter_cronjobs.yml` : Inspect and configure cron job in GitHub Action 
-  `requirements.txt` : Installs and use third party packages
- `Secret environment variables`: Stores `twitter API`  in github referenced inside the `twitter_cronjobs.yml` and `twitter_trends.py`files

