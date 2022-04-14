'''
Description
---------------
A set of documents describe how to build a faster-than-light communications system. The only problem is that when a message is sent, its binary representation is encoded and must be decrypted on the other side. The binary string (B ) is of length N. This string is written down K times, shifted respectively by 0, 1, ..., K - 1 bits.

For example, if B = 1001010 and K = 4 it would appear as:

1001010   
 1001010  
  1001010 
   1001010
Next, calculate XOR in every column and write it down. This number representing the encoded message is call S. For example, XOR-ing the numbers in the above example results in:

1110100110
Both the encoded message (S ) and the value K are sent to the recipient.

You must implement a decoding algorithm that will take S and K and reproduce the original bitstring B (in the above case, you would output '1001010').

Input Format
---------------
The first line contains two integers, N and K.
The second line contains the received string S of length N + K - 1, consisting of ones and zeros.

Constraints
---------------
1 ≤ N,K ≤ 106

Output Format
---------------
The decoded message of length N, consisting of ones and zeros.

Example 0
---------------
Sample Input
7 4
1110100110

Sample Output
1001010

Explanation
---------------
1001010
 1001010
  1001010
   1001010   XOR
----------
1110100110
So, how did we find this solution?

Lets replace each bit with a true/false variable; we must use the encrypted sequence we were provided to determine those original variables.

abcdefg
 abcdefg
  abcdefg
   abcdefg   XOR
----------
1110100110
The first one is easy: since the first encrypted bit is a, it means that (given the first column) a = 1.

So we have:

1bcdefg
 1bcdefg
  1bcdefg
   1bcdefg   XOR
----------
1110100110
Now, looking at the second column (b and 1), we see that: b ⊕ 1 = 1

(note, the ⊕ is the logical symbol for XOR, "exclusive or")

To solve for b, we need to know an important transform. That is, if you have x ⊕ y = z, this is the same as "x ⊕ z = y" or "y ⊕ z = x" or any other ordering.

As such, b = 1 ⊕ 1, or b = 0.

Back to our example:

10cdefg
 10cdefg
  10cdefg
   10cdefg   XOR
----------
1110100110
Next up, the third column (c, 0, 1) means that c ⊕ 0 ⊕ 1 = 1, which is the same as c = 0 ⊕ 1 ⊕ 1, hence c = 0.

Each column will have just one new variable to decypher until the entire original code is reconstructed.

WARNING: Some of the test cases are large, and you don't want to calculate every single XOR for each column. But, if you look at the previous column, you see that it was pretty similar. Can you re-use those previous calculations?

Either way, I recommend that you get something working first for MOST of the test cases and then optimize further when you need to.

Example 1
---------------
Sample Input
6 2
1110001

Sample Output
101111

Explanation
---------------
101111
 101111
-------
1110001
'''
n = input().split()
N = int(n[0])
K = int(n[1])
S = input()
retval = S[0]
check = int(S[0])
for i in range(1, N):
    if i <= K - 1:
        letter = check ^ int(S[i])
        check = check ^ letter
        retval += str(letter)
    else:
        check = check ^ int(retval[i - K])
        letter = check ^ int(S[i])
        check = check ^ letter
        retval += str(letter)

print(retval)