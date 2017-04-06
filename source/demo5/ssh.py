#!/usr/bin/env python
# coding=utf-8
# Author: shangyidong
# Mail: shangyidong@meituan.com

import pexpect

passwd = "445013"
cmd = "java -version"
ret = -1
ssh = pexpect.spawn('ssh shangyidong@%s' % ("jumper.dper.com"))
verifyCode = input("Please input your verifyCode:\n")
passwd = passwd + str(verifyCode)
ssh.sendline(passwd)
ssh.expect('$')
r = ssh.read()
print r