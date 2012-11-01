# GAE Flask Template

This project's goal is to get you up and running quickly with Flask on Google App Engine. It includes a basic app framework along with the necessary libraries to run Flask in development and in production.

## Getting Started

Begin by cloning this repository to your development machine. Install the dependencies using:

    pip install -r requirements.txt

Next, update the first line of `app.yaml` to use your app name instead of `your-gae-flask-app`. Also, update `app/settings.py`, setting `ADMIN_EMAILS` to be the emails of any admins for the app and `SECRET_KEY` to be a random string.

## Deploying

There is a [Fabric](http://fabfile.org/) script which contains a simple deployment script. To deploy your project, simply run:

    fab deploy

The first time you deploy, the script will take you to an OAuth2 page to authorize you.

## Included Libraries

* [Flask](http://flask.pocoo.org/) - [License](http://flask.pocoo.org/docs/license/)
* [Jinja2](http://jinja.pocoo.org/) - [License](https://github.com/mitsuhiko/jinja2/blob/master/LICENSE)
* [Werkzeug](http://werkzeug.pocoo.org/) - [License](https://github.com/mitsuhiko/werkzeug/blob/master/LICENSE)
* [Werkzeug Debugger Appengine](https://github.com/daaku/werkzeug-debugger-appengine)
* [GAE Mini Profiler](https://github.com/kamens/gae_mini_profiler) - [License](http://en.wikipedia.org/wiki/MIT_License)

## Example

[your-gae-flask-app.appspot.com](http://your-gae-flask-app.appspot.com/)