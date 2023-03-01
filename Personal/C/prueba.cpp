#include <stdlib.h>
#include <sys/types.h>
#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <errno.h>
int main(int argc, char **argv)
    {
    pid_t my_pid;
    my_pid = fork();
    if (my_pid < 0)
        {
        printf("The fork didn't work! Terminate\n");
        exit(0);
        }
    if (my_pid != 0)
        {
        // Parent block
        printf("The parent will now wait\n");
        wait(NULL);
        printf("Done!\n");
        }
    else
        {
        // Child block
        int resp;
        resp = execvp(*(argv+1), argv+1);
        printf("There was an error. Response code: %d\n Errno: %s\n", resp, stderror(errno));
        }
    }