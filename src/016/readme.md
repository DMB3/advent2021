Packet Decoder
==============

https://adventofcode.com/2021/day/16

A class was created to represent a packet with the stream of characters for that packet. First part is straightforward
after implementing the operations described, we only need to traverse the packet hierarchy and sum all the versions. For
the second part we recursively evaluate all operations described and return the result.
