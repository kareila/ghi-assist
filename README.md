# ghi-assist
Bot that organizes Github Issues

## Installation
    (virtualenv preferred)
    python setup.py install

## Tests
    py.test tests

## Setup
### Server
A sample configuration file is provided in `etc/config/sample.json`

    cp etc/config.sample.json etc/config.json

### Bot
- [ ] Create a new Github account to serve as your bot
- [ ] Give the bot admin access
    * For organization repos, add to a team with write access
    * For personal repos, add as a collaborator:

        https://github.com/USERNAME/REPO/settings/collaboration

- [ ] Create an API token for the bot with permissions "public_repo":

    https://github.com/settings/tokens/new

- [ ] Add API token to the config

### Secret
- [ ] Create a secret token as per https://developer.github.com/webhooks/securing/
- [ ] Add this secret token to the config

### Webhook
- [ ] Create the webhook https://github.com/USERNAME/REPO/settings/hooks -> Add webhook
- [ ] Configure the webhook:
    * Secret is the secret token from the previous step
    * You only need to care about the "Issues", "Pull Request", and "Issue comment" events

## Running

    python bin/server.py