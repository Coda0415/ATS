import dkim

def sign_payload(private_key, selector, domain, payload):
    signature = dkim.sign(
        message=payload,
        selector=selector,
        domain=domain,
        privkey=private_key,
    )
    return signature

# Example usage
private_key = """
-----BEGIN RSA PRIVATE KEY-----
...
-----END RSA PRIVATE KEY-----
"""

selector = "selector"
domain = "example.com"
payload = "Your payload here"

signature = sign_payload(private_key, selector, domain, payload)
print(signature)
