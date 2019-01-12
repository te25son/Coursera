#include <stdio.h>
#include <string.h>
#include <ctype.h>
#include <cs50.h>

int getAlphaCrypt(char let, int key_item);

int main(int argc, string argv[])
{
    // check if two arguments are passed
    if (argc == 2)
    {
        // check that all chars in second argument are alphabetic
        for (int c = 0; c < strlen(argv[1]); c++)
        {
            if(isalpha(argv[1][c]))
            {
                continue;
            }
            else
            {
                printf("ERROR\n");
                return 1;
            }
        }
        // get the given key (key), plaintext (pt), and make a copy of plaintext to write over , aka cipher text (ct)
        string key = argv[1], pt = get_string("plaintext: "), ct = pt;

        // get length of key and use as mod (mod), and make tracker (t) keep track of alphabetical chars
        int mod = strlen(key), t = 0;

        // iterate over all chars in pt
        for (int i = 0, key_num; i < strlen(pt); i++)
        {
            // check if key char is upper or lower
            if (isupper(key[t]))
            {
                key_num = key[t] - 65;
            }
            else
            {
                key_num = key[t] - 97;
            }

            // check if char is alphabetic
            if (isalpha(pt[i]))
            {
                // check if char is upper or lower
                if (isupper(pt[i]))
                {
                    // assign ascii value (num) to cipher text (ct)
                    ct[i] = getAlphaCrypt(pt[i], key_num);

                    // shift tracker (t)
                    t = (t + 1) % mod;
                }
                else
                {
                    // assign ascii value (num) to cipher text (ct)
                    ct[i] = getAlphaCrypt(pt[i], key_num);

                    // shift tracker (t)
                    t = (t + 1) % mod;
                }
            }
            else
            {
                ct[i] = pt[i];
            }
        }
        // print out cipher text (ct)
        printf("ciphertext: %s\n", ct);
    }
    else
    {
        printf("ERROR\n");
        return 1;
    }
}

int getAlphaCrypt(char let, int key_item)
{
    if (isupper(let))
    {
        return (((let + key_item) - 65) % 26) + 65;
    }
    else
    {
        return (((let + key_item) - 97) % 26) + 97;
    }
}