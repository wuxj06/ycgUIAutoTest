__author__ = 'wuxj06'
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.header import Header
from Common.config import log_dir,report_dir,img_dir
import os

log_dirs=os.listdir(log_dir)
log_attach=os.path.join(log_dir,log_dirs[-1])
report_dirs=os.listdir(report_dir)
report_attach=os.path.join(report_dir,report_dirs[-1])
info = []
file = open(log_attach,'r',encoding='utf-8').readlines()
for item in file:
    if item.find('有问题') != -1 or item.find('异常原因') != -1:
        info.append(item)
mail_server='smtp.exmail.qq.com'
mail_port='465'
from_addr='liuc22@mingyuanyun.com'
passwd="i7FyYdCzpTnra3wk"
#to_addr=['liuc22@mingyuanyun.com','dengyw@mingyuanyun.com','chenhy03@mingyuanyun.com','liaobw@mingyuanyun.com','wenwb@mingyuanyun.com','zhengw16@mingyuanyun.com','panpy01@mingyuanyun.com','hulp@mingyuanyun.com','luoxj02@mingyuanyun.com']
to_addr = ['liuc22@mingyuanyun.com','2285892030@qq.com']
msg=MIMEMultipart('mixed')
msg['subject']=Header('UI自动化测试结果','utf-8')
msg['from']="%s<%s>"%(Header('管理员','utf-8'),from_addr)
msg['to']=Header(",".join(to_addr))
if len(info)>0:
    content="""
    <p>云采购UI自动化测试执行完毕</p>
    <p>请下载附件查看测试结果</p>
    <p>本次运行结果为:不通过</p>
    <p>失败原因：%s</p>
    <p>i am very glasses for you</p>
    """%info
    text=MIMEText(content,'plain','utf-8')
    msg.attach(text)
    log_file=open(log_attach,'rb').read()
    txt=MIMEText(log_file,"base64",'utf-8')
    txt["Content-Type"]='application/octet-stream'
    txt.add_header('Content-Disposition','attachment',filename='log.txt')
    msg.attach(txt)
    report_file=open(report_attach,'rb').read()
    report=MIMEText(report_file,"html",'utf-8')
    report["Content-Type"]='application/octet-stream'
    report.add_header('Content-Disposition','attachment',filename='report.html')
    msg.attach(report)
else:
    content="""
    <p>云采购UI自动化测试执行完毕</p>
    <p>请下载附件查看测试结果</p>
    <p>本次运行结果为:通过</p>
    <p>i am very glasses for you</p>
    """
    text=MIMEText(content,'plain','utf-8')
    msg.attach(text)
    log_file=open(log_attach,'rb').read()
    txt=MIMEText(log_file,"base64",'utf-8')
    txt["Content-Type"]='application/octet-stream'
    txt.add_header('Content-Disposition','attachment',filename='log.txt')
    msg.attach(txt)
    report_file=open(report_attach,'rb').read()
    report=MIMEText(report_file,"html",'utf-8')
    report["Content-Type"]='application/octet-stream'
    report.add_header('Content-Disposition','attachment',filename='report.html')
    msg.attach(report)
mail=smtplib.SMTP_SSL(mail_server,mail_port)
mail.login(from_addr,passwd)
mail.sendmail(from_addr,to_addr,msg.as_string())