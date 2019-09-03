# Real Estate Viewing Platform Example Django Project
## Purpose
BT Real Estate is a mock Residential Real Estate Company used to demonstrate the Django framework. This project used Python 3.7.4, Django 2.2.4. ~~The website can be viewed here. No domain name was purchased for this website. Please mind the ugly URL. [BT Real Estate website]()~~


Make sure that you have django and python installed. To start up python virtual environment:
```python
source venv/bin/activate
python manage.py runserver
```
Pip Dependencies List:
```python
autopep8        1.4.4
Django          2.2.4
Pillow          6.1.0
pip             19.0.3
psycopg2-binary 2.8.3
pycodestyle     2.5.0
pytz            2019.2
setuptools      40.8.0
sqlparse        0.3.0
```

## Some Core Features
### As a site visitor, you can:
1. View listings
2. Search Listings
3. Email Realtors about listings
4. Read about the company and its realtors

### As a realtor, you can:
1. You can receive emails about listings you are showing

### As a site admin, you can
1. edit the data entries
2. choose featured Realtors
3. create, read, update, or delete realtor profiles, listings, or users who have reached out about particular Listing

## Some Cool Things:
1. This website includes pagination
2. Admin can view Python models in table form and even edit some of the boolean Fields
3. You can create an account which records the listings a user has tried to contact a realtor about

## Some General User Stories
### As a site visitor, you can
 1. View Commercial Real Estate Properties in a list view
 2. View Commercial Real Estate Properties in a single in depth view
 3. See what the latest featured listings are
 4. Search for properties based on where they are
 5. Paginate through the listings in the featured listings tab
 6. Search for home based on:
 ..* keywords in the description
 ..* city (case insensitive, exact match)
 ..* state (exact match)
 ..* bedrooms (entry is upper bound on range example <4 rooms)
 ..* price (entry is upper bound on range example <$800,000 rooms)

### As a site admin, you can
1. Create/Read/Update/Delete Realtors
2. Create/Read/Update/Delete Listings
... and enabled quick view functionalities
..* Searchable by title, description, address, city, state, zip code, and price
..* Editable by whether a property is published or not
..* Filterable by realtor, price, and list date
3. Moderate whether a listing is published (boolean is_published)
3. Other outbox

## Next Steps:
* Deploy Project to a a prouction server for viewing
* Use React as the view layer instead of normal javascript and jquery
* Build a more robust RestAPI and Routing system
* Write tests for the backend API
