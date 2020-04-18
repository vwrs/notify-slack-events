notify-slack-events
===

Send [Slack API Events](https://api.slack.com/events) notifications to Slack
using [python-slack-events-api](https://github.com/slackapi/python-slack-events-api).

## Create a Slack app
- Create a Slack app on https://api.slack.com/apps
- Set Permissions, Incoming Webhooks and Event Subscriptions.
  - Subscribe API event types (e.g. `user_change`) you want to track.
  - Request URL should be 'https://xxx.herokuapp.com/slack/events'.

## Deploying to Heroku
- Deploy your Heroku app. e.g.) run the following command:
```sh
$ heroku create
$ heroku git:remote -a <Heroku app's name>
$ git push heroku master
```

or

[![Deploy](https://www.herokucdn.com/deploy/button.svg)](https://heroku.com/deploy)

- Define `SLACK_SIGNING_SECRET` and `WEBHOOK_URL` as Heroku Config Vars.

## Documentation

For more information, see these documents:

- [API Events | Slack](https://api.slack.com/events)
- [slackapi/python-slack-events-api](https://github.com/slackapi/python-slack-events-api)
- [Python on Heroku](https://devcenter.heroku.com/categories/python)
