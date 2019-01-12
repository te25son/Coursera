// Helper functions for music

#include <cs50.h>
#include <string.h>
#include <math.h>

#include "helpers.h"

// Converts a fraction formatted as X/Y to eighths
int duration(string fraction)
{
    char nom = fraction[0], den = fraction[2];

    if (nom == '1')
    {
        if (den == '8')
        {
            return 1;
        }
        else if (den == '4')
        {
            return 2;
        }
        else if (den == '2')
        {
            return 4;
        }
        else if (den == '1')
        {
            return 8;
        }
        else
        {
            return 0;
        }
    }
    else if (nom == '3' && den == '8')
    {
        return 3;
    }
    else
    {
        return 0;
    }
    return 0;
}

// Calculates frequency (in Hz) of a note
int frequency(string note)
{
    // get note's octave
    int octave = note[strlen(note) - 1];

    // convert octave from ascii to int
    octave -= 48;

    // get note's key
    char key = note[0];

    // set default frequency
    double freq = 0.0;

    // adjust frequency according to note's key
    switch(key)
    {
        case 'C':
            freq = 440.0 / pow(2.0, (9.0 / 12.0));
            break;

        case 'D':
            freq = 440.0 / pow(2.0, (7.0/12.0));
            break;

        case 'E':
            freq = 440.0 / pow(2.0, (5.0/12.0));
            break;

        case 'F':
            freq = 440.0 / pow(2.0, (4.0/12.0));
            break;

        case 'G':
            freq = 440.0 / pow(2.0, (2.0/12.0));
            break;

        case 'A':
            freq = 440.0;
            break;

        case 'B':
            freq = 440.0 * pow(2.0, (2.0/12.0));
            break;

        default:
            return 0;
    }

    // adjust frequency according to octave
    if (octave > 4)
    {
        for (int i = 0; i < (octave - 4); i++)
        {
            freq *= 2.0;
        }
    }
    else if (octave < 4)
    {
        for (int i = 0; i < (4 - octave); i++)
        {
            freq /= 2.0;
        }
    }

    // adjust frequency to account for sharps or flats
    if (note[1] == 'b')
    {
        freq /= pow(2.0, (1.0/12.0));
    }
    else if (note[1] == '#')
    {
        freq *= pow(2.0, (1.0/12.0));
    }

    // round the frequency and return the value
    int val = round(freq);
    return val;
}

// Determines whether a string represents a rest
bool is_rest(string s)
{
    if (s[0] == '\0')
    {
        return true;
    }
    else
    {
        return false;
    }
}
