# book-site
####Catalogue site for publisher

* Django 1.9
* Python 3
* Postgres
* Redis Cache
* Amazon S3 / Boto
* Sorl-Thumbnail

####Demo version on [Heroku](http://book-site.herokuapp.com)



**To run locally:**

1. Clone the repo
2. Install Postgres & Redis
3. Set up your env.
4. Install Postgres & Redis
5. Add your AWS Keys
6. Install dependencies: `pip install -r requirements.txt`
7. Migrate db: `python manage.py migrate`
8. Run redis-server 
9. Fire up Django's server: `python manage.py runserver`


