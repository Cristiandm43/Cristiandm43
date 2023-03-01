#include <sys/types.h>
#include <unistd.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/wait.h>

int main (int argc, char *argv[]) {

    int num;
    pid_t pid;

    for (num = 0; num < 3; num++) {
        pid = fork();
        printf ("Soy el proceso PID%d y mi padre tiene $d de PID\n"
                get pid(), getppid());
        if (pid!=0)
            break;
        srndom(getpid());
        sleep (random()%3);
    }
    if (pid!=0)
    printf ("Fin de proceso de PID%d\n", wait (NULL));
    

return 0;
}