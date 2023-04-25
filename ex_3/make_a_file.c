#include <fcntl.h>
#include <unistd.h>

int main() {
        int fd;
        fd = open("newfile.txt",O_CREAT | O_WRONLY, 0666);
        close(fd);
        return 0;
}