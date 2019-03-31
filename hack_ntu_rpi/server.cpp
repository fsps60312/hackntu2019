#include<bits/stdc++.h>
#include"network.h"
using namespace std;
int main()
{
	const int server_fd=GetServerSocketFd(60312);
	clog<<"server_fd="<<server_fd<<endl;
	while(true)
	{
		const int client_fd=Accept(server_fd);
		if(client_fd>0)
		{
			clog<<"accept new client: fd="<<client_fd<<endl;
			clog<<"waiting..."<<endl;
			while(!IsAvailable(client_fd));
			cout<<ReadLine(client_fd)<<endl;
			close(client_fd);
		}
	}
}
