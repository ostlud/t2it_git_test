wordwide = ('xxs', 'xs', 's', 'm', 'l', 'xl','xxl', 'xxxl')
country = ('ua', 'de', 'us', 'fr', 'uk')

num_xxs = [42, 36, 8, 38, 24]
num_xs = [i+2 for i in num_xxs]
num_s = [i+2 for i in num_xs]
num_m = [i+2 for i in num_s]
num_l = [i+2 for i in num_m]
num_xl = [i+2 for i in num_l]
num_xxl = [i+2 for i in num_xl]
num_xxxl = [i+2 for i in num_xxl]

my_dict = dict(zip(wordwide,
                    (dict(zip(country, num_xxs)),
                     dict(zip(country, num_xs)),
                     dict(zip(country, num_s)),
                     dict(zip(country, num_m)),
                     dict(zip(country, num_l)),
                     dict(zip(country, num_xl)),
                     dict(zip(country, num_xxl)),
                     dict(zip(country, num_xxxl)))))

print(my_dict['xxs']['ua'])

