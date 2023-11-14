Winternitz One-Time-Signature
==============================

Python implementation of Winternitz one-time-signature schemes

Description
-----------

Winternitz one-time-signature is an extension of lamport one-time-signature.
This python package can be used to execute WOTS operations, including
key generation, signature generation and signature verification.
Currently WOTS and WOTS+ are implemented.

Introduction
------------
Lamport invented an algorithm in 1979 which allowed one to create one-time-signatures
using a cryptographically secure one-way function. It is the basis for the Winternitz
one-time-signature algorithm. Winternitz added the possibility to adjust the tradeoff
between time- and space-complexity.

Lamport one-time-signature scheme
-----------
Lamport suggested to create two secret keys for each bit of a message which will
be signed. One for each value the bit can take. To derive the verification key,
each secret key is hashed once. Now you have a secret key and a verification key,
which consists of `m` 2-tuples of values, where `m` is the number
of bits of the message. The verification key is published.
The signature consists of `m` values. For each bit of the message you release a secret key from
the corresponding secret keys, depending on which value the bit has. All those secret
keys form the signature for the message. The verifier hashes each of your secret keys
once and compares it to one verification key for this position, depending on the value
of the bit. The signature is valid, if and only if all derived verification keys match with
your published verification key at the correct position of the 2-tuple, which is determined by the value
of the bit. This algorithm is quite fast
(comparing it to existing PQC-algorithms), but the signature sizes are huge.

## How to use

1) python generate_keys.py - creates private and public keys
2) python sign_message.py - generate signature for message
3) python verify_signature.py - verify message with signature