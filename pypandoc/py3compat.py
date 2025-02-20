import locale
import sys

# from http://stackoverflow.com/questions/11687478/convert-a-filename-to-a-file-url
from urllib.parse import urljoin, urlparse
from urllib.request import pathname2url, url2pathname

# compat code from IPython py3compat.py and encoding.py,
# which is licensed under the terms of the Modified BSD License
# (also known as New or Revised or 3-Clause BSD)
_DEFAULT_ENCODING = None
try:
    # There are reports of getpreferredencoding raising errors
    # in some cases, which may well be fixed, but let's be conservative here.
    _DEFAULT_ENCODING = locale.getpreferredencoding()
except Exception:
    pass

_DEFAULT_ENCODING = _DEFAULT_ENCODING or sys.getdefaultencoding()


def _decode(s, encoding=None):
    encoding = encoding or _DEFAULT_ENCODING
    return s.decode(encoding)


def _encode(u, encoding=None):
    encoding = encoding or _DEFAULT_ENCODING
    return u.encode(encoding)


def cast_unicode(s, encoding=None):
    if isinstance(s, bytes):
        return _decode(s, encoding)
    return s


def cast_bytes(s, encoding=None):
    # bytes == str on py2.7 -> always encode on py2
    if not isinstance(s, bytes):
        return _encode(s, encoding)
    return s


def path2url(path):
    return urljoin("file:", pathname2url(path))


def url2path(url):
    return url2pathname(urlparse(url).path)
