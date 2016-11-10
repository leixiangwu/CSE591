# CSE591 - Diffie–Hellman key exchange overview
The Diffie-Hellman key agreement protocol (1976) was the first
practical method for establishing a shared secret over an unsecured
communication channel.
The point is to agree on a key that two parties can use for a
symmetric encryption, in such a way that an eavesdropper cannot
obtain the key.

#Authors
#### Leixiang Wu
#### Varun Sayal

## (1) the problem, i.e., what's given and what's wanted for your project
DistAlgo is a language for distributed algorithms. It is an extension to Python. It makes programming distributed algorithm very easily. However, the DistAlgo lacks security protocol to allow processes communicating securely. For this project, we are going to implement Diffie-Hellman key exchange. We implement a fast way to compute Diffe-Hellman keys and extends DistAlgo to use Diffe-Hellman key exchange protocol to send messages.

## (2) the method that you use to solve the problem
We will use Fast modular exponentiation to compute the DF keys. After each process has a secret number to communicate, we will use DistAlgo to communicate. If we have time, we could use an encryption scheme to actually encrypt the messages that are delivered among processes.

## (3) the implementation of the method 
Use fast modular exponentiation method to compute DF keys efficiently. After that, use DistAlgo to send keys to each other. Then each process can use any encryption schema to encrypts the messages.

## (4) the results, including the runs and tests you performed, with resulting numbers, plots, graphs, etc. Each part should also include brief justifications for why you did what you did.
We will find some best existing implementations of DF-key computations and protocols. Compare the performances among them. Also, we can replace DF-key computations with different implementations while leaving protocol unchanged. This could evaluate the performance of our DF key computation.


Sources:
https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
https://www.cs.utexas.edu/~byoung/cs361/lecture52.pdf
https://drive.google.com/file/d/0B0MWH8ngLAIFTzFna1lOTTF4UlE/view
