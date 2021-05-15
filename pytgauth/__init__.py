import hashlib
import hmac

def verify(data, token):
    """Pass a JSON dict of received value from Telegram as data, and Bot token as token."""
    myhash = data.pop('hash')
    alph_order = sorted(data.items(), key=lambda x: x[0])
    string = []
    for data_pair in alph_order:
        key, value = data_pair[0], data_pair[1]
        string.append(f"{key}={value}")
    string = '\n'.join(string)
    received_hash = hmac.new(hashlib.sha256(token.encode()).digest(), msg=string.encode(), digestmod=hashlib.sha256).hexdigest()

    if received_hash == myhash:
        return True
    return False
    


