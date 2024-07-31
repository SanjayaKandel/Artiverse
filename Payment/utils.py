import hmac
import hashlib
import base64

def generate_signature(secret_key, data, signed_field_names):
    # Construct the string to be signed
    fields = [data[field] for field in signed_field_names.split(',')]
    message = ','.join(f'{name}={value}' for name, value in zip(signed_field_names.split(','), fields))
    
    # Generate HMAC SHA256 signature
    signature = hmac.new(secret_key.encode(), message.encode(), hashlib.sha256).digest()
    
    # Encode the signature in base64
    encoded_signature = base64.b64encode(signature).decode()
    print(encoded_signature)
    return encoded_signature