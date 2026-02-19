try:
    from importlib.metadata import version, PackageNotFoundError
except ImportError:
    from importlib_metadata import version, PackageNotFoundError

try:
    __version__ = version("chatterbox-tts")
except (PackageNotFoundError, ImportError):
    __version__ = "0.0.0+local"

from .tts import ChatterboxTTS
from .vc import ChatterboxVC
from .mtl_tts import ChatterboxMultilingualTTS, SUPPORTED_LANGUAGES
# If you are using Turbo, ensure this line is present (if it exists in your folder structure)
# If tts_turbo.py is not in src/chatterbox/, remove this line.
try:
    from .tts_turbo import ChatterboxTurboTTS
except ImportError:
    pass