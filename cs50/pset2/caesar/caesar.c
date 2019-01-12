#include <stdio.h>
#include <cs50.h>
#include <string.h>
#include <ctype.h>

int getAlphaCrypt(char let, int key_item);

int main(int argc, string argv[])
{
    if (argc == 2)
    {
        // get the key from argv and convert to integer
        int key = atoi(argv[1]);

        // get the plain text and define ciphered text
        string pt = get_string("plaintext: "), ct = pt;

        // iterate over all characters in message
        for (int i = 0, n = strlen(pt); i < n; i++)
        {
            // check if char is alphabetic
            if (isalpha(pt[i]))
            {
                ct[i] = getAlphaCrypt(pt[i], key);
            }
            else
            {
                ct[i] = pt[i];
            }
        }
        printf("ciphertext: %s\n", ct);
        return 0;
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

