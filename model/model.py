import networkx as nx
from database.DAO import DAO
from geopy.distance import distance
class Model:
    def __init__(self):
        self._grafo = nx.Graph()

    def getAllProvider(self):
        provider = DAO.getAllProvider()
        return provider

    def buildGraph(self, provider, soglia):
        locations = DAO.getLocationsProvider(provider)
        self._grafo.add_nodes_from(locations)
        allEdge = DAO.getEdges(provider)


        for u in locations:
            for v in locations:
                if u != v:
                    dist = distance((u.Latitude, u.Longitude), (v.Latitude, v.Longitude)).km
                    if dist < soglia:
                        self._grafo.add_edge(u, v, weight=dist)

    def getNumeri(self):
        return self._grafo.number_of_edges(), self._grafo.number_of_nodes()

    def getVicini(self):
        viciniTuple = []
        for v in self._grafo.nodes:
            count = list(nx.neighbors(self._grafo, v))
            viciniTuple.append((v, len(count)))

        viciniTuple.sort(key=lambda x: x[1], reverse=True)
        return viciniTuple



