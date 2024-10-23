# PollHub
PollHub is a simple web app for creating and sharing polls built with Django and powered by PostgreSQL for reliable data management. Deployed on Railway for testing purposes it offers fast secure and scalable performance for real-time survey results.

## Prerequisites
- **Python 3.12** installed
- **Railway** account for deployment
- **GitHub** repository to link with Railway

## Project Setup
1. **Clone the repository**
```bash
    git clone https://github.com/0xshr00msz/pollhub.git
    cd pollhub
```
2. **Set up the virtual environment**

    Create a virtual environment and activate it 
```bash
    python3 -m venv .venv
    source .venv/bin/activate
```
3. **Install Dependencies**
```bash
    pip install -r requirements.txt
```

## Deets and Customization
1. This Django project contains one app called `ask`. Go to the templates located at `ask/templates/ask` and modify `index.html` to suit your preferences. Feel free to customize the texts inside the `<script>`

    ```html
    <h1 class="p-3">Hi Name!</h1>
    <div id="displayText" class="mb-3 px-5">
        Click to reveal messages hehez
    </div>
    <button class="btn btn-primary mb-3" onclick="changeText()">Click me!</button>

    <h2 class="p-4">Insert cheesy question here</h2>
    ```

2. **Models**: PollHub has one model `Question` with only one field `answer` to represent users' answer YES or NO. 1=Yes and 2=No

    ```python
    class Question(models.Model):
        answer = models.CharField(max_length=1)
    ```
3. **Forms**: This project has one form `QuestionForm` for selecting between "Yes" and "No" options, displayed as radio buttons. Used to collect the responses of your crush/es, sheesh! The `CHOICES` list defines each option with an internal value ('1' for "Yes" and '2' for "No") and a label for display.

    ```python
    class QuestionForm(forms.Form):
        CHOICES = [('1', 'Yes'), ('2', 'No')]
        answer = forms.ChoiceField(choices=CHOICES, widget=forms.RadioSelect)
    ```

4. **admin.py**: This registers the `Question` model to the Django admin site, providing an interface for administrators to manage its instances. This registration enables easy addition, editing, and deletion of `Question` records without requiring additional coding, streamlining administrative tasks.

    ```python
    admin.site.register(Question)
    ```
    After registering the model, create an administrative user with full access to the Django admin interface, enabling the management of site content and user accounts.

    ```bash
    python manage.py createsuperuser
    ```
    **Enter Superuser Information**: Username, Email, and Password
    
    _Example Prompt_:
    ```bash
    Username (leave blank to use 'yourusername'): admin
    Email address: admin@example.com
    Password: 
    Password (again): 
    ```

## Configuration
1. **Initialize `.env` file**: Create a `.env` file in the project root with the following environment variables:

```
    ENVIRONMENT=development
    SECRET_KEY=
    DB_NAME=
    DATABASE_URL=
    DB_USER=
    DB_PASSWORD=
    DB_HOST=
    DB_PORT=
```
2. Project settings in your Django `settings.py` file, located at `pollhub/pollhub/settings.py`:
    
    - Import environment variables
    ```python
    import os
    import dj_database_url
    ```

    - Transfer Django's secret key to `.env`. From settings.py cut the secret key and paste it into the .env `SECRET_KEY`. Replace it with the code below.
    ```python
    SECRET_KEY = env('SECRET_KEY')
    ```
    
    Configure `DATABASES` to use Postgresql from `DATABASE_URL`:

    ```python
    POSTGRES_LOCALLY = False
    if ENVIRONMENT == 'production' or POSTGRES_LOCALLY == True:
        DATABASES['default'] = dj_database_url.parse(env('DATABASE_URL'))
    ```

## Preparing for Deployment
1. Create required files:
    - Procfile (to run the app)
    ```plaintext
    web: gunicorn pollhub.wsgi --log-file -
    ```

    - `runtime.txt` (to specify python version)
    ```plaintext
    Python-3.12.3
    ```

## Create the PostgreSQL Database in Railway
1. Go to Railway dashboard
2. Click `Provision PostgreSQL`

>After deploying the database, connect the database to our django app.

3. Click the postgresql and go to `variables` tab.
4. Copy the `DATABASE_URL`, the public one. Paste it to the `.env`.
5. Copy all the needed info to the `.env` accordingly.

    ```plaintext
    ENVIRONMENT=development
    SECRET_KEY=your-secret-key
    DB_NAME=your-db-name
    DATABASE_URL=your-db-url from postgressql railway
    DB_USER=your-postgresql-db-user
    DB_PASSWORD=your-postgres-password
    DB_HOST=your-postgres-host
    DB_PORT=your-postgresql-port
    ```
6. Run `makemigrations` and `migrate`

    makemigrations
    ```bash
    python manage.py makemigrations
    ```
    
    migrate
    ```bash
    python manage.py migrate
    ```
5. Make sure there are no errors.
6. Go to the `data` tab and click the table/model that you have from the django app.

## Deploy to Railway
1. **Push Code to GitHub**: Push your project to a GitHub repository.


3. **Link GitHub to Railway**
    - Sign in to Railway
    - From the right side of the dashboard, click `New` and `GitHub Repo` to connect github repository.
    - Choose your repository and link it.
4.  Click deploy located at the top of the dashboard.
5. Once deployed, click it and go to the `settings` tab. Scroll down and locate the `Networking` section. Generate domain, you can edit it or leave it as it is, and now you have it.
6. Copy the domain and paste it in the `settings.py` allowed hosts.
    ```python
    ALLOWED_HOSTS = ['your-domain-here', 'localhost', '127.0.0.1']
    ```
7. We also need the `CSRF_TRUSTED_ORIGINS`:
    ```python
    CSRF_TRUSTED_ORIGINS = ['your-deployed-url-here']
    ```
    >Example: https://your-domain-here

8. Now, check your website.
9. For responses, go to the Postgresql Database to view the responses.
## Notes
- Remember to set DEBUG=False in production.
- Be sure to replace placeholder values with actual credentials and configuration details.


