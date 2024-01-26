# Logistics Demo App

![Postgres](https://img.shields.io/badge/postgres-%23316192.svg?style=for-the-badge&logo=postgresql&logoColor=white)
	![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![Swagger](https://img.shields.io/badge/-Swagger-%23Clojure?style=for-the-badge&logo=swagger&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![JWT](https://img.shields.io/badge/JWT-black?style=for-the-badge&logo=JSON%20web%20tokens)

## Description

The application is a model of a network for selling goods. The network is a hierarchical structure of 3 levels:
* Factory;
* Retail network;
* Individual entrepreneur.

Each link in the network refers to only one equipment supplier (not necessarily the previous one in the hierarchy). 
It is important to note that the hierarchy level is determined not by the name of the link, but by its relationship 
to other elements of the network, i.e. The plant is always at level 0, and if the retail network relates directly 
to the plant, bypassing other links, its level is 1.

## Installation

Follow these steps:

1. **Clone repo**:
   ```bash
   https://github.com/ShadeSWD/logistics.git
   ```
2. **Install dependencies::**
   ```bash
   cd price-maker
   poetry init
   ```
3. **Setup environment:**
    use template in .env.sample
4. **Perform migrations:**
   ```bash
   python manage.py migrate
   ```
5. **Run app:**
   ```bash
   python manage.py runserver
   ```
6. **Open app:** 
    The app is ready to process requests
7. **Create superuser:**
    ```bash
       python manage.py createsuperuser
   ```
8. **Create vendor:** Now, when you created a superuser, you can log in and create vendors at <your_host>/users/

To load data from fixtures run:
```bash
    manage.py loadddata fixtures/vendors_data.json
```

To dump data from fixtures run:
```bash
    manage.py dumpdata --indent=2 users > fixtures/vendors_data.json
```

## Docs:
    
Docs are available at:
- <your_host>/swagger/
- <your_host>/redoc/