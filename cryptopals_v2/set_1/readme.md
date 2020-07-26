# Walkthrough (Thinking process) - Set 1

## Challenge 2

Here's what I am trying at this moment. I have to find the XOR of two hex value. I checked with an online tool (because my answers are kept coming wrong!). I converted the hex to decimal and then tried to find the XOR. but the result does not match.

So, now I am going to converted the hex to a string. and then convert the string to decimal value by their ascii value and finally XOR them. Let's see if it works. IDK

I have calculated the previous method. That one did not pan out either. I think I am screwing up the XOR calculation somehow! I checked the result with an online tool, the hex answer does not match but the base10 value does not match with my base10 value either. What in the world!

So, I was extremely smart and tried to do lots of different shits! -_-
Ultimately the solution was and the key tagline is **Always operate on raw bytes. Hex and base64 is only for prettyfying**. I converted both hex into bytes using codecs, ran a simple loop to calculate the XOR between them and convert the result byte into hex.