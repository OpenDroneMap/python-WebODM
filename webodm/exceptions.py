from requests import HTTPError


class ParamRequired(HTTPError):
    """A required parameter is missing."""


class NonFieldErrors(HTTPError):
    """A non field error ocurred."""
