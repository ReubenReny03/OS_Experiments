#include <stdio.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>

int main() {
        int input_fd, input_fd_2, output_fd, bytes_read, bytes_written;
        char buffer[1024];
        input_fd = open("input.txt", O_RDONLY);
        input_fd_2 = open("input.txt", O_RDONLY);
        output_fd = open("output.txt", O_WRONLY | O_APPEND );
        while (( bytes_read = read(input_fd, buffer, sizeof(buffer) ) ) > 0) {
                bytes_written = write(output_fd, buffer, bytes_read);
        }
        while (( bytes_read = read(input_fd_2, buffer, sizeof(buffer) ) ) > 0) {
                bytes_written = write(output_fd, buffer, bytes_read);
        }
}