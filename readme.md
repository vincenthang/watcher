# Watcher

A python script to back up Blink video footage to your local drive, from the cloud.

## How to use

### Continuous Backup
Complete [installation](#installation), then setup a daily cron job that runs `run_cron.py` at least once a day for continuous back-up. Make sure to set environment variables for your Blink login.

Set username and password (can be done in startup profile, or passed-through during the run command):
```bash
export BLINK_USERNAME=<USERNAME_REDACTED>
export BLINK_PASSWORD=<PASSWORD_REDACTED>
```
Then run your cron job on :
```
# Example for every 12 hours
CRON EXPRESSION: 0 0 */12 ? * *
CRON JOB: poetry run python run_cron.py
```
The downloads will be sent to `./video_backup` unless otherwise specified with `-f <DIRECTORY>` running `run_cron.py`.

### Download All Footage Off The Cloud
The script allows you to download all footage off the cloud. Complete [installation](#installation), then do the following.

Set username and password (can be done in startup profile, or passed-through during the run command):
```bash
export BLINK_USERNAME=<USERNAME_REDACTED>
export BLINK_PASSWORD=<PASSWORD_REDACTED>
```
Run `run_cron.py`
```bash
poetry run python run_cron.py --all
```
The downloads will be sent to `./video_backup` unless otherwise specified with `-f <DIRECTORY>` running `run_cron.py`.




## Installation
Requires `python 3.7.6`:
```bash
pyenv install 3.7.6
pyenv virtualenv 3.7.6 watcher
pyenv local watcher
poetry install
```

## Development

Complete [installation](#installation), then install pre-commit.
```bash
poetry pre-commit install
```
### Testing
This project uses `pytest`.
```bash
poetry run pytest
```
