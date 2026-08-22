# coding: utf-8

"""Tests for OutageException."""

from rbczpremiumapi.exceptions import ApiException
from rbczpremiumapi.Outage.outage_exception import OutageException


class TestOutageExceptionIsOutageResponse:
    def test_true_for_status_500_with_outage_header_dict(self):
        assert OutageException.is_outage_response(500, {"outage": "yes"}) is True

    def test_true_case_insensitive_on_value(self):
        assert OutageException.is_outage_response(500, {"outage": "YES"}) is True

    def test_true_with_list_of_tuples_headers(self):
        assert OutageException.is_outage_response(500, [("Outage", "yes")]) is True

    def test_false_for_status_500_without_outage_header(self):
        assert OutageException.is_outage_response(500, {}) is False

    def test_false_for_none_headers(self):
        assert OutageException.is_outage_response(500, None) is False

    def test_false_for_other_status_with_outage_header(self):
        assert OutageException.is_outage_response(503, {"outage": "yes"}) is False

    def test_false_for_outage_header_no(self):
        assert OutageException.is_outage_response(500, {"outage": "no"}) is False


class TestOutageExceptionFromApiException:
    def test_extends_api_exception(self):
        exc = OutageException(status=500, reason="Outage")
        assert isinstance(exc, ApiException)

    def test_converts_matching_api_exception(self):
        exc = ApiException(status=500, reason="Internal Server Error")
        exc.headers = {"outage": "yes"}
        exc.body = "body"
        exc.data = None

        outage = OutageException.from_api_exception(exc)

        assert outage is not None
        assert isinstance(outage, OutageException)
        assert outage.status == 500
        assert outage.headers == {"outage": "yes"}

    def test_returns_none_for_non_outage_api_exception(self):
        exc = ApiException(status=500, reason="Internal Server Error")
        exc.headers = {}

        assert OutageException.from_api_exception(exc) is None

    def test_returns_none_for_non_500_api_exception(self):
        exc = ApiException(status=503, reason="Service Unavailable")
        exc.headers = {"outage": "yes"}

        assert OutageException.from_api_exception(exc) is None
