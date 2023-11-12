# Climate Wavers - Django Server

<img width="1000" alt="image" src="https://github.com/Olagold-hackxx/ClimateWavers2/assets/133222922/bd3a5667-d3cd-48d9-b6d6-c8ac673dd49f">

The Django Server microservice of Climate wavers is responsible for handling core functionalities, user management, and data processing tasks. Built on the Django rest framework, this server provides a robust and secure backend for the application.

## Table of Contents

- [Climate Wavers - Django Server](#climate-wavers---django-server)
  - [Table of Contents](#table-of-contents)
  - [Project Overview](#project-overview)
  - [Features](#features)
  - [Installation and Setup](#installation-and-setup)
    - [Setting up a MariaDB Database](#setting-up-a-mariadb-database)
    - [Starting MariaDB](#starting-mariadb)
  - [Environment Variables](#environment-variables)
  - [License](#license)

## Project Overview

The Climate Change and Disaster Response Platform aims to monitor climate changes, predict natural disasters, and facilitate efficient disaster response. Leveraging Django, the server component ensures seamless user experience, data management, and integration with various data sources.

## Features

- **User Authentication:** Secure user registration, login, and profile management.
- **Data Management:** Store and manage user data, community information, and datasets.
- **Real-time Data Processing:** Process incoming data streams for analysis and visualization.
- **Collaborative Communities:** Enable users to form communities, share observations, and collaborate.
- **API Endpoints:** Provides RESTful APIs for frontend interaction and external integrations.

## Installation and Setup

1. **Clone the Repository:**
   ```bash
   https://github.com/ClimateWavers/backend.git
   cd backend
   ```
2. **Create virtual environment:**
  ```bash
  python3 -m venv myenv -- "Name of the virtual environment"
  ```
  - Activate virtual environment:
  ```bash
  source myenv/bin/activate
  ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Database Setup:**
   - Configure the database settings in `settings.py`.
   - Run migrations:
     ```bash
     python manage.py migrate
     ```

5. **Static and Media Files:**
   - Collect static files:
     ```bash
     python manage.py collectstatic
     ```
   - Configure media file settings in `settings.py`.

6. **Run the Django Development Server:**
   ```bash
   python manage.py runserver
   ```

   The Django server will be available at `http://localhost:8001`.

## Setting up a MariaDB Database

### Install MariaDB
If you haven't already, you need to install MariaDB on your server or local development environment. You can download MariaDB from the [official website](https://mariadb.org/).

### Database Configuration
1. Open your Django project's `settings.py`.
2. Locate the `DATABASES` section.
3. Configure the database settings. Here's an example configuration for MariaDB:

   ```python
   # ... (Your existing settings)
   DATABASES = {
       'default': {
           'ENGINE': 'django.db.backends.mysql',
           'NAME': 'your_database_name',
           'USER': 'your_database_user',
           'PASSWORD': 'your_database_password',
           'HOST': 'localhost',  # Set the host where your MariaDB is running
           'PORT': '3306',  # Default MariaDB port
       }
   }
	```

## Setup MariaDB
To start MariaDB, refer to the database microservice repository `https://github.com/ClimateWavers/database` or the branch - database, at development repository `https://github.com/Olagold-hackxx/ClimateWavers`
    
## Environment Variables

- **SECRET_KEY:** Django secret key for security 
- **DEBUG:** Set to `True` for development, `False` for production.
- **ALLOWED_HOSTS:** List of allowed hostnames for the Django server.
-  **MARIADB_PASSWORD:** Database Password
-  **MARIADB_USER:** Database user
-  **VERIFICATION_MAIL:** Personalized verification mail
-  **DOMAIN:** Application domain or frontend url
-  **APP_EMAIL:** Application email
-  **MARIADB_DB_NAME:** Database name
-  **MARIADB_PORT:** Database port, 3306 default value for mariadb
-  **MARIADB_SERVER:** Database host, localhost on development environment, database service name on openshift cluster
-  **BACKEND:** 


## License

This project is licensed under the [MIT License](LICENSE).
