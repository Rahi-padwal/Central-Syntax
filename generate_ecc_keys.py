from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import serialization

print("🔐 Generating ECC Key Pair...")

# Generate ECC private key
private_key = ec.generate_private_key(ec.SECP384R1())
public_key = private_key.public_key()

# Save private key
with open("ecc_private_key.pem", "wb") as f:
    f.write(private_key.private_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PrivateFormat.PKCS8,
        encryption_algorithm=serialization.NoEncryption()
    ))

# Save public key
with open("ecc_public_key.pem", "wb") as f:
    f.write(public_key.public_bytes(
        encoding=serialization.Encoding.PEM,
        format=serialization.PublicFormat.SubjectPublicKeyInfo
    ))

print("ECC Keys Generated Successfully!")
print("📁 Private Key: ecc_private_key.pem (KEEP THIS SECURE!)")
print("📁 Public Key: ecc_public_key.pem")
print("⚠️  IMPORTANT: Never commit ecc_private_key.pem to version control!") 