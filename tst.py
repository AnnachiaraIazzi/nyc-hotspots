from database.DAO import DAO

print(DAO.getAllProvider())

print(DAO.getLocationsProvider("ALTICEUSA"))

for e in allEdge:
    l1 = e[0]
    l2 = e[1]
    distanza = distance((l1.Latitude, l2.Longitude), (l1.Latitude, l2.Longitude)).km
    if distanza < soglia:
        self._grafo.add_edge(l1, l2, weight=distanza)