import os
os.system("nmap -sV --script=http-sql-injection  testphp.vulnweb.com  -oX kerimeraslan.xml")