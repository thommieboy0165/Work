The purpose of the TELNET Protocol is to provide a fairly general, bi-directional, eight-bit byte oriented communications facility. A TELNET connection is a Transmission Control Protocol (TCP) connection used to transmit data with interspersed TELNET control information.

The TELNET Protocol is built upon three main ideas:  first, the concept of a "Network Virtual Terminal"; second, the principle of negotiated options; and third, a symmetric view of terminals and processes.

When a Telnet connection is first established, each end is assumed to originate and terminate at a “Network Virtual Terminal”. An NVT is an imaginary device which provides a standard,
network-wide, intermediate representation of a canonical terminal. This eliminates the need for "server" and "user" hosts to keep information about the characteristics of each other's terminals and
terminal handling conventions.

There are two different protocols from different network layers involved in the TELNET "Synch" signal. What other protocol is involved and why is it necessary?
Ip is the other protocol that is necessarry for telnet. Without the IP protocol it is not possible to setup a connection between the user and server.
