from subprocess import Popen, PIPE
import os
import time
import datetime
import grp
import shutil
import sys
import base64
import pwd

def group_kontrol(grup_adi):
	ok=True
	try:
		grp.getgrnam(grup_adi)
	except KeyError:
		ok=False
	return ok

if not os.path.exists("/opt/drstrange"):
	izin=input("Uygulama kurulmamış. Kurmak ister misiniz? [e/h]:")
	if izin=="e":
		os.mkdir("/opt/drstrange")
		shutil.copy(os.getcwd() + "/" + os.path.basename(sys.argv[0]),"/opt/drstrange/agent.py")
		f=open("/etc/systemd/system/drstrange.service","w")
		f.write("[Unit]\n")
		f.write("Description=Connection log service\n")
		f.write("After=network.target\n")
		f.write("StartLimitIntervalSec=0\n\n")
		f.write("[Service]\n")
		f.write("Type=simple\n")
		f.write("Restart=always\n")
		f.write("RestartSec=1\n")
		f.write("User=root\n")
		f.write("ExecStart=/bin/python3 /opt/drstrange/agent.py\n\n")
		f.write("[Install]\n")
		f.write("WantedBy=multi-user.target")
		f.close()
		Popen("chmod go-wx /opt/drstrange/agent.py",shell=True)
		komutsatiri=base64.b64decode("ZXhwb3J0IFBST01QVF9DT01NQU5EPSdlY2hvIGRhdGU9WyQoZGF0ZSldICQoY2F0IC9ldGMvKi1yZWxlYXNlIHwgZ3JlcCBESVNUUklCX0lEIHwgc2VkIC1yICJzLz0vPVsvZyIpXSB1c3I9WyQod2hvYW1pKV0gY29tbWFuZD1bJChoaXN0b3J5IC13IC9kZXYvc3Rkb3V0IHwgdGFpbCAtbiAxIHwgaGVhZCAtMSldID4+IC92YXIvbG9nL2hpc3RvcnlfJCh3aG9hbWkpLmxvZyc=").decode("utf-8")
		f=open("/etc/bash.bashrc","r+")
		f.write('if [ -z "${PS1}" ]; then\n')
		f.write('return\n')
		f.write('else\n')
		f.write(komutsatiri+"\n")
		f.write('fi\n')
		f.close()
		f=open("/etc/rsyslog.d/50-default.conf","w")
		f.write(base64.b64decode("IyAgRGVmYXVsdCBydWxlcyBmb3IgcnN5c2xvZy4KIwojICAgICAgICAgICAgICAgICAgICAgICBGb3IgbW9yZSBpbmZvcm1hdGlvbiBzZWUgcnN5c2xvZy5jb25mKDUpIGFuZCAvZXRjL3JzeXNsb2cuY29uZgoKIwojIEZpcnN0IHNvbWUgc3RhbmRhcmQgbG9nIGZpbGVzLiAgTG9nIGJ5IGZhY2lsaXR5LgojCgphdXRoLGF1dGhwcml2LiogICAgICAgICAgICAgICAgIC92YXIvbG9nL2F1dGgubG9nCiouKjthdXRoLGF1dGhwcml2Lm5vbmUgICAgICAgICAgLS92YXIvbG9nL3N5c2xvZwpjcm9uLiogICAgICAgICAgICAgICAgICAgICAgICAgIC92YXIvbG9nL2Nyb24ubG9nCmRhZW1vbi4qICAgICAgICAgICAgICAgICAgICAgICAgLS92YXIvbG9nL2RhZW1vbi5sb2cKa2Vybi4qICAgICAgICAgICAgICAgICAgICAgICAgICAtL3Zhci9sb2cva2Vybi5sb2cKbHByLiogICAgICAgICAgICAgICAgICAgICAgICAgICAtL3Zhci9sb2cvbHByLmxvZwptYWlsLiogICAgICAgICAgICAgICAgICAgICAgICAgIC0vdmFyL2xvZy9tYWlsLmxvZwp1c2VyLiogICAgICAgICAgICAgICAgICAgICAgICAgIC0vdmFyL2xvZy9kcGtnLmxvZwojCiMgTG9nZ2luZyBmb3IgdGhlIG1haWwgc3lzdGVtLiAgU3BsaXQgaXQgdXAgc28gdGhhdAojIGl0IGlzIGVhc3kgdG8gd3JpdGUgc2NyaXB0cyB0byBwYXJzZSB0aGVzZSBmaWxlcy4KIwptYWlsLmluZm8gICAgICAgICAgICAgICAgICAgICAgIC0vdmFyL2xvZy9tYWlsLmluZm8KbWFpbC53YXJuICAgICAgICAgICAgICAgICAgICAgICAtL3Zhci9sb2cvbWFpbC53YXJuCm1haWwuZXJyICAgICAgICAgICAgICAgICAgICAgICAgL3Zhci9sb2cvbWFpbC5lcnIKCiMKIyBTb21lICJjYXRjaC1hbGwiIGxvZyBmaWxlcy4KIwojKi49ZGVidWc7XAojICAgICAgIGF1dGgsYXV0aHByaXYubm9uZTtcCiMgICAgICAgbmV3cy5ub25lO21haWwubm9uZSAgICAgLS92YXIvbG9nL2RlYnVnCiMqLj1pbmZvOyouPW5vdGljZTsqLj13YXJuO1wKIyAgICAgICBhdXRoLGF1dGhwcml2Lm5vbmU7XAojICAgICAgIGNyb24sZGFlbW9uLm5vbmU7XAojICAgICAgIG1haWwsbmV3cy5ub25lICAgICAgICAgIC0vdmFyL2xvZy9tZXNzYWdlcwoKIwojIEVtZXJnZW5jaWVzIGFyZSBzZW50IHRvIGV2ZXJ5Ym9keSBsb2dnZWQgaW4uCiMKKi5lbWVyZyAgICAgICAgICAgICAgICAgICAgICAgICA6b211c3Jtc2c6KgoKIwojIEkgbGlrZSB0byBoYXZlIG1lc3NhZ2VzIGRpc3BsYXllZCBvbiB0aGUgY29uc29sZSwgYnV0IG9ubHkgb24gYSB2aXJ0dWFsCiMgY29uc29sZSBJIHVzdWFsbHkgbGVhdmUgaWRsZS4KIwojZGFlbW9uLG1haWwuKjtcCiMgICAgICAgbmV3cy49Y3JpdDtuZXdzLj1lcnI7bmV3cy49bm90aWNlO1wKIyAgICAgICAqLj1kZWJ1ZzsqLj1pbmZvO1wKIyAgICAgICAqLj1ub3RpY2U7Ki49d2FybiAgICAgICAvZGV2L3R0eTg=").decode("utf-8"))
		f.close()
		f=open("/etc/rsyslog.d/101-root.conf","w")
		f.write(base64.b64decode("JE1vZExvYWQgaW1maWxlCiRJbnB1dEZpbGVOYW1lIC92YXIvbG9nL2hpc3Rvcnlfcm9vdC5sb2cKJElucHV0RmlsZVRhZyByb290dXNlcmNvbW1hbmQKJElucHV0RmlsZVN0YXRlRmlsZSByb290dXNlcmNvbW1hbmQtc3RhdGUKJElucHV0RmlsZVNldmVyaXR5IGluZm8KJElucHV0RmlsZUZhY2lsaXR5IGxvY2FsMwokSW5wdXRSdW5GaWxlTW9uaXRvcg==").decode("utf-8"))
		f.close()
		f=open("/etc/rsyslog.d/102-apache.conf","w")
		f.write(base64.b64decode("JElucHV0RmlsZU5hbWUgL3Zhci9sb2cvYXBhY2hlMi9hY2Nlc3MubG9nCiRJbnB1dEZpbGVUYWcgYXBhY2hlLWxvZwokSW5wdXRGaWxlU3RhdGVGaWxlIGFwYWNoZS1zdGF0ZQokSW5wdXRGaWxlU2V2ZXJpdHkgaW5mbwokSW5wdXRGaWxlRmFjaWxpdHkgbG9jYWw0CiRJbnB1dFJ1bkZpbGVNb25pdG9y").decode("utf-8"))
		f.close()
		f=open("/etc/rsyslog.d/103-connectionest.conf","w")
		f.write(base64.b64decode("JElucHV0RmlsZU5hbWUgL3Zhci9sb2cvY29ubmVjdGlvbl9lc3RhYmxpc2hlZC5sb2cKJElucHV0RmlsZVRhZyBjb25uZWN0aW9uLWxvZwokSW5wdXRGaWxlU3RhdGVGaWxlIGNvbm5lY3Rpb24tc3RhdGUKJElucHV0RmlsZVNldmVyaXR5IGluZm8KJElucHV0RmlsZUZhY2lsaXR5IGxvY2FsNQokSW5wdXRSdW5GaWxlTW9uaXRvcg==").decode("utf-8"))
		f.close()
		for p in pwd.getpwall():
			if p[0]!="root":
				f=open("/etc/rsyslog.d/"+p[0]+".conf","w")
				f.write("$InputFileName /var/log/history_"+p[0]+".log\n")
				f.write("$InputFileTag " + p[0]+"usercommand\n")
				f.write("$InputFileStateFile "+p[0]+"usercommand-state\n")
				f.write("$InputFileSeverity info\n$InputFileSeverity info\n$InputRunFileMonitor")
				f.close()
			if not group_kontrol(p[0]+"syslog"):
				Popen("groupadd "+p[0]+"syslog && usermod -a -G "+p[0]+"syslog syslog && touch /var/log/history_"+p[0]+".log && chown "+p[0]+":"+p[0]+"syslog /var/log/history_"+p[0]+".log && chmod og-rwx /var/log/history_"+p[0]+".log && chmod g+r /var/log/history_"+p[0]+".log",shell=True)
		#Popen("echo 'module(load="imudp")' >> /etc/rsyslog.conf && echo 'input(type="imudp" port="514")' >> /etc/rsyslog.conf && echo '*.* @192.168.11.17:514' >> /etc/rsyslog.conf && systemctl restart --now rsyslog && systemctl enable rsyslog",shell=True)
		izin=input("Uygualam kurulumu tamamlandı ve servis olarak eklendi. Şimdi çalıştırılsın mı? [e/h]:")
		if izin=="e":
			Popen("systemctl enable drstrange.service && systemctl start drstrange.service",shell=True)
			print("Kurulum tamamlandı.\nÇıkılıyor...")
			sys.exit()






if not os.path.exists("/var/log/connection_established.log"):
	Popen("touch /var/log/connection_established.log && chown root:rootsyslog /var/log/connection_established.log && chmod go-rwx /var/log/connection_established.log && chmod g+r /var/log/connection_established.log",shell=True)

while True:
	pt=Popen("lsof -t -i -sTCP:ESTABLISHED | xargs ps --no-headers -o'lstart' -p",shell=True,stdout=PIPE,stderr=PIPE)
	pt.wait()
	p=Popen("lsof -i -sTCP:ESTABLISHED | grep -v PID",shell=True,stdout=PIPE,stderr=PIPE) #Connection ESTABLISHED uygulamaların başlangıç zamanını ve uygulamaları al
	p.wait()
	stdouttar,stderrtar=pt.communicate()
	stdoutp,stderrp=p.communicate()
	ciktitarih=str(stdouttar).replace("b'","").split("\\n")
	ciktisurec=str(stdoutp).replace("b'","").split("\\n")
	for i in range(len(ciktitarih)):
		(mode, ino, dev, nlink, uid, gid, size, atime, mtime, ctime)=os.stat("/var/log/connection_established.log")
		if ciktisurec[i].find("ESTABLISHED") != -1:
			if datetime.datetime.strptime(ciktitarih[i], "%a %b %d %H:%M:%S %Y").timestamp()>mtime:
				log="surec_ip_tip=[" + ciktisurec[i] +"] zaman=["+ciktitarih[i]+"]"
				Popen("echo \'" + log + "\' >> /var/log/connection_established.log",shell=True)
	time.sleep(10)
