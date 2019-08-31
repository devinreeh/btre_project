# Real Estate Viewing Platform Example Django Project



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
