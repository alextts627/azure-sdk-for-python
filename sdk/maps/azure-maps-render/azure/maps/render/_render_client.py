# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING
from azure.core.tracing.decorator import distributed_trace
from azure.core.exceptions import HttpResponseError
from ._generated._render_client import RenderClient as RenderClientGen
from ._generated.models import *
from .models import *
# from .utils import get_authentication_policy, get_headers_policy

if TYPE_CHECKING:
    from typing import Any, List, Optional, Object
    from azure.core.credentials import TokenCredential
    from azure.core.polling import LROPoller

class RenderClient(object):
    """Azure Maps Render REST APIs.
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

        self._render_client = RenderClientGen(
            credential,
            **kwargs
        ).render
                
    @distributed_trace
    def get_map_tile(
        self,
        query,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """**Applies to**\ : S0 and S1 pricing tiers.

        Fetches map tiles in vector or raster format typically to be integrated into a new map control
        or SDK. By default, Azure uses vector map tiles for its web map control (see `Zoom Levels and
        Tile Grid
        <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_\ )

        **Note**\ : Weather tiles are only available via `Get Map Tile V2 API
        <https://aka.ms/AzureMapsWeatherTiles>`_. We recommend to start to use the new `Get Map Tile V2
        API <https://aka.ms/GetMapTileV2>`_.

        :param format: Desired format of the response. Possible values are png & pbf.
        :type format: str or ~azure.maps.render.models.TileFormat
        :param layer: Map layer requested. Possible values are basic, hybrid, labels and terra.
        :type layer: str or ~azure.maps.render.models.MapTileLayer
        :param style: Map style to be returned. Possible values are main, dark, and shaded_relief.
        :type style: str or ~azure.maps.render.models.MapTileStyle
        :param zoom: Zoom level for the desired tile. For *raster* tiles, value must be in the range:
         0-18 (inclusive). Terra raster tiles, values must be in the range 0-6 (inclusive). For *vector*
         tiles, value must be in the range: 0-22 (inclusive).
         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type zoom: int
        :param x_tile_index: X coordinate of the tile on zoom grid. Value must be in the range [0,
         2:code:`<sup>`zoom`</sup>` -1].

         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type x_tile_index: int
        :param y_tile_index: Y coordinate of the tile on zoom grid. Value must be in the range [0,
         2:code:`<sup>`zoom`</sup>` -1].

         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type y_tile_index: int
        :param tile_size: The size of the returned map tile in pixels.
        :type tile_size: str or ~azure.maps.render.models.MapTileSize
        :param language: Language in which search results should be returned. Should be one of
         supported IETF language tags, case insensitive. When data in specified language is not
         available for a specific field, default language is used.

         Please refer to `Supported Languages
         <https://docs.microsoft.com/en-us/azure/azure-maps/supported-languages>`_ for details.
        :type language: str
        :param view: The View parameter specifies which set of geopolitically disputed content is
         returned via Azure Maps services, including  borders and labels displayed on the map. The View
         parameter (also referred to as “user region parameter”) will show the  correct maps for that
         country/region. By default, the View parameter is set to “Unified” even if you haven’t defined
         it in  the request. It is your responsibility to determine the location of your users, and then
         set the View parameter correctly  for that location. Alternatively, you have the option to set
         ‘View=Auto’, which will return the map data based on the IP  address of the request. The View
         parameter in Azure Maps must be used in compliance with applicable laws, including those
         regarding mapping, of the country where maps, images and other data and third party content
         that you are authorized to  access via Azure Maps is made available. Example: view=IN.

         Please refer to `Supported Views <https://aka.ms/AzureMapsLocalizationViews>`_ for details and
         to see the available Views.
        :type view: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
            
        return self._render_client.get_map_tile(
            query,
            **kwargs
        )
        
    @distributed_trace
    def get_map_state_tile(
        self,
        query,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """**Applies to**\ : S0 and S1 pricing tiers.

        Fetches state tiles in vector format typically to be integrated into indoor maps module of map
        control or SDK. The map control will call this API after user turns on dynamic styling (see
        `Zoom Levels and Tile Grid
        <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_\
        ).

        :param zoom: Zoom level for the desired tile. Zoom value must be in the range: 0-20
         (inclusive).

         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type zoom: int
        :param x_tile_index: X coordinate of the tile on zoom grid. Value must be in the range [0,
         2:code:`<sup>`zoom`</sup>` -1].

         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type x_tile_index: int
        :param y_tile_index: Y coordinate of the tile on zoom grid. Value must be in the range [0,
         2:code:`<sup>`zoom`</sup>` -1].

         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type y_tile_index: int
        :param stateset_id: The stateset id.
        :type stateset_id: str
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
            
        return self._render_client.get_map_state_tile_preview(
            query,
            **kwargs
        )
    
    @distributed_trace
    def get_copyright_caption(
        self,
        query,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.GetCopyrightCaptionResult"
        """**Applies to**\ : S0 and S1 pricing tiers.

        Copyrights API is designed to serve copyright information for Render Tile
        service. In addition to basic copyright for the whole map, API is serving
        specific groups of copyrights for some countries.

        As an alternative to copyrights for map request, one can receive captions
        for displaying the map provider information on the map.

        :param format: Desired format of the response. Value can be either *json* or *xml*.
        :type format: str or ~azure.maps.render.models.TextFormat
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GetCopyrightCaptionResult, or the result of cls(response)
        :rtype: ~azure.maps.render.models.GetCopyrightCaptionResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
            
        return self._render_client.get_copyright_caption(
            query,
            **kwargs
        )
        
    @distributed_trace
    def get_map_static_image(
        self,
        query,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        """**Applies to:** S1 pricing tier.

        This service returns a map image tile with size 256x256, given the x and y coordinates and zoom
        level. Zoom level ranges from 1 to 19. The current available style value is 'satellite' which
        provides satellite
        imagery alone.

        **Note**\ : We recommend to start to use the new `Get Map Tile V2 API
        <https://aka.ms/GetMapTileV2>`_.

        :param format: Desired format of the response. Possible value: png.
        :type format: str or ~azure.maps.render.models.RasterTileFormat
        :param style: Map style to be returned. **Possible values:** satellite.
        :type style: str or ~azure.maps.render.models.MapImageryStyle
        :param zoom: Zoom level for the desired tile. Zoom value must be in the range: 1-19
         (inclusive).
         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type zoom: int
        :param x_tile_index: X coordinate of the tile on zoom grid. Value must be in the range [0,
         2:code:`<sup>`zoom`</sup>` -1].

         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type x_tile_index: int
        :param y_tile_index: Y coordinate of the tile on zoom grid. Value must be in the range [0,
         2:code:`<sup>`zoom`</sup>` -1].

         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type y_tile_index: int
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: IO, or the result of cls(response)
        :rtype: IO
        :raises: ~azure.core.exceptions.HttpResponseError
        """
            
        return self._render_client.get_map_static_image(
            query,
            **kwargs
        )
        
    @distributed_trace
    def get_copyright_from_bounding_box(
        self,
        query,  # type: str
        boundingBox, #type: BoundingBox
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.GetCopyrightFromBoundingBoxResult"
        """**Applies to**\ : S0 and S1 pricing tiers.

        Returns copyright information for a given bounding box. Bounding-box requests should specify
        the minimum and maximum longitude and latitude (EPSG-3857) coordinates.

        :param format: Desired format of the response. Value can be either *json* or *xml*.
        :type format: str or ~azure.maps.render.models.TextFormat
        :param mincoordinates: Minimum coordinates of bounding box in latitude longitude coordinate
         system. E.g. 52.41064,4.84228.
        :type mincoordinates: str
        :param maxcoordinates: Maximum coordinates of bounding box in latitude longitude coordinate
         system. E.g. 52.41064,4.84228.
        :type maxcoordinates: str
        :param text: Yes/no value to exclude textual data from response. Only images and country names
         will be in response.
        :type text: str or ~azure.maps.render.models.IncludeText
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GetCopyrightFromBoundingBoxResult, or the result of cls(response)
        :rtype: ~azure.maps.render.models.GetCopyrightFromBoundingBoxResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
            
        return self._render_client.get_copyright_from_bounding_box(
            query,
            **kwargs
        )
    
    @distributed_trace
    def get_copyright_for_tile(
        self,
        query,  # type: str
        tileIndex, # TileIndex
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.GetCopyrightForTileResult"
        """**Applies to**\ : S0 and S1 pricing tiers.

        Copyrights API is designed to serve copyright information for Render Tile  service. In addition
        to basic copyright for the whole map, API is serving  specific groups of copyrights for some
        countries.
        Returns the copyright information for a given tile. To obtain the copyright information for a
        particular tile, the request should specify the tile's zoom level and x and y coordinates (see:
        Zoom Levels and Tile Grid).

        :param format: Desired format of the response. Value can be either *json* or *xml*.
        :type format: str or ~azure.maps.render.models.TextFormat
        :param zoom: Zoom level for the desired tile. Zoom value must be in the range: 0-18
         (inclusive).

         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type zoom: int
        :param x_tile_index: X coordinate of the tile on zoom grid. Value must be in the range [0,
         2:code:`<sup>`zoom`</sup>` -1].

         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type x_tile_index: int
        :param y_tile_index: Y coordinate of the tile on zoom grid. Value must be in the range [0,
         2:code:`<sup>`zoom`</sup>` -1].

         Please see `Zoom Levels and Tile Grid
         <https://docs.microsoft.com/en-us/azure/location-based-services/zoom-levels-and-tile-grid>`_
         for details.
        :type y_tile_index: int
        :param text: Yes/no value to exclude textual data from response. Only images and country names
         will be in response.
        :type text: str or ~azure.maps.render.models.IncludeText
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GetCopyrightForTileResult, or the result of cls(response)
        :rtype: ~azure.maps.render.models.GetCopyrightForTileResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
            
        return self._render_client.get_copyright_for_tile(
            query,
            **kwargs
        )
        
    @distributed_trace
    def get_copyright_for_world(
        self,
        query,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.GetCopyrightForWorldResult"
        """**Applies to**\ : S0 and S1 pricing tiers.

        Copyrights API is designed to serve copyright information for Render Tile  service. In addition
        to basic copyright for the whole map, API is serving  specific groups of copyrights for some
        countries.
        Returns the copyright information for the world. To obtain the default copyright information
        for the whole world, do not specify a tile or bounding box.

        :param format: Desired format of the response. Value can be either *json* or *xml*.
        :type format: str or ~azure.maps.render.models.TextFormat
        :param text: Yes/no value to exclude textual data from response. Only images and country names
         will be in response.
        :type text: str or ~azure.maps.render.models.IncludeText
        :keyword callable cls: A custom type or function that will be passed the direct response
        :return: GetCopyrightForWorldResult, or the result of cls(response)
        :rtype: ~azure.maps.render.models.GetCopyrightForWorldResult
        :raises: ~azure.core.exceptions.HttpResponseError
        """
            
        return self._render_client.get_copyright_for_world(
            query,
            **kwargs
        )