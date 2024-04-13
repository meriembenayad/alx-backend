## 02 - i18n

### Resources

- [Flask-Babel](https://web.archive.org/web/20201111174034/https://flask-babel.tkte.ch/ "Flask-Babel")
- [Flask i18n tutorial](https://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-xiii-i18n-and-l10n "Flask i18n tutorial")
- [pytz](https://pypi.org/project/pytz/ "pytz")

### Tasks

<details>
<summary>0. Basic Flask app</summary>

1. Setup a basic Flask app in `0-app.py`.
2. Create a single `/` route and an `index.html` template that simply outputs “Welcome to Holberton” as page title (`<title>`) and “Hello world” as header (`<h1>`).

**Files:**

- `0-app.py`
- `templates/0-index.html`
</details>

<details>
<summary>1. Basic Babel setup</summary>

1. Install the Babel Flask extension:

```sh
$ pip3 install flask_babel==2.0.0
```

2. instantiate the Babel object in your app. Store it in a module-level variable named `babel`.
3. In order to configure available languages in our app, you will create a `Config` class that has a `LANGUAGES` class attribute equal to `["en", "fr"]`.
4. Use `Config` to set Babel’s default locale (`"en"`) and timezone (`"UTC"`).
5. Use that class as config for your Flask app.

**Files:**

- `1-app.py`
- `templates/1-index.html`
</details>

<details>
<summary>2. Get locale from request</summary>

1. Create a `get_locale` function with the `babel.localeselector` decorator.
2. Use `request.accept_languages` to determine the best match with our supported languages.

**Files:**

- `2-app.py`
- `templates/2-index.html`
</details>

<details>
<summary>3. Parametrize templates</summary>

Use the `_` or `gettext` function to parametrize your templates.,Use the message IDs `home_title` and `home_header`.
Create a `babel.cfg` file containing

```python
[python: **.py]
[jinja2: **/templates/**.html]
extensions=jinja2.ext.autoescape,jinja2.ext.with_
```

Then initialize your translations with

```sh
$ pybabel extract -F babel.cfg -o messages.pot .
```

and your two dictionaries with

```sh
$ pybabel init -i messages.pot -d translations -l en
$ pybabel init -i messages.pot -d translations -l fr
```

Then edit files `translations/[en|fr]/LC_MESSAGES/messages.po` to provide the correct value for each message ID for each language. Use the following translations:

| msgid         | English                  | French                       |
| ------------- | ------------------------ | ---------------------------- |
| `home_title`  | `"Welcome to Holberton"` | `"Bienvenue chez Holberton"` |
| `home_header` | `"Hello world!"`         | `"Bonjour monde!"`           |

Then compile your dictionaries with

```sh
$ pybabel compile -d translations
```

Reload the home page of your app and make sure that the correct messages show up.

**Files:**

- `3-app.py`
- `babel.cfg`
- `templates/3-index.html`
- `translations/en/LC_MESSAGES/messages.po`
- `translations/fr/LC_MESSAGES/messages.po`
- `translations/en/LC_MESSAGES/messages.mo`
- `translations/fr/LC_MESSAGES/messages.mo`
</details>

<details>
<summary>4. Force locale with URL parameter</summary>

In this task, you will implement a way to force a particular locale by passing the `locale=fr` parameter to your app’s URLs.

In your `get_locale` function, detect if the incoming request contains `locale` argument and ifs value is a supported locale, return it. If not or if the parameter is not present, resort to the previous default behavior.

Now you should be able to test different translations by visiting `http://127.0.0.1:5000?locale=[fr|en]`.

**Visiting `http://127.0.0.1:5000/?locale=fr` should display this level 1 heading:**

```html
Bonjour monde!
```

**Files:**

- `4-app.py`
- `templates/4-index.html`
</details>

<details>
<summary>5. Mock logging in</summary>

Creating a user login system is outside the scope of this project. To emulate a similar behavior, copy the following user table in `5-app.py`.

```python
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}
```

This will mock a database user table. Logging in will be mocked by passing `login_as` URL parameter containing the user ID to log in as.

Define a `get_user` function that returns a user dictionary or `None` if the ID cannot be found or if `login_as` was not passed.

Define a `before_request` function and use the `app.before_request` decorator to make it be executed before all other functions. `before_request` should use `get_user` to find a user if any, and set it as a global on `flask.g.user`.

In your HTML template, if a user is logged in, in a paragraph tag, display a welcome message otherwise display a default message as shown in the table below.

| msgid           | English                                | French                                           |
| --------------- | -------------------------------------- | ------------------------------------------------ |
| `logged_in_as`  | `"You are logged in as %(username)s."` | `"Vous êtes connecté en tant que %(username)s."` |
| `not_logged_in` | `"You are not logged in."`             | `"Vous n'êtes pas connecté."`                    |

**Visiting `http://127.0.0.1:5000/` in your browser should display this:**

```html
Hello world! You are not logged in
```

**Visiting `http://127.0.0.1:5000/?login_as=2` in your browser should display this:**

```html
Hello world! You are logged in as Beyonce
```

**Files:**

- `5-app.py`
- `templates/5-index.html`
</details>
