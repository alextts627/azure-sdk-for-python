# -------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING
from azure.core.tracing.decorator import distributed_trace
from azure.core.exceptions import HttpResponseError
from ._generated._route_client import RouteClient as RouteClientGen
from ._generated.models import *
from .models import *
# from .utils import get_authentication_policy, get_headers_policy

if TYPE_CHECKING:
    from typing import Any, List, Optional, Object
    from azure.core.credentials import TokenCredential
    from azure.core.polling import LROPoller

class RouteClient(object):
    """Azure Maps Route REST APIs.
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

        self._route_client = RouteClientGen(
            credential,
            **kwargs
        ).route