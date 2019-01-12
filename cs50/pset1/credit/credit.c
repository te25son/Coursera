#include <cs50.h>
#include <stdio.h>

int main(void)
{
    // promt user for card number
    // set number to a variable
    long long cc_num = get_long_long("Enter Card Number: "), cc_copy = cc_num;

    int num, sum = 0, start_num, counter = 0;

    // use counter to get length of card number
    while(cc_copy > 0)
    {
        cc_copy /= 10;
        counter += 1;
    }

    // iterate through nums from last to first, adding them to sum
    // multiply every other num by two, add the mod 10 of that num to sum
    // then divide num by 10 to check if num is more than one digit
    // add mod 10 of this num to sum (if not two digits, remainder of this operation will be 0)
    for(int i = 0; i < counter; i++)
    {
        // get first two digits and store for later check
        if(cc_num <= 100 && cc_num >= 10)
        {
            start_num = cc_num;
        }
        if(i % 2 == 0)
        {
            num = cc_num % 10;
            sum += num;
        }
        else
        {
            num = (cc_num % 10) * 2;
            sum += num % 10;
            num /= 10;
            sum += num % 10;
        }
        cc_num /= 10;
    }

    // check if card is legit
    // else display INVALID
    if(sum % 10 == 0)
    {
        // check American Express
        if((start_num == 34 || start_num == 37) && counter == 15)
        {
            printf("AMEX\n");
        }
        // check MasterCard
        else if((start_num == 51 || start_num == 52 || start_num == 53 || start_num == 54 || start_num == 55) && counter == 16)
        {
            printf("MASTERCARD\n");
        }
        // check Visa
        else if((start_num / 10) % 10 == 4 && counter >= 13 && counter <= 16)
        {
            printf("VISA\n");
        }
        // else a tricky card, but not tricky enough ;)
        else
        {
            printf("INVALID\n");
        }
    }
    else
    {
        printf("INVALID\n");
    }
}

