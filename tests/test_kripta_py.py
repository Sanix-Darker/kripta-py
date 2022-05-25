"""
test_kripta.py
"""
from kripta_py import KriptaAES, KriptaRSA


def test_aes():
    """
    We test the AES
    """
    k = KriptaAES()

    message = "secret-message"
    secret_key = "secret-code-password"
    encrypted_msg1 = k.encrypt(message, secret_key)
    encrypted_msg2 = k.encrypt(message, secret_key)

    # encrypted values should be differents
    assert encrypted_msg1 != encrypted_msg2

    # But decryptions should be the same
    assert (
        k.decrypt(encrypted_msg1, secret_key) ==
        k.decrypt(encrypted_msg2, secret_key)
    )

    # And most importantly we should have our message back
    assert k.decrypt(encrypted_msg1, secret_key).decode() == message


def test_rsa():
    """
    We test our RSA
    """
    k = KriptaRSA()

    pub_key = """-----BEGIN PUBLIC KEY-----
MIICITANBgkqhkiG9w0BAQEFAAOCAg4AMIICCQKCAgBQn49bqBS1U61tDXfaj+Rl
CrWRSPLOAEwASb1Co3rfUvaQEylOfJUAyL/1GyFXiw68pHeDA+FKY02IW4SsKbkT
nGKdO/QePz7L2W2dnRl5uulyimNFWNUPHA3OsB7F3/3QNjpiBtFs2d2aRwBOSawX
YeOdhWAt/tJPxVorbVzU9hn1KGIy0NRxJVbO5W/hzbJnL33LxTimO2DF5o7vQtCZ
l5O46JLrgcjG266yMid/ckkeF2Mbp5CvjZVFx6axnCBf5kFd4Oy+2G2pZTq4hbqc
cQMm8RLg17TwkhqzlbmDJA2zwPYRQeof3WQaVoIBFVfvG5zewNtxja3XLGGhjqO8
oGQvxykc1OdI4+eamZpzpjxI+LjO9II8chyXEyDebnrFIPVgcdaGeT7byzsUcxWY
uZlCzOEjmfqLumeh9c07lP0Q54G7extvBAYPpKj9c71Avo4oSWN6MBJbspR6CysV
IPaHALtGu9M+lBcqA7hpaLNG2eNQEeQ7HUL6K4gQh0qAf659v7jBOG3/AmDxtNiY
y71k5XztI2En0LsY89E0Q1lJuTdfuqA9tsSbdW6SaKrDPGqdwWf8A7Fg7yNPcTpb
AoMC4yppYokLU5wEdTz1kd5FENbTRAulTFvXBJmWPJrWGFr082soh2+oB68JQ2iy
TJPbps4pU4mbgpNc63YbFQIDAQAB
-----END PUBLIC KEY-----"""

    priv_key = """-----BEGIN RSA PRIVATE KEY-----
MIIJJgIBAAKCAgBQn49bqBS1U61tDXfaj+RlCrWRSPLOAEwASb1Co3rfUvaQEylO
fJUAyL/1GyFXiw68pHeDA+FKY02IW4SsKbkTnGKdO/QePz7L2W2dnRl5uulyimNF
WNUPHA3OsB7F3/3QNjpiBtFs2d2aRwBOSawXYeOdhWAt/tJPxVorbVzU9hn1KGIy
0NRxJVbO5W/hzbJnL33LxTimO2DF5o7vQtCZl5O46JLrgcjG266yMid/ckkeF2Mb
p5CvjZVFx6axnCBf5kFd4Oy+2G2pZTq4hbqccQMm8RLg17TwkhqzlbmDJA2zwPYR
Qeof3WQaVoIBFVfvG5zewNtxja3XLGGhjqO8oGQvxykc1OdI4+eamZpzpjxI+LjO
9II8chyXEyDebnrFIPVgcdaGeT7byzsUcxWYuZlCzOEjmfqLumeh9c07lP0Q54G7
extvBAYPpKj9c71Avo4oSWN6MBJbspR6CysVIPaHALtGu9M+lBcqA7hpaLNG2eNQ
EeQ7HUL6K4gQh0qAf659v7jBOG3/AmDxtNiYy71k5XztI2En0LsY89E0Q1lJuTdf
uqA9tsSbdW6SaKrDPGqdwWf8A7Fg7yNPcTpbAoMC4yppYokLU5wEdTz1kd5FENbT
RAulTFvXBJmWPJrWGFr082soh2+oB68JQ2iyTJPbps4pU4mbgpNc63YbFQIDAQAB
AoICABOyBwlzFCv/1xwO8DqacEcmyJhHY9ljRS3E1dFTso6f68/ifnLICHZ6lDpC
eHC0bdMzsmZ1KjJL9ALdqJmOT8I0r/qNTOOeu6583URlvnV4bdMnb3zfaJ0aU10s
tTfNsmmM9dJArCSVTIeF1NNLOBk2Nq6iiI5z89i883wsaUM1I746MVMMpPlHD9/X
OO/GmlCOz4JaGa6yTr/JxR06C0+aMeI4Hrwdpni97f1mNzPxLV+GgxWcZ8IbKl4z
mctFwrrquwk+C1fL824wZpnxQVc6XHTE68G1sGQcrR019G3O/vHsr7AjlBhYsz2j
6HpvRl4JNtdL8c/ZtqAcHXWkLOd/PV010w6w0PxDbrzPikMZE2wEkNiVoHChj2Kb
DDGzMshx9rF94dLudPoWFCLShTZonKV2kYSE4UwzR582uSF8l4o4jbvMXFQYd1jF
yeBZ4JU1XHn2KUIkbGleVX5Jo3X60h8BsYe0+j68QHwC+8WrfUT2HAT2/VCwLN4W
dcchMG9bs3bjygdPB0fa+reWgMIFt7BjQ+mfPetTO2PPA2lOlne1YzNn0y/eK1DA
4uPHOZNz9e2ILl+nijZm9dTC1NAabZO7cFmM1IpJ1DofwYX9i6eILvzIV5fXcKVw
4VOiqFaC2RbEoEE3IUWF41M/fWyOu9pvii6ewWH95Hd7zmK5AoIBAQCans8gWzNL
TYIW1lImhCWSt/JbTkF8j+ikgskOWSmVxXNvckIvodeU+WZ8QnT+nNIRGwDxKYwQ
nGzjETvKGfUCqDur1iszqtPxnj1+hUkqcdXt/4lBVFFfK4mHgkum6F9BHyudbv1a
fXbabqVkEuF7MRxaPGOyAZH48NzeNRNCQV5tieyUXekZfib1dGJVRtYsWq+vkpz+
BXaQ6ox3kGTNgy0MAMsw6qzZESZmtEFyIVPkawF5LdY87vNg62mkuLxOsmfThyOH
uZ/sEo9GDXC0GT1+7xdq2OU/wjAY/5sYOD+nGi/mecm1y0qE6xJjYrjnyVuu5l3+
+YKoIJIG02SLAoIBAQCFfEOYP8jrfybk8MmUlcRhggSuq+7voaM90YLkBRBqPdj0
+MgIA1tjK2LGceidX6gm7N/64cnFVUbWw8NKfdVuRgNg9afYyXiNgWrFfElhjXBI
vjfiwEKIdUNlxcViFwgnie+mcotYzBQudjWT2XTAZtDeXHTpvysFVtfiWmpOWUxY
pUb0p4PFzJZ8v786VtAL7ivG+Mkr/EFE0vZtvyiGT0eQaqm5afhU51Bnu99mcfuV
YMYcOWH209uk20GJ9nW/hlBGi9DSLJdnLUrHcraLz4B0/KpNV/jURo3KpllbAeS1
43VMBedyhpTZg4Gnwn7gMgAfOyGxfyrvARTj91LfAoIBAArx2NmCeyQGbYHuU8xU
KFC1Ypth87K8gQw8Eb1JRG9Mlbo6zUKP4zGxYbbEAYIQWbJKRgvMFBUM7Yw5KRFK
OxSgEfE87LvwiKYevF2bU62Ed08semu8azIgY9DKwU4kPrHeYfj35UklfmdB08U8
rOdKd6ZPhgMQp2OGsSuteBqFhAie7bcm2pwqWNmhDmDY7cof9TWpXCGDA3yIjb7c
4rXFZkfmOnvQ8MFAvIYilktc3pJZnLYWL4cKpwGiSE0XooSzjjPj6fjug8pzGd8s
jmDBNKAqjm7KwZd8yGjMlw7k1GSgrulSj5ulszWrahbM4yfNEgdUWSz2PnBmNc/z
4LcCggEAD+fDoiOPjEgFWWg7jMHfuYKlji6cdN88tUP+pa7Yyt/9twrhwtqrjACC
b4TpI79fKOw2sA0xXpsPqs1+uqSNxur+whHjYxh2jd3q3Ac4MzCIPZK01Ab2po3a
bwkGwO5foV51OM8TPYxrpzGcprZVjAt0Pdqkb6nAtY0ogicl3ZoUV8ex0bsYH3yG
Pe0XGxt3BMTnYHkKd3xCRrIgfOk3KfHOZC3hdV9kILHDSej/8JQKVz1Fvd00iBWs
aVNa1taQJzcY358PTcvUao3iCCvqBnS+KLJmlHq0Ao85m/kAUrDCEM4+jsVxU5sn
p1ddHqE1Pv+WNiJ0nFK7yejGFXfF3wKCAQADPrRRwGRwH0ZUDTdviadnbhM/igYl
2qRLJKWKOtyP4qQTqJzViEGJaAS7ZwjgA+ImIAyczBf4pPT0ySxsi9y7nkLdCc3q
wHQc0/w5jzRQivxO6dy2ydG+gaTSLzt9/Gx5JkXeKuoOLYJWkcF90WsmNqOn/OWY
o6eGlByPr1HQBPhWuCJgpS5JjXmcueP9LCR3odGUZj9L+/FiVS9JQ+nA2lrK2DTd
foP1vLQwGljIabv2sT3U0KASc25z/pnVxu7Z53+eD2KaWf+5XAihEjKfLS1ay8jY
9PcYCMGfq9tKTkXhkX0YAfKAk1C8TMUR2BLcK6Jr+u79hRLtQAQH8stJ
-----END RSA PRIVATE KEY-----"""

    k.setPublicKey(pub_key)
    k.setPrivateKey(priv_key)

    message = (
        "cascsac acasc ascascasc ascsacdcsdsvdscdscascascacdcsdsecret message"
        "cascsac acasc ascascasc ascsacdcsdsvdscdscascascacdcsdsecret message"
        "cascsac acasc ascascasc ascsacdcsdsvdscdscascascacdcsdsecret message"
        "cascsac acasc ascascasc ascsacdcsdsvdscdscascascacdcsdsecret message"
        "cascsac acasc ascascasc ascsacdcsdsvdscdscascascacdcsdsecret message"
        "cascsac acasc ascascasc ascsacdcsdsvdscdscascascacdcsdsecret message"
        "aqsssvdscdscascascacdcsdsecret message"
    )
    assert len(message) == 446
    # We tests getters/Setters
    assert k.getPublicKey().decode() == pub_key
    assert k.getPrivateKey().decode() == priv_key

    encrypted_msg1 = k.encrypt(k.getPublicKey(), message.encode())
    encrypted_msg2 = k.encrypt(k.getPublicKey(), message.encode())
    # We need to have a different value for each encryption
    assert encrypted_msg2 != encrypted_msg1

    # But the same value on decryption
    assert k.decrypt(encrypted_msg1) == k.decrypt(encrypted_msg2)
