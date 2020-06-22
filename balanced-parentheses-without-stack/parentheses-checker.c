/**
 * Code to check if parentheses are balanced in the given expression.
 *
 * {}[] - balanced
 * {{}} - balanced
 * {{()[]}}{} - balanced
 * [{} - not balanced
 * []{ - not balanced
 * {{(())(}} - not balanced
 *
 * assumption - input contains only parentheses to check for balanced expression
 *              and does not contain whitespaces or any other characters.
 */

#include <stdio.h>
#include <stdbool.h>
#include <string.h>

// check if the character is open parentheses.
bool is_open_parentheses(char ch) {
    return (ch == '{' || ch == '(' || ch == '[');
}

// check if the character is closed parentheses.
bool is_close_parentheses(char ch) {
    return (ch == '}' || ch == ')' || ch == ']');
}

// get matching open parentheses for the given closed parentheses.
char get_open_parentheses(char ch) {
    switch (ch) {
        case '}':
            return '{';
        case ')':
            return '(';
        case ']':
            return '[';
    }
}

// check if given expression starting is balanced or not.
bool check(char* exp, int len, int* index) {
    int i = 1;
    int j = 0;
    
    for( ;i < len; i++) {
        if (is_close_parentheses(exp[i])) {
            // check for parentheses match at postion i and j.
            if (exp[j] != get_open_parentheses(exp[i])) {
                return false;
            } else if (--j == -1 && *index != 0) {
                // decrement j index for every match.
                // when j reaches -1, all parentheses starting from *index
                // has been evaluated, break the loop.
                break;
            }
        } else if (is_open_parentheses(exp[i])) {
            // check for sub-expression in the given expression.
            if (j == (i - 1)) {
                // when j position is previous postion of i, 
                // it's not a sub-expression.
                j++;
            } else if (!check(exp + i, len - i, &i)) {  // sub expression, use recursion.
                // when sub-expression is not balanced return failure.
                return false;
            }
        }
    }

    // when j index position doesn't reach -1 finally then the expression
    // is not balanced.
    if (j != -1) {
        return false;
    }

    // update the index.
    (*index) = (*index + i);
    return true;
}

// program entry point.
int main(int argc, char* argv[]) {
    char exp[32] = {};

    while(true) {
        // get expression.
        printf("Enter expression - ");
        scanf("%s", exp);

        // check the given expression.
        int index = 0;
        bool ret = check(exp, strlen(exp), &index);
        printf("%s : %s\n\n", exp, ret ? "balanced" : "not balanced");
    }

    return 0;
}

