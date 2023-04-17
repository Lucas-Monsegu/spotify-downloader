"""
Audio providers for spotdl.
"""

from spotdl.providers.audio.base import (
    ISRC_REGEX,
    AudioProvider,
    AudioProviderError,
    YTDLLogger,
)
from spotdl.providers.audio.youtube import YouTube
from spotdl.providers.audio.ytmusic import YouTubeMusic
from spotdl.providers.audio.sliderkz import SliderKZ

__all__ = [
    "YouTube",
    "YouTubeMusic",
    "SliderKZ",
    "AudioProvider",
    "AudioProviderError",
    "YTDLLogger",
    "ISRC_REGEX",
]
