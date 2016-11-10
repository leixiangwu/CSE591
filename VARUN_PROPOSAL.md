# CSE591 - Diffie–Hellman key local
Diffie-Hellman uses the concept of one-way functions to exchange a secret over an unsecure channel in a secure way. That is, two parties can exchange a secret number even in the precence of an almost omnipotent eavesdropper. The transferred key can then be used to cryptographically encrypt messages over the network. The key exchange is a foundation that can be used for instance as the pad in the one-time-pad encryption scheme.

#Authors
#### Leixiang Wu
#### Varun Sayal

## (1) the problem, i.e., what's given and what's wanted for your project
My part of the project would essentially serve as an API to do the one-way function computations needed for the key exchange. In this n-person key exchange at the crucial stage of the key computation we need to compute ~N modular exponentiations. My part of the project would provide API's to compute the appropriate secret value to send to the other parties.

## (2) the method that you use to solve the problem
There is well studied and tested pseudocode to describe what needs to be sent over the network in the key-exchange. And while this logic is cool, the more interesting part is to do the efficient computation of the modular exponentiation needed for Diffie-Hellman. There are interesting properites of binary that will allow for A ^ B % C to be calculated quickly using smaller computations. By incrementalizing this I hope to implement a way for fast modular exponentiation to happen N times.

## (3) the implementation of the method 
The implementation of the method will be in Python, using the idea presented in source #BLANK. The distributed system stuff will be implemented in DistAlgo.

## (4) the results, including the runs and tests you performed, with resulting numbers, plots, graphs, etc. Each part should also include brief justifications for why you did what you did.
In the results I hope to include many different methods to compute this modular exponentiation as well as their relative running times. I also hope to include some documentation detailing the ideas behind each specific implementation.


Sources:
http://sublimerobots.com/2015/01/simple-diffie-hellman-example-python/

https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/fast-modular-exponentiation

http://crypto.stackexchange.com/questions/1025/can-one-generalize-the-diffie-hellman-key-exchange-to-three-or-more-parties
