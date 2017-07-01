#include <sys/types.h>
#include <sys/socket.h>
#include <netinet/in.h>
#include <unistd.h>
#include <arpa/inet.h>
#include <netdb.h>
#include <unistd.h>
#include <signal.h>
#include <stdio.h>
#include <string.h>
#include <fcntl.h>
#include <errno.h>
#include <sys/time.h>
#include <stdlib.h>
#include <memory.h>
#include <ifaddrs.h>
#include <net/if.h>
#include <stdarg.h>
#include <stdbool.h>

struct client
{
  struct client* next;
  char name[1024];
  int sd;
};

struct client* head;

void add(int id, char* n)
{
  struct client* temp;
  temp = (struct client*)malloc(sizeof(struct client));
  strcpy(temp -> name, n);
  temp -> sd = id;
  temp -> next = head;
    head = temp;
}

bool findsd(int id)
{
  struct client* cur = head;
  if(head == NULL)
 {
    return NULL;
  }

  while(cur -> sd != id)
  {
    if(cur -> next == NULL)
    {
       return false;
    }
    else
    {
       cur = cur -> next;
    }
  }
  return true;
}

struct client* find(char* n)
{
  struct client* cur = head;
  if(head == NULL)
  {
    return NULL;
  }
  while(strcmp(cur -> name, n) != 0)
  {
    if(cur -> next == NULL)
    {
       return NULL;
    }
    else
    {
       cur = cur -> next;
    }
  }
  return cur;
}

void printList()
{

  struct client* ptr = head;
  while(ptr != NULL)
  {
    printf("[(%s, %d)]\n", ptr -> name, ptr -> sd);
    ptr = ptr -> next;
  }

}
void *connection_handler(void *socket_desc)
{
    int sock = *(int*)socket_desc;
    struct client* c;
    int num, i = 0;
    char r[1024], n[100];

    num = recv(sock, r, sizeof(r), 0);
    if(num <= 0)
    {
    printf("Error\n");
    //break;
    }
    else if (num == 0)
     {
        printf("Connection closed\n");
     }
    r[num] = '\0';
    if(!findsd(sock))
    {
      add(sock, r);
      printList();
    }
    else{
     while(r[i] != ' ')
     {
       n[i] = r[i];
       i++;
     }
     n[i] = '\0';
    }
     if((c = find(n)) != NULL)
     {
       send(c -> sd, r, sizeof(r), 0);
     }

}

int main()
{
  int sd, csd;
  int* new_sock;
  char buf[1024];
  char b[1024];
  int* d, *c;
  int num;
  struct sockaddr_in sAddr;
  struct sockaddr_storage sStorage;
  socklen_t addr_size;

  sd = socket(PF_INET, SOCK_STREAM, 0);

  sAddr.sin_family = AF_INET;
  sAddr.sin_port = htons(8888);
  sAddr.sin_addr.s_addr = inet_addr("127.0.0.1");
  memset(sAddr.sin_zero, '\0', sizeof sAddr.sin_zero);

  bind(sd, (struct sockaddr *) &sAddr, sizeof(sAddr));

  if( listen(sd, 5) == 0 )
    printf("Listening\n");
  else
    printf("Error\n");

  addr_size = sizeof(struct sockaddr_in);
  int j, i = 0;
  new_sock = malloc(5);

    while( csd = accept(sd, (struct sockaddr *) &sStorage, &addr_size))
    {
     puts("Connection accepted");

     pthread_t sniffer_thread;
     new_sock[i] = csd;

        if( pthread_create( &sniffer_thread , 0 ,connection_handler , (void*) (new_sock + i)) < 0)
        {
            perror("could not create thread");
            return 1;
        }

        puts("Handler assigned");
    i++;

    }

}
