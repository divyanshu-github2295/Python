#include <math.h>
#include <cs50.h>
#include <ctype.h>
#include <string.h>
#include <stdio.h>

int count_letter(string);
int count_words(string);
int count_sentence(string);
int compute_index(int, int, int);
void compute_grade(int);

int main(void)
{
    // Asking Text from user
    string text = get_string("Text:");

    // Calling count_letter function for counting letters
    int letter = count_letter(text);

    // Calling count_words function for counting words
    int words = count_words(text);

    // Calling count_sentence function for counting sentence
    int sentence = count_sentence(text);

    // Calling compute_index function for calculating index
    int index = compute_index(letter, words, sentence);

    // Calling compute_grade function and printing Grade 
    compute_grade(index);
}

// Counting letters
int count_letter(string t)
{
    int l = 0;
    int n = strlen(t);
    for (int i = 0; i < n; i++)
    {
        if (isalpha(t[i]))
        {
            l ++;
        }
    }
    return l;
}

// Counting words
int count_words(string t)
{
    int w = 0;
    int n = strlen(t);
    for (int i = 0; i < n; i++)
    {
        if (isspace(t[i]))
        {
            w ++;
        }
    }
    w ++;
    return w;
}

// Counting sentences
int count_sentence(string t)
{
    int s = 0;
    int n = strlen(t);
    for (int i = 0; i < n; i++)
    {
        if (t[i] == '.' || t[i] == '!' || t[i] == '?')
        {
            s ++;
        }
    }
    return s;
}

// Computing Index
int compute_index(int l, int w, int s)
{
    // index using coleman-liau
    // index = 0.0588 * L - 0.296 * S - 15.8

    float L = 0, S = 0, inx = 0;
    printf("s:%i\n", s);
    L = ((float)l / (float)w) * 100;
    S = ((float)s / (float)w) * 100;
    printf("L:%f\n", L);
    printf("S:%f\n", S);
    inx = 0.0588 * L - 0.296 * S - 15.8;
    printf("Index:%f\n", inx);
    int r = 0;
    r = round(inx);

    return r;
}

// Determining Grade according to index
void compute_grade(int inx)
{
    if (inx >= 1 && inx <= 15)
    {
        printf("Grade %i\n", inx);
    }
    else if (inx < 1)
    {
        printf("Before Grade 1\n");
    }
    else
    {
        printf("Grade 16+\n");
    }
}