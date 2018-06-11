#include<stdio.h>
#include<string.h>
#include <netdb.h> 
#include <sys/types.h> 
#include <netinet/in.h> 
#include <sys/socket.h> 
#include <unistd.h>
#include <stdlib.h> 
#include <sys/ptrace.h>

#define PORT 8888

void check(void) __attribute__((constructor));

void check(void)
{
    if (ptrace(PTRACE_TRACEME, 0,0,0) == -1)
    {
        _exit(-1);
    }
}

const char * onefunc()
{
  int a = 3;
  int b = 9;
  int c = 87;
  if ( a > 4 ) {
    return "LQA";
  } else if ( b < 8) {
    return "PLK";
  } else if ( c < 84) {
    return "QKI";
  } else { 
    return "_L3"; 
  }
}

const char * twofunc()
{
    int sockfd, numbytes;
    char *buf = malloc(3);
    struct hostent *he;
    struct sockaddr_in their_addr; 

    he = gethostbyname("127.0.0.1");

    sockfd = socket(AF_INET, SOCK_STREAM, 0);

    their_addr.sin_family = AF_INET;
    their_addr.sin_port = htons(PORT);
    their_addr.sin_addr = *((struct in_addr *)he->h_addr);
    bzero(&(their_addr.sin_zero), 8);

    connect(sockfd, (struct sockaddr *)&their_addr, sizeof(struct sockaddr));

    send(sockfd, "?\n", 2, 0);

 
    numbytes=recv(sockfd, buf, 3, 0);
    buf[numbytes] = '\0';

    close(sockfd);

    return buf;
}

const char * threefunc()
{
    return "PRATEZ";
}


int main(void)
{
  int i;
  char one[3];
  char two[3];
  char three[6];

  strcpy(one, onefunc());
  strcpy(two, twofunc());
  strcpy(three, threefunc());
  char alpha[13];
  
  snprintf(alpha, sizeof(alpha), "%s%s%s", one, two, three);

  //char key[32] = { 3,2,0,4,2,2,5,0,6,7,10,9,11,2,1,11,0,7,10,6,10,8,9,0,6,7,10,9,11,2,1,11};
  char key[32] = { 0,0,0,0,0,0,0,0,0,0,0 ,0, 0,0,0, 0,0,0, 0,0, 0,0,0,0,0,0, 0,0, 0,0,0, 0};
  for(i = 0; i < 32; i++)
  {
    printf("%c", alpha[key[i]]); 
  }
  printf("\n");
}
