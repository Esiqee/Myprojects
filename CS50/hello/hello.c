#include <stdio.h>
#include <cs50.h>

int main(void)
{
    //input the name and then print it as hello: name
    string name = get_string("What is your name? ");
    printf("hello, %s\n", name);
}


