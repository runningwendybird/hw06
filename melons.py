melon_name = {
    1: "Honeydew",
    2: "Crenshaw",
    3: "Crane",
    4: "Casaba",
    5: "Cantaloupe",
}

melon_price = {
    1: 0.99,
    2: 2.00,
    3: 2.50,
    4: 2.50,
    5: 0.99,
}

melon_seedless = {
    1: True,
    2: False,
    3: False,
    4: False,
    5: False,
}


melon_master = {}

# This for loop creates a dictionary to
# more easily access our information.
# I have also added 'flesh', 'rind', and 'avg_wt'
# Though they are currently going to be None
# for all melons currently. As we get more information
# we can replace None with the acutal value\
# or add other properties. 

for melon in melon_name:
    melon_master[melon_name[melon]] = {
        'price': melon_price[melon],
        'seedless': melon_seedless[melon],
        'flesh': None,
        'rind': None,
        'avg_wt': None
    }


print melon_master
