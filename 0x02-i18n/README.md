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
2. instantiate the Babel object in your app. Store it in a module-level variable named babel.
3. In order to configure available languages in our app, you will create a Config class that has a LANGUAGES class attribute equal to ["en", "fr"].
4. Use Config to set Babel’s default locale ("en") and timezone ("UTC").
5. Use that class as config for your Flask app.

**Files:**

- `1-app.py`
- `templates/1-index.html`
</details>
