# kripta-py

An simple implementation of a Symmetric(AES) and Asymmetric(RSA) encryption based on [pycryptodome](https://github.com/Legrandin/pycryptodome) module.

## Requirements

- Python (3.10 recommended)

## Features

- Generate RSA keys like
- Encrypt/Decrypt messages, files, binaries on symmetric or asymmetric

## How to use

- Install the lib
```bash
pip install kripta-py
```

- To use the **symmetric encryption** (AES):
    - Schema :

        <img
            src="https://github.com/Sanix-Darker/kripta/raw/master/images/s.png"
            alt="drawing"
            width="400"
        />
    - Code :
        ```python
        from kripta_py import KriptaAES


        message = "secret-message"
        secret_key = "secret-code-password"

        k = KriptaAES()
        # to encrypt
        encrypted_msg = k.encrypt(message, secret_key)

        # to decrypt
        print(k.decrypt(encrypted_msg1, secret_key).decode())
        # secret-message 
        ```

- To use an **asymmetric encryption** (RSA):
    - Schema :

        <img
            src="https://github.com/Sanix-Darker/kripta/raw/master/images/as.gif"
            alt="drawing"
            width="400"
        />
    - Code example:
        ```python
        from kripta_py import KriptaRSA


        message = "secret-message"
        pub_key = """-----BEGIN PUBLIC KEY-----
        ....
        -----END PUBLIC KEY-----"""

        k = KriptaRSA()
        k.setPublicKey(pub_key)
        # To encrypt a message
        encrypted_msg = k.encrypt(k.getPublicKey(), message.encode())

        priv_key = """-----BEGIN RSA PRIVATE KEY-----
        .....
        -----END RSA PRIVATE KEY-----"""

        k.setPrivateKey(priv_key)
        # To decrypt
        print(k.decrypt(encrypted_msg).decode())
        # secret-message 
        ```
