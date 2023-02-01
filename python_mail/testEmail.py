import smtplib
from email.mime.text import MIMEText

class Email:
    def __init__(self):
        self.from_address = 'suxxxx5@huxxxx.com'
        self.smtp_server = 'smtp.xxxxx.com'
        self.user = 'sxxxxxx'
        self.paaswd = '2xxxxxxx'

    def login(self):
        try:
            server = smtplib.SMTP(self.smtp_server, 25)
            server.login(self.user, self.paaswd)
            return server
        except:
            print('邮箱登录失败')

    def sendEmail(self,to_address,subject,message):
        msg = MIMEText(message, 'plain', 'utf-8')
        msg['To'] = to_address
        msg['Subject'] = subject
        server = self.login()
        server.sendmail(self.from_address, to_address, msg.as_string())
        server.quit()

if __name__ == '__main__':
    email = Email()
    addr_list = ['suxxxxx@huxxxxxs.com','mexxxao2@huxxxm.com']
    to_addr = ','.join(addr_list)  #逗号连接收件人账号
    subject = '终身误'
    message = '花谢花飞花满天，红消香断有谁怜。\n游丝软系飘香榭，落絮轻沾扑绣帘。\n'
    message1 = '都道是金玉良缘，俺只念木石前盟。\n空对着，山中高士晶莹雪；\n终不忘，世外仙姝寂寞林；\n叹人间，美中不足今方信。\n纵然是齐眉举案，到底意难平。\n'
    email.sendEmail(to_addr,subject,message1)
