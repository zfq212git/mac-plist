# mac-plist
build a plist for managing to run a task at a designated time

# 相关命令
1.  launchctl load xxxx.plist    (在命令窗口中输入，把这个任务放到苹果的定时任务队列中去)
2.  launchctl unload xxxx.plist
3.  launchctl start xxxx.plist   （可以用来测试任务。这个是立即执行，不管设定的时间到了没有）
4.  launchctl stop xxxx.plist
5.  launchctl list   （列出现在在定时队列里的所有任务)


深入的再说一下，其实，/Library/LaunchAgents这样的目录在mac下一般有三个，我们上面说的是当前用户的目录下的，还有两个一个在/Library/LaunchAgents另一个在/System/Library/LaunchAgents/ 如果是不管哪一个用户都要定时执行的话，就要放在 
/Library/LaunchAgents这个下面 


#注意
各个代码里有绝对路径，如果路径变了，需要改下代码。