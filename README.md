# bikes-perf

## How to deploy
- `heroku create --app app-name-here`
- `heroku git:remote -a app-name-here`
- `heroku config:set DJANGO_SETTINGS_MODULE=core.settings.production`
- `heroku config:set 'SECRET_KEY=secret-key-here'`
- `heroku addons:create heroku-postgresql:hobby-dev`
- `git push heroku master`
- `heroku run python manage.py migrate`
# hackathon
# hackathon
