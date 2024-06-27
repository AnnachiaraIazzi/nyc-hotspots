from database.DB_connect import DBConnect
from model.location import Location

class DAO():
    @staticmethod
    def getAllProvider():
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor()
        cursor.execute("""select distinctrow Provider 
                        from nyc_wifi_hotspot_locations """)
        for row in cursor:
            result.append(*row)
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getLocationsProvider(provider):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary = True)
        cursor.execute("""select distinctrow Location, Longitude, Latitude 
                        from nyc_wifi_hotspot_locations 
                        where Provider = %s """, (provider,))
        for row in cursor:
            result.append(Location(**row))
        cursor.close()
        conn.close()
        return result

    @staticmethod
    def getEdges(provider):
        conn = DBConnect.get_connection()
        result = []
        cursor = conn.cursor(dictionary=True)
        cursor.execute("""select n1.Location as l1, n2.Location as l2, avg( n1.Latitude) as lt1, avg(n2.Latitude) as lt2, avg(n1.Longitude) as lg1, avg(n2.Longitude) as lg2
                        from nyc_wifi_hotspot_locations n1, nyc_wifi_hotspot_locations n2
                        where n1.Provider= n2.Provider and n1.Provider = %s and n1.Location<n2.Location 
                        group by n1.Location, n2.Location """, (provider, ))
        for row in cursor:
            loc1 = Location(row["l1"], row["lg1"], row["lt1"])
            loc2 = Location(row["l2"], row["lg2"], row["lt2"])
            result.append(((loc1, loc2)))
        cursor.close()
        conn.close()
        return result