from typing import List, Optional
from .._generated.models import *

class LatLon(object):

    def __init__(
        self,
        lat: float=None,
        lon: float=None
    ):
        self._lat = lat
        self._lon = lon

    @property
    def lat(self) -> float:
        return self._lat

    @lat.setter
    def lat(self, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError(f'lat.setter(): got {type(value).__name__} but expected type is float')
        else:
            self._lat = value

    @property
    def lon(self) -> float:
        return self._lon

    @lon.setter
    def lon(self, value: float) -> None:
        if not isinstance(value, float):
            raise TypeError(f'lon.setter(): got {type(value).__name__} but expected type is float')
        else:
            self._lon = value

class BoundingBox(object):

    def __init__(
        self,
        top_left: LatLon=None,
        bottom_right: LatLon=None,
        top_right: LatLon=None,
        bottom_left: LatLon=None
    ):
        self.top_left = top_left
        self.bottom_right = bottom_right
        self.top = top_left.lat
        self.bottom = bottom_right.lat
        self.left = top_left.lon
        self.right = bottom_right.lon
        self.top_right = top_right if top_right else LatLon(top_left.lat, bottom_right.lon)
        self.bottom_left = bottom_left if bottom_left else LatLon(bottom_right.lat, top_left.lon)

class StructuredAddress(object):

    def __init__(
        self,
        country_code: str,
        cross_street: Optional[str] = None,
        street_number: Optional[str] = None,
        street_name: Optional[str] = None,
        municipality: Optional[str] = None,
        municipality_subdivision: Optional[str] = None,
        country_tertiary_subdivision: Optional[str] = None,
        country_secondary_subdivision: Optional[str] = None,
        country_subdivision: Optional[str] = None,
        postal_code: Optional[str] = None
    ):
        self._country_code = country_code
        self.cross_street = cross_street
        self.street_number = street_number
        self.street_name = street_name
        self.municipality = municipality
        self.municipality_subdivision = municipality_subdivision
        self.country_tertiary_subdivision = country_tertiary_subdivision
        self.country_secondary_subdivision = country_secondary_subdivision
        self.country_subdivision = country_subdivision
        self.postal_code = postal_code

    @property
    def country_code(self) -> str:
        return self._country_code

    @country_code.setter
    def country_code(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f'country_code.setter(): got {type(value).__name__} but expected type is string')
        else:
            self._country_code = value

    @property
    def cross_street(self) -> str:
        return self._cross_street

    @cross_street.setter
    def cross_street(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f'cross_street.setter(): got {type(value).__name__} but expected type is string')
        else:
            self._cross_street = value

    @property
    def street_number(self) -> str:
        return self._street_number

    @street_number.setter
    def street_number(self, value) -> None:
        if not isinstance(value, str):
            raise TypeError(f'street_number.setter(): got {type(value).__name__} but expected type is string')
        else:
            self._street_number = value

    @property
    def street_name(self) -> str:
        return self._street_name

    @street_name.setter
    def street_name(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f'street_name.setter(): got {type(value).__name__} but expected type is string')
        else:
            self._street_name = value

    @property
    def municipality(self) -> str:
        return self._municipality

    @municipality.setter
    def municipality(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f'municipality.setter(): got {type(value).__name__} but expected type is string')
        else:
            self._municipality = value

    @property
    def municipality_subdivision(self) -> str:
        return self._municipality_subdivision

    @municipality_subdivision.setter
    def municipality_subdivision(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f'municipality_subdivision.setter(): got {type(value).__name__} but expected type is string')
        else:
            self._municipality_subdivision = value

    @property
    def country_tertiary_subdivision(self) -> str:
        return self._country_tertiary_subdivision

    @country_tertiary_subdivision.setter
    def country_tertiary_subdivision(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f'country_tertiary_subdivision.setter(): got {type(value).__name__} but expected type is string')
        else:
            self._country_tertiary_subdivision = value

    @property
    def country_secondary_subdivision(self) -> str:
        return self._country_secondary_subdivision

    @country_secondary_subdivision.setter
    def country_secondary_subdivision(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f'country_secondary_subdivision.setter(): got {type(value).__name__} but expected type is string')
        else:
            self._country_secondary_subdivision = value

    @property
    def country_subdivision(self) -> str:
        return self._country_subdivision

    @country_subdivision.setter
    def country_subdivision(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f'country_subdivision.setter(): got {type(value).__name__} but expected type is string')
        else:
            self._country_subdivision = value

    @property
    def postal_code(self) -> str:
        return self._postal_code

    @postal_code.setter
    def postal_code(self, value: str) -> None:
        if not isinstance(value, str):
            raise TypeError(f'postal_code.setter(): got {type(value).__name__} but expected type is string')
        else:
            self._postal_code = value


class SearchSummary(object):

    def __init__(
        self,
        query: str = None,
        query_type: str = None,
        query_time: int = None,
        num_results: int = None,
        top: int = None,
        skip: int = None,
        total_results: int = None,
        fuzzy_level: int = None,
        geo_bias: LatLon = None
    ):
        self.query = query
        self.query_type = query_type
        self.query_time = query_time
        self.num_results = num_results
        self.top = top
        self.skip = skip
        self.total_results = total_results
        self.fuzzy_level = fuzzy_level
        self.geo_bias = geo_bias

