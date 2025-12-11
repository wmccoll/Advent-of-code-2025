### Advent of Code 2025

Gonna try and do this relatively on time this year, started late but I'll be happy if I can get at least half of the days done. Will also be keeping notes here on each day

#### Day 1

The first problem (`Day1.py`) was relatively quick, but when attempting to expand my work to encompass the second part of the day's problem, I forgot that counting upwards and downwards from a multiple of 100 would need to be handled differently depending on positive/negative state. I eventually rewrote my algorithm after doing some rubber duck debugging, and ended up with a solution that I'm overall happy with, even if it's not the most concise. 


#### Day 2

I found this one to be a good bit quicker, and used this as an opportunity to practice with some basic data structure stuff for efficiency. The first part was a one and done, just needing to convert each value to a string, see if it's length was even, and count it if the first half was the same as the second. The extension had me wonder for a bit on how to best automate splitting of an arbitrary length, but then I recalled some basic math knowledge that a prime factorization would come in handy, and used the properties of a set to quickly check if all the entries in my subdivided number would be the same. Initially, I forgot to exit out of the factorization if we found a winning answer, so numbers like `666666` would get counted twice, but adding a quick `break` statement fixed that issue, and it was smooth sailing. There is probably a more efficient way to handle this than just loops, but I think I did an okay job of stopping calculations when we got to a point that it wasn't possible for each entry to be the same, so I'm not too bothered. 