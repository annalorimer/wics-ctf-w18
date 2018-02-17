You're the sysadmin/secops/general go-to person for your startups two in-house servers. You've been pinged because
one of your coworkers has discovered that one of your machines is being used to serve malicious traffic off of port
28400. That is capital B Bad. You run netstat to find out what's up. Based on this output, what command would you use
to kill the program immediately? (Note: you are already the root user, so do not prepend any commands with `sudo`)

```
root@company:~$ netstat -plnt
Active Internet connections (only servers)
Proto Recv-Q Send-Q Local Address           Foreign Address         State       PID/Program name
tcp        0      0 0.0.0.0:111             0.0.0.0:*               LISTEN      735/rpcbind
tcp        0      0 0.0.0.0:57556           0.0.0.0:*               LISTEN      1080/rpc.mountd
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      763/sshd
tcp        0      0 0.0.0.0:36505           0.0.0.0:*               LISTEN      -
tcp        0      0 0.0.0.0:443             0.0.0.0:*               LISTEN      1080/our_fun_app
tcp        0      0 0.0.0.0:45985           0.0.0.0:*               LISTEN      1080/rpc.mountd
tcp6       0      0 0.0.0.0:28400           0.0.0.0:*               LISTEN      20049/evil_mcbad
tcp6       0      0 :::18000                :::*                    LISTEN      13897/weechat
```
