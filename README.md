# Backend generic for ERP or Ecommerce
This is a project in development, is not ready for production. In this project only is the backend, the frontend is in another project. [frontenderp.com](https://frontenderp.com)

## Website: [backenderp.com](https://backenderp.com)

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

# How use
```
http://localhost:8000/doc/
http://localhost:8000/admin/
http://localhost:8000/redoc/
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

# Plan of the project
This is the plan of the project.
1. The user can register and change the password.
2. The user can login and logout.
3. The user can change the language.
4. The user can change the company.
5. The user can change the theme.
6. The user can sale one product.
7. The user can sale many products.
8. The user can sale from the website.
9. The user can sale from the website course.
10. Create the invoice.
11. Create the payment.
12. Create the picking.
13. ...


# Apps and Modules
This is the list of apps and modules that are in the project.

# con (Contact)
App to manage the contacts.
- [x] contact
- [x] state
- [x] country

# inv (Stock)
App to manage the stock.
- [x] contact
- [x] product
- [x] uom
- [x] category
- [x] warehouse
- [x] location
- [x] brand
- [x] model
- [ ] picking
- [ ] pickingLine 

# sal (Sale)
App to manage the sales.
- [x] saleOrder
- [x] saleOrderLine
- [ ] report

# pur (Purchase)
App to manage the purchases.
- [x] purchaseOrder
- [ ] purchaseOrderLine
- [ ] report

# acc (Account)
App to manage the account.
- [x] tax
- [x] currency
- [x] journal
- [ ] Account Account
- [ ] Account Invoice
- [ ] Account Move
- [ ] Account Analytic
- [ ] Payment

# conf (Configuration)
App to manage the configuration.
- [x] configuration
- [x] cron
- [x] Log
- [ ] Files
- [ ] Backup
- [x] Note
- [x] Parameter
- [ ] Email
- [ ] EmailServer
- [x] Sequence
- [x] language
- [ ] EmailLog
- [ ] Theme

# crm (Customer Relationship Management)
App to manage the crm.
- [ ] lead
- [ ] opportunity

# mkt (Marketing)
App to manage the marketing.
- [ ] Campaign

# pry (Project)
App to manage the project.
- [x] Project
- [x] Task
- [ ] Ticket

# hr (Human Resources)
App to manage the human resources.
- [ ] employee
- [ ] department
- [ ] job
- [ ] contract

# web
App to manage the web.
- [ ] website
- [ ] page
- [x] post
- [ ] comment
- [ ] rating
- [ ] menu
- [ ] slider
- [ ] faq

# Comunication
App to manage the comunication.
- [ ] message
- [ ] channel
- [ ] chat

# elr (eLearning)
App to manage the eLearning.
- [x] course
- [x] lesson









