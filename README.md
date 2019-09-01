# Real Estate Viewing Platform Example Django Project
## Overview
BT Real Estate is a mock Residential Real Estate Company used to demonstrate the Django framework. This project used Python 3.7.4, Django 2.2.4. The website can be viewed here. No domain name was purchased for this website. Please mind the ugly URL. [BT Real Estate website](https://www.google.com)

## Some General User Stories
#### As a site visitor, you can
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



#### As a site admin, you can
1. Create/Read/Update/Delete Realtors
2. Create/Read/Update/Delete Listings
... and enabled quick view functionalities
..* Searchable by title, description, address, city, state, zip code, and price
..* Editable by whether a property is published or not
..* Filterable by realtor, price, and list date
3. Moderate whether a listing is published (boolean is_published)
3. Other outbox



## Mapping out the Database, Models, and Fields

### Listing
id: INT

realtor: INT (foreign key [realtor])

title: STR
address: STR
city: STR
state: STR
zipcode: STR
description: TEXT
price: INT
bedrooms: INT
bathrooms: INT
garage: INT
sqft: INT
lot_size: FLOAT
is_published: BOOL [TRUE]
list_date: DATE
photo_main: STR
photo_1: STR
photo_2: STR
photo_3: STR
photo_4: STR
photo_5: STR
photo_6: STR

### Realtor
id: INT
name:  STR
photo: STR
description: STR
email: STR
phone: STR
is_mvp: BOOL [0]
hire_date: DATE

### Contact
id: INT
user_id: INT
listing: INT
listing_id: INT
name: STR
email: STR
phone: STR
message: TEXT
contact_date: DATE
