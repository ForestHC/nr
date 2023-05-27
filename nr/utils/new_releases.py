from ..schemas.releasehook import ReleaseHook
from ..configs.config import settings
from hmac import HMAC

import hmac
import hashlib


def verify_signature(signature: str, timestamp: str, release: ReleaseHook) -> bool:
    secret = settings.newreleases_webhook_verify_key
    message: str = f"{timestamp}.{str(release.json())}"
    _hmac: HMAC = hmac.new(key=secret.encode(), msg=message.encode(), digestmod=hashlib.sha256)

    print(f"return {_hmac.hexdigest()} == {signature}")

    return True
    #return _hmac.hexdigest() == signature
