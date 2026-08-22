# coding: utf-8

"""
Exception raised when the RB API gateway itself reports being down, rather
than rejecting an individual request.
"""

from typing import Any, Optional

from rbczpremiumapi.exceptions import ApiException


class OutageException(ApiException):
    """Raised when the RB gateway signals a site-wide outage.

    Raiffeisenbank's gateway signals this by returning HTTP 500 together with
    an ``outage: yes`` response header on every endpoint, regardless of
    account/certificate/client - distinct from a per-request 500 caused by
    bad input or a transient backend error. Extends :class:`ApiException` so
    that callers who already ``except ApiException`` around API calls catch
    this too, without needing a separate ``except`` clause, while still being
    able to catch it specifically to skip retries or surface a clearer
    "RB is down" message.
    """

    @staticmethod
    def is_outage_response(status: Optional[int], headers: Optional[Any]) -> bool:
        """Detect the RB gateway's outage signal on a raw HTTP response.

        :param status: the HTTP status code
        :param headers: the response headers, as anything exposing a
            case-insensitive ``.get(name)`` (e.g. urllib3's
            ``HTTPHeaderDict``, or a plain ``dict`` with a lower-cased key)
        """
        if status != 500 or headers is None:
            return False

        value = None

        get = getattr(headers, "get", None)

        if callable(get):
            value = get("outage")

            if value is None:
                value = get("Outage")
        else:
            for name, header_value in headers:
                if name.lower() == "outage":
                    value = header_value
                    break

        return value is not None and str(value).strip().lower() == "yes"

    @classmethod
    def from_api_exception(cls, exc: ApiException) -> Optional["OutageException"]:
        """Convert an already-caught :class:`ApiException` into an
        :class:`OutageException`, or return ``None`` if it isn't one.

        Typical usage::

            try:
                ...
            except ApiException as exc:
                outage = OutageException.from_api_exception(exc)
                if outage is not None:
                    raise outage from exc
                raise
        """
        if not cls.is_outage_response(exc.status, exc.headers):
            return None

        outage = cls(
            status=exc.status,
            reason=exc.reason,
            body=exc.body,
            data=exc.data,
        )
        outage.headers = exc.headers

        return outage
