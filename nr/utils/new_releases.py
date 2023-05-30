from ..schemas.releasehook import ReleaseHook
from ..configs.config import settings
from hmac import HMAC

import hmac
import hashlib


def verify_signature(signature: str, timestamp: str, release: ReleaseHook) -> bool:
    secret: str = settings.newreleases_webhook_verify_key
    message: str = f"{timestamp}.{''.join(release.json(skip_defaults=True).split())}"
    _hmac: HMAC = hmac.new(
        key=secret.encode(),
        msg=message.encode(),
        digestmod=hashlib.sha256
    )

    return _hmac.hexdigest() == signature
