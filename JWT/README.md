# Authentication & Security – Learning Notes

This document contains the authentication, authorization, and security concepts I learned while working on the Nexora project.

## 1. JSON Web Token (JWT)
JWT is a compact, secure way of transferring information between a client and a server. It is commonly used to verify a user's identity after successful login.

## 2. JWT Header
The header contains metadata about the token, including the token type (JWT) and the signing algorithm (such as HS256). It helps the server understand how the token was created and signed.

## 3. JWT Payload
The payload contains claims or information about the user, such as their email, user ID, and token expiration time. This information is encoded but not encrypted, so sensitive data should not be stored in it.

## 4. JWT Signature
The signature verifies that the token has not been modified after it was created. It is generated using the encoded header, payload, and a secret key or private key.

## 5. Access Token
An access token is used to authenticate and authorize requests to protected APIs or resources. It usually has a short expiration time to reduce security risks.

## 6. Refresh Token
A refresh token is used to obtain a new access token when the existing access token expires. It generally has a longer lifetime and must be stored securely.

## 7. Registering an Application
Application registration is the process of creating an application with an authentication or authorization provider. It provides the application with credentials and configuration details needed to establish secure communication.

## 8. Redirect URL
A redirect URL is the address where the authentication provider sends the user after completing the authentication process. It must match the URL registered in the application settings.

## 9. Scope
A scope defines the permissions an application requests from a user or authorization provider. It determines what resources or actions the application is allowed to access.

## 10. TOML
TOML (Tom's Obvious, Minimal Language) is a configuration file format used to store application settings in a readable structure. It supports key-value pairs, tables, and nested configuration sections.

## 11. Client Secret
A client secret is a confidential credential used by an application to authenticate itself with an authorization server. It must be stored securely and should never be exposed in frontend code or public repositories.

## 12. Cryptography
Cryptography is the practice of securing information using mathematical techniques. It helps protect data through encryption, decryption, digital signatures, and verification.

## 13. Private Key
A private key is a confidential cryptographic key used to sign data or decrypt information, depending on the cryptographic system. It must only be accessible to authorized parties.

## 14. Public Key
A public key is a cryptographic key that can be shared with others. It can be used to verify digital signatures created using the corresponding private key or to encrypt data for the private key owner.

## 15. Token Expiry
Token expiry defines the time period for which an authentication token remains valid. Once the token expires, the user may need to obtain a new access token using a refresh token or authenticate again.