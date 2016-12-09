# CSE591 - Diffie–Hellman key exchange overview
The Diffie-Hellman key agreement protocol (1976) was the first
practical method for establishing a shared secret over an unsecured
communication channel.
The point is to agree on a key that two parties can use for a
symmetric encryption, in such a way that an eavesdropper cannot
obtain the key.

#Authors
#### Leixiang Wu

## (1) the problem, i.e., what's given and what's wanted for your project
DistAlgo is a language for distributed algorithms. It is an extension to Python.
It makes programming distributed algorithm very easily.
However, the DistAlgo lacks security protocol to allow processes communicating securely.
For this project, I am going to implement Diffie-Hellman key exchange.

## (2) the method that you use to solve the problem
I will use DistAlgo to communicate. If we have time, we could use an encryption scheme
to actually encrypt the messages that are delivered among processes.

## (3) the implementation of the method 
After that, I will use DistAlgo built-in functions to
to send keys to each other. I will also implement DH in Erlang.

## (4) the results, including the runs and tests you performed, with resulting numbers, plots, graphs, etc. Each part should also include brief justifications for why you did what you did.
We will find some best existing implementations of DF-key protocols.
Compare the performances and clarity among them. 


Sources:
https://en.wikipedia.org/wiki/Diffie%E2%80%93Hellman_key_exchange
https://www.cs.utexas.edu/~byoung/cs361/lecture52.pdf
https://drive.google.com/file/d/0B0MWH8ngLAIFTzFna1lOTTF4UlE/view
