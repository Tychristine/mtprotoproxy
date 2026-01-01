PORT = 22111

USERS = {
    # 32位16进制字符串
    "tg":  "xxx",
}

MODES = {
    # Classic mode, easy to detect
    "classic": False,

    # Makes the proxy harder to detect
    # Can be incompatible with very old clients
    "secure": False,

    # Makes the proxy even more hard to detect
    # Can be incompatible with old clients
    "tls": True
}
TLS_DOMAIN = "endfield.gryphline.com"
