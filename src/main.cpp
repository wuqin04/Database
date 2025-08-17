#include "sys/socket.h"
#include "netinet/in.h"
#include "netinet/ip.h"

int main() {
    // file descriptor
    int fd = socket(AF_INET, SOCK_STREAM, 0);

    int val = 1;
    setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &val, sizeof(val));
}