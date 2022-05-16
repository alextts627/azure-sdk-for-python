# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING
from azure.core.tracing.decorator import distributed_trace
from azure.core.exceptions import HttpResponseError
from ._generated._weather_client import WeatherClient as WeatherClientGen
from ._generated.models import *
from .models import *

if TYPE_CHECKING:
    from typing import Any, List, Optional, Object
    from azure.core.credentials import TokenCredential
    from azure.core.polling import LROPoller

class WeatherClient(object):
    """Azure Maps Weather REST APIs.
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    """
    def __init__(
        self,
        credential, # type: TokenCredential
        **kwargs # type: Any
    ):
        # type: (...) -> None

        if not credential:
            raise ValueError(
                "You need to provide account shared key to authenticate.")

        self._weather_client = WeatherClientGen(
            credential,
            **kwargs
        ).weather


    @distributed_trace
    def get_hourly_forecast(
        self,
        query,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.HourlyForecastResponse"
        """**Get Hourly Forecast**

        **Applies to**\ : S0 and S1 pricing tiers.

        Request detailed weather forecast by the hour for the next 1, 12, 24 (1 day), 72 (3 days), 120
        (5 days), and 240 hours (10 days) for the given the given coordinate location.  The API returns
        details such as temperature, humidity, wind, precipitation, and ultraviolet (UV) index.

        In S0 you can request hourly forecast for the next 1, 12, 24 hours (1 day), and 72 hours (3
        days). In S1 you can also request hourly forecast for the next 120 (5 days) and 240 hours (10
        days).

        :param format: Desired format of the response. Only ``json`` format is supported.
        :type format: str or ~azure.maps.weather.models.ResponseFormat
        :param query: Coordinates of the location for which hourly forecast information is requested.
         The applicable query is specified as a comma separated string composed by latitude followed by
         longitude e.g. "47.641268,-122.125679".
        :type query: str
        :param unit: Specifies to return the data in either metric units or imperial units. Default
         value is metric.
        :type unit: str or ~azure.maps.weather.models.WeatherDataUnit
        :param duration: Time frame of the returned weather forecast. By default, the forecast data for
         next hour will be returned. Available values are


         * ``1`` - Return forecast data for the next hour. Default value.
         * ``12`` - Return hourly forecast for next 12 hours.
         * ``24`` - Return hourly forecast for next 24 hours.
         * ``72`` - Return hourly forecast for next 72 hours (3 days).
         * ``120`` - Return hourly forecast for next 120 hours (5 days). Only available in S1 SKU.
         * ``240`` - Return hourly forecast for next 240 hours (10 days). Only available in S1 SKU.
        :type duration: int
        :param language: Language in which search results should be returned. Should be one of
         supported IETF language tags, case insensitive. When data in specified language is not
         available for a specific field, default language is used.  Default value is en-us.

         Please refer to `Supported languages
         <https://docs.microsoft.com/azure/azure-maps/supported-languages>`_ for details.
        :type language: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: HourlyForecastResponse, or the result of cls(response)
        :rtype: ~azure.maps.weather.models.HourlyForecastResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        return self._weather_client.get_hourly_forecast(
            query,
            **kwargs
        )
            
   
    @distributed_trace
    def get_minute_forecast(
        self,
        query,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.MinuteForecastResponse"
        """**Get Minute Forecast**

        **Applies to**\ : S1 pricing tier.

        Get Minute Forecast service returns minute-by-minute forecasts for a given location for the
        next 120 minutes.  Users can request weather forecasts in the interval of 1, 5 and 15 minutes.
        The response will include details such as the type of precipitation (including rain, snow, or a
        mixture of both), start time, and precipitation intensity value (dBZ).

        :param format: Desired format of the response. Only ``json`` format is supported.
        :type format: str or ~azure.maps.weather.models.ResponseFormat
        :param query: Coordinates of the location for which minute forecast information is requested.
         The applicable query is specified as a comma separated string composed by latitude followed by
         longitude e.g. "47.641268,-122.125679".
        :type query: str
        :param interval: Specifies time interval in minutes for the returned weather forecast.
         Supported values are


         * ``1`` -  Retrieve forecast for 1-minute intervals. Returned by default.
         * ``5`` - Retrieve forecasts for 5-minute intervals.
         * ``15`` - Retrieve forecasts for 15-minute intervals.
        :type interval: int
        :param language: Language in which search results should be returned. Should be one of
         supported IETF language tags, case insensitive. When data in specified language is not
         available for a specific field, default language is used.  Default value is en-us.

         Please refer to `Supported languages
         <https://docs.microsoft.com/azure/azure-maps/supported-languages>`_ for details.
        :type language: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: MinuteForecastResponse, or the result of cls(response)
        :rtype: ~azure.maps.weather.models.MinuteForecastResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        return self._weather_client.get_hourly_forecast(
            query,
            **kwargs
        )
        
        
        
    @distributed_trace
    def get_quarter_day_forecast(
        self,
        query,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.QuarterDayForecastResponse"
        """**Get Quarter-Day Forecast**

        **Applies to**\ : S0 and S1 pricing tiers.

        Service returns detailed weather forecast by quarter-day for the next 1, 5, 10, or 15 days for
        a given location. Response data is presented by quarters of the day - morning, afternoon,
        evening, and overnight. Details such as temperature, humidity, wind, precipitation, and UV
        index are returned.

        :param format: Desired format of the response. Only ``json`` format is supported.
        :type format: str or ~azure.maps.weather.models.ResponseFormat
        :param query: Coordinates of the location for which quarter-day forecast information is
         requested. The applicable query is specified as a comma separated string composed by latitude
         followed by longitude e.g. "47.641268,-122.125679".
        :type query: str
        :param unit: Specifies to return the data in either metric units or imperial units. Default
         value is metric.
        :type unit: str or ~azure.maps.weather.models.WeatherDataUnit
        :param duration: Specifies for how many days the quester-day forecast responses are returned.
         Supported values are:


         * ``1`` - Return forecast data for the next day. Returned by default.
         * ``5`` - Return forecast data for the next 5 days.
         * ``10`` - Return forecast data for next 10 days.
         * ``15`` - Return forecast data for the next 15 days.
        :type duration: int
        :param language: Language in which search results should be returned. Should be one of
         supported IETF language tags, case insensitive. When data in specified language is not
         available for a specific field, default language is used.  Default value is en-us.

         Please refer to `Supported languages
         <https://docs.microsoft.com/azure/azure-maps/supported-languages>`_ for details.
        :type language: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: QuarterDayForecastResponse, or the result of cls(response)
        :rtype: ~azure.maps.weather.models.QuarterDayForecastResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        return self._weather_client.get_quarter_day_forecast(
            query,
            **kwargs
        )
        
        
    @distributed_trace   
    def get_current_conditions(
        self,
        query,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.CurrentConditionsResponse"
        """**Get Current Conditions**

        **Applies to**\ : S0 and S1 pricing tiers.

        Get Current Conditions service returns detailed current weather conditions such as
        precipitation, temperature and wind for a given coordinate location. Also, observations from
        the past 6 or 24 hours for a particular location can be retrieved. The basic information
        returned with the response include details such as observation date and time, brief description
        of the weather conditions, weather icon, precipitation indicator flags, and temperature.
        Additional details such as RealFeel™ Temperature and UV index are also returned.

        :param format: Desired format of the response. Only ``json`` format is supported.
        :type format: str or ~azure.maps.weather.models.ResponseFormat
        :param query: Coordinates of the location for which current conditions information is
         requested. The applicable query is specified as a comma separated string composed by latitude
         followed by longitude e.g. "47.641268,-122.125679".
        :type query: str
        :param unit: Specifies to return the data in either metric units or imperial units. Default
         value is metric.
        :type unit: str or ~azure.maps.weather.models.WeatherDataUnit
        :param details: Return full details for the current conditions. Available values are


         * ``true`` - Returns full details. By default all details are returned.
         * ``false`` - Returns a truncated version of the current condition data, which includes
         observation date time, weather phrase, icon code, precipitation indicator flag, and
         temperature.
        :type details: str
        :param duration: Time frame of the returned weather conditions. By default, the most current
         weather conditions will be returned. Default value is 0. Supported values are:


         * ``0`` - Return the most current weather conditions.
         * ``6`` - Return weather conditions from past 6 hours.
         * ``24`` - Return weather conditions from past 24 hours.
        :type duration: int
        :param language: Language in which search results should be returned. Should be one of
         supported IETF language tags, case insensitive. When data in specified language is not
         available for a specific field, default language is used.  Default value is en-us.

         Please refer to `Supported languages
         <https://docs.microsoft.com/azure/azure-maps/supported-languages>`_ for details.
        :type language: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: CurrentConditionsResponse, or the result of cls(response)
        :rtype: ~azure.maps.weather.models.CurrentConditionsResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        return self._weather_client.get_current_conditions(
            query,
            **kwargs
        )
        
    
    @distributed_trace   
    def get_daily_forecast(
        self,
        query,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DailyForecastResponse"
        """**Get Daily Forecast**

        **Applies to**\ : S0 and S1 pricing tiers.

        The service returns detailed weather forecast such as temperature and wind by day for the next
        1, 5, 10, 15, 25, or 45 days for a given coordinate location.  The response include details
        such as temperature, wind, precipitation, air quality, and UV index.

        In S0 you can request daily forecast for the next 1, 5, 10, and 15 days. In S1 you can also
        request daily forecast for the next 25 days, and 45 days.

        :param format: Desired format of the response. Only ``json`` format is supported.
        :type format: str or ~azure.maps.weather.models.ResponseFormat
        :param query: Coordinates of the location for which current conditions information is
         requested. The applicable query is specified as a comma separated string composed by latitude
         followed by longitude e.g. "47.641268,-122.125679".
        :type query: str
        :param unit: Specifies to return the data in either metric units or imperial units. Default
         value is metric.
        :type unit: str or ~azure.maps.weather.models.WeatherDataUnit
        :param duration: Specifies for how many days the daily forecast responses are returned.
         Available values are


         * ``1`` - Return forecast data for the next day. Returned by default.
         * ``5`` - Return forecast data for the next 5 days.
         * ``10`` - Return forecast data for the next 10 days.
         * ``25`` - Return forecast data for the next 25 days. Only available in S1 SKU.
         * ``45`` - Return forecast data for the next 45 days. Only available in S1 SKU.
        :type duration: int
        :param language: Language in which search results should be returned. Should be one of
         supported IETF language tags, case insensitive. When data in specified language is not
         available for a specific field, default language is used.  Default value is en-us.

         Please refer to `Supported languages
         <https://docs.microsoft.com/azure/azure-maps/supported-languages>`_ for details.
        :type language: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DailyForecastResponse, or the result of cls(response)
        :rtype: ~azure.maps.weather.models.DailyForecastResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        return self._weather_client.get_daily_forecast(
            query,
            **kwargs
        )
        
        
    @distributed_trace    
    def get_weather_along_route(
        self,
        query,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.WeatherAlongRouteResponse"
        """**Get Weather along route**

         **Applies to**\ : S1 pricing tier.

         Weather along a route API returns hyper local (one kilometer or less), up-to-the-minute
        weather nowcasts, weather hazard assessments, and notifications along a route described as a
        sequence of waypoints.
         This includes a list of weather hazards affecting the waypoint or route, and the aggregated
        hazard index for each waypoint might be used to paint each portion of a route according to how
        safe it is for the driver. When submitting the waypoints, it is recommended to stay within, or
        close to, the distance that can be traveled within 120-mins or shortly after. Data is updated
        every five minutes.

         The service supplements Azure Maps `Route Service
        <https://docs.microsoft.com/rest/api/maps/route>`_ that allows you to first request a route
        between an origin and a destination and use that as an input for Weather Along Route endpoint.

         In addition, the service supports scenarios to generate weather notifications for waypoints
        that experience an increase in intensity of a weather hazard. For example, if the vehicle is
        expected to begin experiencing heavy rain as it reaches a waypoint, a weather notification for
        heavy rain will be generated for that waypoint allowing the end product to display a heavy rain
        notification before the driver reaches that waypoint.
         The trigger for when to display the notification for a waypoint could be based, for example,
        on a `geofence <https://docs.microsoft.com/azure/azure-maps/tutorial-iot-hub-maps>`_\ , or
        selectable distance to the waypoint.

         The API covers all regions of the planet except latitudes above Greenland and Antarctica.

        :param format: Desired format of the response. Only ``json`` format is supported.
        :type format: str or ~azure.maps.weather.models.ResponseFormat
        :param query: Coordinates through which the route is calculated, separated by colon (:) and
         entered in chronological order. A minimum of two waypoints is required. A single API call may
         contain up to 60 waypoints.
         A waypoint indicates location, ETA, and optional heading: latitude,longitude,ETA,heading,
         where


         * ``Latitude`` - Latitude coordinate in decimal degrees.
         * ``Longitude`` - Longitude coordinate in decimal degrees.
         * ``ETA (estimated time of arrival)`` - The number of minutes from the present time that it
         will take for the vehicle to reach the waypoint. Allowed range is from 0.0 to 120.0 minutes.
         * ``Heading`` - An optional value indicating the vehicle heading as it passes the waypoint.
         Expressed in clockwise degrees relative to true north. This is issued to calculate sun glare as
         a driving hazard. Allowed range is from 0.0 to 360.0 degrees. If not provided, a heading will
         automatically be derived based on the position of neighboring waypoints.

         It is recommended to stay within, or close to, the distance that can be traveled within
         120-mins or shortly after. This way a more accurate assessment can be provided for the trip and
         prevent isolated events not being captured between waypoints.  Information can and should be
         updated along the route (especially for trips greater than 2 hours) to continuously pull new
         waypoints moving forward, but also to ensure that forecast information for content such as
         precipitation type and intensity is accurate as storms develop and dissipate over time.
        :type query: str
        :param language: Language in which search results should be returned. Should be one of
         supported IETF language tags, case insensitive. When data in specified language is not
         available for a specific field, default language is used.  Default value is en-us.

         Please refer to `Supported languages
         <https://docs.microsoft.com/azure/azure-maps/supported-languages>`_ for details.
        :type language: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: WeatherAlongRouteResponse, or the result of cls(response)
        :rtype: ~azure.maps.weather.models.WeatherAlongRouteResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        return self._weather_client.get_weather_along_route(
            query,
            **kwargs
        )
        
    
    @distributed_trace   
    def get_severe_weather_alerts(
        self,
        query,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.SevereWeatherAlertsResponse"
        """**Get Severe Weather Alerts**

        **Applies to**\ : S0 and S1 pricing tiers.

        Severe weather phenomenon can significantly impact our everyday life and business operations.
        For example, severe weather conditions such as tropical storms, high winds or flooding can
        close roads and force logistics companies to reroute their fleet causing delays in reaching
        destinations and breaking the cold chain of refrigerated food products.  Azure Maps
        Severe Weather Alerts API returns the severe weather alerts that are available worldwide
        from both official Government Meteorological Agencies and leading global to
        regional weather alert providers. The service can return details such as alert type, category,
        level and detailed description about the active severe alerts for the requested location, like
        hurricanes, thunderstorms, lightning, heat waves or forest fires.

        :param format: Desired format of the response. Only ``json`` format is supported.
        :type format: str or ~azure.maps.weather.models.ResponseFormat
        :param query: Coordinates of the location for which severe weather alerts are requested. The
         applicable query is specified as a comma separated string composed by latitude followed by
         longitude e.g. "47.641268,-122.125679".
        :type query: str
        :param language: Language in which search results should be returned. Should be one of
         supported IETF language tags, case insensitive. When data in specified language is not
         available for a specific field, default language is used.  Default value is en-us.

         Please refer to `Supported languages
         <https://docs.microsoft.com/azure/azure-maps/supported-languages>`_ for details.
        :type language: str
        :param details: Return full details for the severe weather alerts. Available values are


         * ``true`` - Returns full details. By default all details are returned.
         * ``false`` - Returns a truncated version of the alerts data, which excludes the area-specific
         full description of alert details (\ ``alertDetails``\ ).
        :type details: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: SevereWeatherAlertsResponse, or the result of cls(response)
        :rtype: ~azure.maps.weather.models.SevereWeatherAlertsResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        return self._weather_client.get_severe_weather_alerts(
            query,
            **kwargs
        )
        
    
    @distributed_trace
    def get_daily_indices(
        self,
        query,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.DailyIndicesResponse"
        """**Get Daily Indices**

        **Applies to**\ : S0 and S1 pricing tiers.

        There may be times when you want to know if the weather conditions are optimal for a specific
        activity, for example, for outdoor construction, indoor activities, running or farming
        including soil moisture information.  Azure Maps Indices API returns index values that will
        guide end users to plan future activities. For example, a health mobile application can notify
        users that today is good weather for running or for other outdoors activities like for playing
        golf, and retail stores can optimize their digital marketing campaigns based on predicted index
        values. The service returns in daily indices values for current and next 5, 10 and 15 days
        starting from current day.

        :param format: Desired format of the response. Only ``json`` format is supported.
        :type format: str or ~azure.maps.weather.models.ResponseFormat
        :param query: Coordinates of the location for which daily indices are requested. The applicable
         query is specified as a comma separated string composed by latitude followed by longitude e.g.
         "47.641268,-122.125679".
        :type query: str
        :param language: Language in which search results should be returned. Should be one of
         supported IETF language tags, case insensitive. When data in specified language is not
         available for a specific field, default language is used.  Default value is en-us.

         Please refer to `Supported languages
         <https://docs.microsoft.com/azure/azure-maps/supported-languages>`_ for details.
        :type language: str
        :param duration: Specifies for how many days the daily indices are returned. By default, the
         indices data for the current day will be returned. When requesting future indices data, the
         current day is included in the response as day 1. Available values are


         * ``1`` - Return daily index data for the current day. Default value.
         * ``5`` - Return 5 days of daily index data starting from the current day.
         * ``10`` - Return 10 days of daily index data starting from the current day.
         * ``15`` - Return 15 days of daily index data starting from the current day.
        :type duration: int
        :param index_id: Numeric index identifier that can be used for restricting returned results to
         the corresponding index type. Cannot be paired with ``indexGroupId``. Please refer to `Weather
         Service Concepts <https://aka.ms/AzureMapsWeatherConcepts>`_ for details and to see the
         supported indices.
        :type index_id: int
        :param index_group_id: Numeric index group identifier that can be used for restricting returned
         results to the corresponding subset of indices (index group). Cannot be paired with
         ``indexId``. Please refer to `Weather Service Concepts
         <https://aka.ms/AzureMapsWeatherConcepts>`_ for details and to see the supported index groups.
        :type index_group_id: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: DailyIndicesResponse, or the result of cls(response)
        :rtype: ~azure.maps.weather.models.DailyIndicesResponse
        :raises: ~azure.core.exceptions.HttpResponseError
        """
        return self._weather_client.get_daily_indices(
            query,
            **kwargs
        )