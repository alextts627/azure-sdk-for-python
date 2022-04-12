# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING
from azure.core.tracing.decorator import distributed_trace
from azure.core.exceptions import HttpResponseError
from ._generated._traffic_client import TrafficClient as TrafficClientGen
from .models import *
# from .utils import get_authentication_policy, get_headers_policy

if TYPE_CHECKING:
    from typing import Any, List, Optional, Object, Union, IO
    from azure.core.credentials import TokenCredential
    from azure.core.polling import LROPoller
    from .models import LatLon
    
class TrafficClient(object):
    """Azure Maps Traffic REST APIs.
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

        self._traffic_client = TrafficClientGen(
            credential,
            **kwargs
        ).traffic


    @distributed_trace
    def get_traffic_flow_tile(
        self,
        style,  # type: Union[str, "_models.TrafficFlowTileStyle"]
        zoom,  # type: int
        x_tile_index,  # type: int
        y_tile_index,  # type: int
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
            
        return self._traffic_client.get_traffic_flow_tile(
            style,
            zoom,
            **kwargs
        )
        
        
    @distributed_trace
    def get_traffic_flow_segment(
        self,
        style,  # type: Union[str, "models.TrafficFlowSegmentStyle"]
        zoom,  # type: int
        query,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "models.TrafficFlowSegmentResult"
            
        return self._traffic_client.get_traffic_flow_segment(
            style,
            zoom,
            query,
            **kwargs
        )

        
    @distributed_trace
    def get_traffic_incident_tile(
        self,
        style,  # type: Union[str, "_models.TrafficIncidentTileStyle"]
        zoom,  # type: int
        x_tile_index,  # type: int
        y_tile_index,  # type: int
        **kwargs  # type: Any
    ):
        # type: (...) -> IO
        
        return self._traffic_client.get_traffic_incident_tile(
            style,
            zoom,
            **kwargs
        )
        
    @distributed_trace
    def get_traffic_incident_detail(
        self,
        style,  # type: Union[str, "_models.TrafficIncidentDetailStyle"]
        boundingbox,  # type: str
        bounding_zoom,  # type: int
        trafficmodelid,  # type: str
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.TrafficIncidentDetailResult"
        return self._traffic_client.get_traffic_incident_tile(
            style,
            boundingbox,
            bounding_zoom,
            trafficmodelid,
            **kwargs
        )
                
                
    @distributed_trace
    def get_traffic_incident_viewport(
        self,
        boundingbox,  # type: str
        boundingzoom,  # type: int
        overviewbox,  # type: str
        overviewzoom,  # type: int
        **kwargs  # type: Any
    ):
        # type: (...) -> "_models.TrafficIncidentViewportResult"
        
        return self._traffic_client.get_traffic_incident_tile(
            boundingbox,
            boundingzoom,
            overviewbox,
            overviewzoom,
            **kwargs
        )
