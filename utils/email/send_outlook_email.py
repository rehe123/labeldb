import win32com.client as win32


class send_email():
    def send_outlook_mail(self, to_addr, mail_subject, mail_content, cc_addr='', attachment=''):
        outlook = win32.Dispatch("outlook.Application")  # 固定写法
        mail = outlook.CreateItem(0)  # 固定写法

        mail.To = to_addr  # 收件人

        if len(cc_addr.split()) > 0:
            mail.CC = cc_addr
        # mail.Recipients.Add(address)
        #
        mail.Subject = mail_subject

        if len(attachment.split()) > 0:
            mail.Attachments = attachment

        mail.Body = mail_content  # 邮件内容

        mail.Send()  # 发送

if __name__ == '__main__':
   email = send_email()

   email.send_outlook_mail('wangyunhui@163.com','测试附件功能','12312',attachment='文件绝对路径')


