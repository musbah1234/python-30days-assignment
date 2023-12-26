# Given list of countries
names = ['Finland', 'Sweden', 'Norway', 'Denmark', 'Iceland', 'Estonia', 'Russia']

# Unpack the first five countries
nordic_countries = names[:5]

# Unpack Estonia and Russia
es, ru = names[5:7]

# Print the results
print("Nordic Countries:", nordic_countries)
print("Estonia:", es)
print("Russia:", ru)
