"""amazing-software-factories: measure the repositories one person ships at factory pace."""
from pathlib import Path
import tomllib

ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / "data"
CONFIG = tomllib.loads((ROOT / "config.toml").read_text())
METHOD_VERSION = "1"
