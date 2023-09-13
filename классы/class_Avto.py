class Avto:
    marka = ''
    skorost = None
    gruzopod = None
    skolko_koles = None
    color = ''

giguli = Avto()
giguli.marka = 'giguli'
giguli.skorost = 120
giguli.gruzopod = 5
giguli.skolko_koles = 4
giguli.color = 'red'

kamaz = Avto()
kamaz.marka = 'kamaz'
kamaz.skorost = 90
kamaz.gruzopod = 50
kamaz.skolko_koles = 6
kamaz.color = 'orange'

print(giguli.__dict__)
print(kamaz.__dict__)
