import socket
import sys

print ' '
print ' '
print ' '
print ' '
print '         *****************************        '
print '         ************** **************        '
print '         *************   *************        '
print '         ************     ************        '
print '         ***********       ***********        '
print '         **********    *    **********        '
print '         *********           *********        '
print '         ********             ********        '
print '         *****************************        '
print '         ********** AzAzEl03 *********        '
print '         *****************************        '
print '         *****************************        '
print ' '
print ' '
print ' '
print '* Tool for find user on server smtp, entering the ip of smtp,'
print '  command of check and name user'
print ' '
print ' '
print ' '
print ' '
try:
	target = raw_input('* IP of SMTP check: ')
	command = 'vrfy'
	print ' '
	user = raw_input('* Name User: ')
	sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	sock.connect((target,25))
	banner = sock.recv(1024)
	print ' '
	print ' '
	print ' '
	print 'Check:'
	print banner
	if '220' in banner:
		sock.send(command+' '+user)
		result = sock.recv(1024)
		if '252' in str(result) or '250' in str(result):
			print 'Valid User: ' + user
			print ' '
			print ' '
		else:
			print 'User invalid'
			print ' '
			print ' '
	else:
		print 'Error connect'
		print ' '
		print ' '			
	sock.close()
except socket.timeout:
	print 'Timeout for: ' + target
	print ' '
	print ' '
except socket.error:
	print 'Error connect for: ' + target
	print ' '
	print ' '
