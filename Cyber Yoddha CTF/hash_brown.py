import hashlib 
import pandas as pd

hash_ = "F3899973D90D9EBB3A03ABC143B293CD33CFD688CB949AE1FBA61ACAB0D3D6220948AB3C35E00AF9D9497484B666D7FEA9D7673E2FC6AE463936C7B797FB3AF0".lower()

cities = pd.read_csv('fr.csv')
cities = cities['city'].to_list()
# with open('uniq_cities.txt', 'rb') as h:

#     cities = h.readlines()

cities = map(lambda x : x.encode().lower().strip(), cities)

i=0
c=0
for city in cities:
    print(f'city = {c}')
    for number in range(0, pow(10, 7)):
        password = city + str(number).encode()
        h = hashlib.sha512(password).hexdigest()
        if not i%1000000:
            print(f'doing index {i}')
        if h == hash_:
            print('FOUND!!!')
            print(password)
        # break
        i+=1
    c += 1