"""Settings module for test app."""
ENV = "development"
TESTING = True

from pathlib import Path
import os
basedir = Path(__file__).resolve().parent
DATABASE = "flaskr.db"
url = os.getenv("DATABASE_URL", f"sqlite:///{Path(basedir).joinpath(DATABASE)}")
if url.startswith("postgres://"):
    url = url.replace("postgres://", "postgresql://", 1)
SQLALCHEMY_DATABASE_URI = url

SECRET_KEY = "not-so-secret-in-tests"
BCRYPT_LOG_ROUNDS = (
    4  # For faster tests; needs at least 4 to avoid "ValueError: Invalid rounds"
)
DEBUG_TB_ENABLED = False
CACHE_TYPE = "simple"  # Can be "memcached", "redis", etc.
SQLALCHEMY_TRACK_MODIFICATIONS = False
WTF_CSRF_ENABLED = False  # Allows form testing
USE_REDIS = False
USE_ES = False
DATABASE_QUERY_TIMEOUT = 1000
