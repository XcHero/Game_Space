import tkinter as tk
from tkinter import messagebox
# 一封邮件
from email.mime.multipart import MIMEMultipart
# 邮件的内容
from email.mime.text import MIMEText
import smtplib
import random
import re
from data_process import read_data, write_pwd


def font_set(size):
    font = ('Microsoft YaHei', size)
    return font


# 产生6位随机数
def random_code():
    random_list = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                   'h', 'i', 'j', 'k', 'l', 'm', 'n',
                   'o', 'p', 'q', 'r', 's', 't',
                   'u', 'v', 'w', 'x', 'y', 'z',
                   '0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    random_verification_code = ''
    for i in range(6):
        random_verification_code += random_list[random.randint(0, len(random_list) - 1)]
    return random_verification_code


# 发送邮件
def send_email(user_name, email_add, verification_code):
    if user_name not in read_data():
        print('用户不存在，请注册后登陆！')
        tk.messagebox.showinfo('用户不存在', message='用户不存在，请注册后登陆！')
    else:
        print('用户存在，验证后重置密码！')
        # 用户存在，才验证。
        sender = '1330984569@qq.com'
        authorization_pwd = 'xjqflotfjqozijdd'
        receiver = email_add.get()

        email = MIMEMultipart()
        subjcet = '重置密码验证码'
        email['Subject'] = subjcet
        email['From'] = sender
        email['To'] = receiver

        if re.match(r'^[0-9a-zA-Z_]{0,19}@[0-9a-zA-Z]{1,13}\.[com,cn,net]{1,3}$', receiver):
            print('格式正确，邮件发送！')
            content = MIMEText('验证码：{}验证码仅依次有效，请正确输入！'.format(verification_code))
            email.attach(content)
            # 连接服务器发送邮件
            # 1、连接服务器
            smtp = smtplib.SMTP()
            smtp.connect('smtp.qq.com')
            # 2、输入账户和授权码
            smtp.login(sender, authorization_pwd)
            # 3、发送邮件
            smtp.send_message(email)
            # 4、关闭链接
            smtp.close()

            print('邮件发送成功！')
            tk.messagebox.showinfo('发送成功✅', message='邮件发送成功，请注意查收！')
        else:
            print('邮箱格式错误！')
            tk.messagebox.showerror('发送失败❌', message='邮件格式有误，请确认后发送！')


# 确认验证码
def confirm_verification_code(code_enter, verification_code):
    if code_enter.get() == verification_code:
        print('验证码正确')
        tk.messagebox.showinfo('验证码正确✅', message='验证码正确，请输入新密码！')
        return True
    else:
        print('验证码错误')
        tk.messagebox.showerror('失败❌', message='验证码错误，请重新验证！')
        return False


def reset_pwd(name, pwd, confirm_pwd):
    if pwd != confirm_pwd:
        print('两次密码不一致！')
        tk.messagebox.showerror(title='密码不一致', message='两次密码不一致，请重新输入！')
    else:
        print('两次密码一致！')
        write_pwd(name, pwd)

def reset_pw():
    # 界面初始化设定
    reset_pw_window = tk.Toplevel()
    reset_pw_window.title('重置密码')
    width = 400
    height = 400
    screen_width, screen_height = reset_pw_window.maxsize()
    align_str = "{}x{}+{}+{}".format(width, height, int((screen_width - width) / 2), int((screen_height - height) / 2))
    reset_pw_window.geometry(align_str)
    reset_pw_window.resizable(width=False, height=False)
    reset_pw_window.attributes('-alpha', 0.9)

    # 重置界面
    # 用户名
    reset_user_name_label = tk.Label(reset_pw_window, text='用户名', font=font_set(15))
    reset_user_name_label.place(x=50, y=50)
    reset_user_name_text = tk.StringVar()
    reset_user_name_text.set('请输入用户名')
    reset_user_name_entry = tk.Entry(reset_pw_window, text=reset_user_name_text, font=font_set(15), width=15)
    reset_user_name_entry.place(x=150, y=50)

    # 邮箱输入框
    verification_code_label = tk.Label(reset_pw_window, text='邮箱', font=font_set(15))
    verification_code_label.place(x=50, y=100)
    verification_email_text = tk.StringVar()
    verification_email_text.set('邮箱(接收验证码)')
    verification_email_entry = tk.Entry(reset_pw_window, text=verification_email_text, font=font_set(15), width=20)
    verification_email_entry.place(x=150, y=100)

    # 验证码输入框
    verification_code_label = tk.Label(reset_pw_window, text='验证码', font=font_set(15))
    verification_code_label.place(x=50, y=150)
    verification_code_text = tk.StringVar()
    verification_code_text.set('请输入6位验证码')
    verification_code_entry = tk.Entry(reset_pw_window, text=verification_code_text, font=font_set(15), width=15)
    verification_code_entry.place(x=150, y=150)

    # 发送前把验证码保存下来
    verification_code = random_code()
    # 发送按钮
    send_button = tk.Button(reset_pw_window, text='发送验证码', font=font_set(12), width=10,
                            command=lambda: send_email(reset_user_name_entry.get(), verification_email_entry,
                                                       verification_code))
    send_button.place(x=20, y=300)

    # 验证按钮
    verification_button = tk.Button(reset_pw_window, text='确认验证码', font=font_set(12), width=10,
                                    command=lambda: confirm_verification_code(verification_code_entry,
                                                                              verification_code))

    verification_button.place(x=150, y=300)

    # 新密码输入框
    new_pwd_label = tk.Label(reset_pw_window, text='新密码', font=font_set(15))
    new_pwd_label.place(x=50, y=200)
    new_pwd_text = tk.StringVar()
    new_pwd_text.set('请输入新密码')
    new_pwd_entry = tk.Entry(reset_pw_window, text=new_pwd_text, font=font_set(15), width=15)
    new_pwd_entry.place(x=150, y=200)
    # 确认密码输入框
    confirm_pwd_label = tk.Label(reset_pw_window, text='确认密码', font=font_set(15))
    confirm_pwd_label.place(x=50, y=250)
    confirm_pwd_text = tk.StringVar()
    confirm_pwd_text.set('确认新密码')
    confirm_pwd_entry = tk.Entry(reset_pw_window, text=confirm_pwd_text, font=font_set(15), width=15)
    confirm_pwd_entry.place(x=150, y=250)

    # 重置密码按钮
    reset_button = tk.Button(reset_pw_window, text='重置密码', font=font_set(12), width=10,
                             command=lambda: reset_pwd(reset_user_name_entry.get(), new_pwd_entry.get(), confirm_pwd_entry.get()))

    reset_button.place(x=270, y=300)
    reset_pw_window.mainloop()


if __name__ == '__main__':
    reset_pw()
