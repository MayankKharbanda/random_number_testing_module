# ENT

# 1).Entropy
It tries to compress the random numbers file. The better the algorithm the less likely the file would compress.


# 2).Chi-square Test
The chi-square distribution is calculated for the stream of bytes in the file and expressed as an absolute number and a percentage which indicates how frequently a truly random sequence would exceed the value calculated. We interpret the percentage as the degree to which the sequence tested is suspected of being non-random. 


# 3).Arithmetic Mean
This is simply the result of summing the all the bytes (bits if the -b option is specified) in the file and dividing by the file length.


# 4).Monte Carlo Value for Pi
Each successive sequence of six bytes is used as 24 bit X and Y co-ordinates within a square. If the distance of the randomly-generated point is less than the radius of a circle inscribed within the square, the six-byte sequence is considered a “hit”. The percentage of hits can be used to calculate the value of Pi.


# 5).Serial Correlation Coefficient
This quantity measures the extent to which each byte in the file depends upon the previous byte. For random sequences, this value (which can be positive or negative) will, of course, be close to zero.


### Source: https://www.fourmilab.ch/random/
