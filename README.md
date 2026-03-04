# prodigy.cs.02
To develop a simple image encryption tool using pixel manipulation, you can use the Pillow library in Python to perform operations like XORing pixel values with a key. This method is effective because the XOR operation is its own inverse, meaning applying the same operation twice returns the original data.
How it Works
Pixel Loading: The tool uses the Pillow Image module to open the image and load() to access the pixel data.
Mathematical Operation: It applies a bitwise XOR to each RGB channel (Red, Green, Blue) using a user-provided integer key.
Reversibility: Because 
, applying the same key to an encrypted image automatically decrypts it back to its original state.
Security: While this is useful for learning pixel manipulation, it is a basic form of encryption that can be easily broken. For sensitive data, industry-standard libraries like PyCrypto or cryptography are recommended.