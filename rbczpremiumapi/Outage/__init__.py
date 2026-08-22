# coding: utf-8

"""
RB API gateway outage detection for Raiffeisen Bank Premium API.

Detects the gateway's undocumented outage signal (HTTP 500 with an
``outage: yes`` response header) so applications can distinguish a
site-wide RB outage from a per-request error and react accordingly
(e.g. skip retries, surface a clear "RB is down" message).
"""

from rbczpremiumapi.Outage.outage_exception import OutageException

__all__ = [
    "OutageException",
]
