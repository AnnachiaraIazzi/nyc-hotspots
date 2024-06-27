from dataclasses import dataclass
@dataclass
class Location:
    Location: str
    Longitude: float
    Latitude: float

    def __str__(self):
        return f"{self.Location} - ({self.Latitude} - {self.Longitude})"

    def __hash__(self):
        return hash(self.Location)