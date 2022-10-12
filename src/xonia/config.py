from yarl import URL

__all__ = [
    "API_URL",
    "USER_DATE_FORMAT",
    "COOKIE_EXPIRE_FORMAT",
    "SUPPORTED_TYPES"
]

API_URL = URL("https://gateway.xoniaapp.com/api")

USER_DATE_FORMAT = "%Y-%m-%dT%H:%M:%S.%fZ"
COOKIE_EXPIRE_FORMAT = "%a, %d %b %Y %H:%M:%S %Z"

SUPPORTED_TYPES = [
    "image/jpg"
    "image/vnd.microsoft.icon"
    "image/gif"
    "image/jpeg"
    "image/png"
    "image/svg"
    "audio/mp3"
    "audio/mpeg"
    "audio/opus"
    "video/mpeg"
    "video/mp4"
    "application/json"
    "application/zip"
    "application/gzip"
    "application/ld+json"
    "application/pdf"
    "application/vnd.rar"
    "application/x-tar"
    "application/x-7z-compressed"
    "application/x-bzip"
    "application/x-bzip2"
    "application/octet-stream"
    "application/x-binary"
    "application/*"
]