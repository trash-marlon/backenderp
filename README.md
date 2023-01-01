# Backend generic for ERP or Ecommerce
## Website
[backenderp.com](https://backenderp.com)

# How install
```
git clone https://github.com/falconsoft3d/backenderp.git
cd backenderp
source env/bin/activate
pip install -r requirements.txt
python manage.py runserver
```

# Django
```
python manage.py startapp www
```

# Libraries
```
Python==3.9.15
Django==4.1.4
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







