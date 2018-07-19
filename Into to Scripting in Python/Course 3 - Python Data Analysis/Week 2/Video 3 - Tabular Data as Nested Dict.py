"""
Course 3
Week 2 - Video 3 - Tabular Data as a Nested Dictionary
"""


def space():
    print('')


space()

# Top 10 software products with the most vulnerabilities in 2017
# (through August).
vulnerabilities2017 = {
    'Android': {'vendor': 'Google',
                'type': 'Operating System',
                'number': 564},
    'Linux Kernel': {'vendor': 'Linux',
                     'type': 'Operating System',
                     'number': 367},
    'Imagemagick': {'vendor': 'Imagemagick',
                    'type': 'Application',
                    'number': 307},
    'IPhone OS': {'vendor': 'Apple',
                  'type': 'Operating System',
                  'number': 290},
    'Mac OS X': {'vendor': 'Apple',
                 'type': 'Operating System',
                 'number': 210},
    'Windows 10': {'vendor': 'Microsoft',
                   'type': 'Operating System',
                   'number': 195},
    'Windows Server 2008': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 187},
    'Windows Server 2016': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 183},
    'Windows Server 2012': {'vendor': 'Microsoft',
                            'type': 'Operating System',
                            'number': 176},
    'Windows 7': {'vendor': 'Microsoft',
                  'type': 'Operating System',
                  'number': 174}
}

# display table
print('Product               Vendor        Type              Vulnerabilities')
print('---------------------------------------------------------------------')
for product, values in vulnerabilities2017.items():
    row = '{:21} {:13} {:18} {:8}'.format(
        product,
        values['vendor'],
        values['type'],
        values['number']
    )
    print(row)

space()

# we can then print out specific information.
# in this case it's simple because we know the column and row numbers

print(
    'Windows 7 is a(n) {}'.format(
        vulnerabilities2017['Windows 7']['type']
    )
)
print(
    'Mac OS X had {} vulnerabilities in 2017'.format(
        vulnerabilities2017['Mac OS X']['number']
    )
)

space()

maxproduct = None
maxnumber = -1

for product, values in vulnerabilities2017.items():
    if values['number'] > maxnumber:
        maxproduct = product
        maxnumber = values['number']

print(
    '{} had the most vulnerabilities in 2017 with a total of {}.'.format(
        maxproduct, maxnumber
    )
)
