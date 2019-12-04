import Email_Test as em

def main():
    email_user = input('邮箱:')
    #授权码：Cs123456，不是邮箱登陆密码，需要发短信开通权限
    password = input('pop3授权码:')
    em.c_step4_get_email.run_ing(email_user, password)

if __name__ == '__main__':
    main()