# Backend generic for ERP or Ecommerce
## Website
[backenderp.com](https://backenderp.com)

# How install
```
git clone https://github.com/falconsoft3d/backenderp.git
cd backenderp
git checkout dev
virtualenv env --python=python3
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
python manage.py runserver --settings app.settings.dev
```

# Django
```
python manage.py startapp www
python manage.py makemigrations
python manage.py migrate
```

# Update the libraries requirements
```
pip freeze > requirements.txt
```

# How install with docker local
```
docker run -d -p 8000:8000 mfalconsoft/caprover-django
```

# How update if you have docker local
```
docker build -t mfalconsoft/backenderp .
docker push mfalconsoft/backenderp
docker images
docker run -d -p 8000:8000 mfalconsoft/caprover-django
```

# My contact data
```
Marlon Falcón Hernández | Valencia | Spain
* ERP, CRM y Software: https://www.marlonfalcon.com
» Email: mfalconsoft@gmail.com , falconsof.3d@gmail.com
» Github: https://github.com/falconsoft3d
» linkedin: https://linkedin.com/in/marlon-falcón-3a2aa9a4
```

# Apps and Modules
## Doing
| number | short name | name             | note |
|--------|------------|------------------|------|
| 1      | base       | Module base      | -    |
| 2      | users      | Module for users | -    |
| 3      | web        | Website          | -    |
| 4      | inv        | Stock            | -    |
| 5      | con        | Contact          | -    |
| 6      | acc        | Account          | -    |
| 7      | www        | Simple Web       | -    |

# con (Contact)
- [x] contact
- [x] state
- [x] country

# inv (Stock)
- [x] contact
- [x] product
- [x] uom
- [x] category
- [ ] warehouse
- [ ] location

# sal (Sale)
- [x] saleOrder

# pur (Purchase)
- [x] purchaseOrder

# acc (Account)
- [x] tax
- [x] currency

# conf (Configuration)
- [x] configuration
- [x] cron

# web
- [x] post
- [ ] comment









