#include "sys/socket.h"
#include "netinet/in.h"
#include "netinet/ip.h"
#include <unistd.h>
#include <stdio.h>
#include <string.h>

static void do_something(int connfd);

int main() {
    // file descriptor
    int fd = socket(AF_INET, SOCK_STREAM, 0);

    // set socket options
    int val = 1;
    setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, &val, sizeof(val));

    // bind to an address
    struct sockaddr_in addr = {};
    addr.sin_family = AF_INET;
    addr.sin_port = htons(1234);        // port
    addr.sin_addr.s_addr = htonl(0);    // wildcard IP 0.0.0.0
    int rv = bind(fd, (const sockaddr*)&addr, sizeof(addr));
    
    // listen
    rv = listen(fd, SOMAXCONN);

    // Accept connections
    while (true) {
        // accept 
        struct sockaddr_in client_addr = {};
        socklen_t addrlen = sizeof(client_addr);
        int connfd = accept(fd, (struct sockaddr*)&client_addr, &addrlen);

        if (connfd < 0) 
            continue;   // error

        do_something(connfd);
    }
}

static void do_something(int connfd) {
    char rbuf[64] = {};
    ssize_t n = read(connfd, rbuf, sizeof(rbuf) -1);
    
    if (n < 0) {
        return;     // error
    }

    printf("client says: %s\n", rbuf);

    char wbuf[] = "world";
    write(connfd, wbuf, strlen(wbuf));

}