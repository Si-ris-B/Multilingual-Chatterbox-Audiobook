# try:
#     from importlib.metadata import version
# except ImportError:
#     from importlib_metadata import version  # For Python <3.8
#
# __version__ = version("chatterbox-tts")
__version__ = "local-dev" # You can put any string here



from .tts import ChatterboxTTS
from .vc import ChatterboxVC
from .mtl_tts import ChatterboxMultilingualTTS, SUPPORTED_LANGUAGES