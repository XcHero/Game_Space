import tkinter as tk
from tkinter import messagebox
from data_process import read_data
import sign_in
from reset_password import reset_pw


def font_set(size):
    font = ('Microsoft YaHei', size)
    return font


def start_program():
    # 用户登录
    def user_login():
        name = user_name_text.get()
        pw = user_pw_text.get()
        user_dict = read_data()
        if name != '' and pw != '':
            if name in user_dict.keys():
                if pw == user_dict[name]:
                    print('登录成功')
                    tk.messagebox.showinfo(title='登录成功', message='欢迎【{}】来到Maker’s Game Space！'.format(name))
                else:
                    print('密码错误')
                    tk.messagebox.showerror(title='密码错误', message='密码错误，请重新输入密码！')
            else:
                print('用户名错误')
                tk.messagebox.showerror(title='用户名错误', message='用户名错误，请确认用户名信息！')
        else:
            print('用户名或密码不能为空')
            tk.messagebox.showinfo(title='用户名或密码错误', message='用户名或密码不能为空！')

    main_window = tk.Tk()
    main_window.title('Maker‘s Game Space')
    width = 500
    height = 500
    screen_width, screen_height = main_window.maxsize()
    align_str = "{}x{}+{}+{}".format(width, height, int((screen_width - width) / 2), int((screen_height - height) / 2))
    main_window.geometry(align_str)
    main_window.resizable(width=False, height=False)
    # 设置透明度
    main_window.attributes('-alpha', 0.9)
    main_window.attributes('-topmost', 0)
    # 设置标签内容及位置
    user_name_label = tk.Label(main_window, text='用户名', font=font_set(15))
    user_name_label.place(x=100, y=100)
    user_pw_label = tk.Label(main_window, text='密码', font=font_set(15))
    user_pw_label.place(x=100, y=150)

    # 设置账号、密码输入框
    user_name_text = tk.StringVar()
    user_name_text.set('请输入用户名')
    user_name_entry = tk.Entry(main_window, textvariable=user_name_text, font=font_set(15), width=15)
    user_name_entry.place(x=190, y=100)
    user_pw_text = tk.StringVar()
    user_pw_text.set('请输入密码')
    user_pw_entry = tk.Entry(main_window, textvariable=user_pw_text, font=font_set(15), width=15)
    user_pw_entry.place(x=190, y=150)

    # 设置忘记密码
    user_forget_pw_button = tk.Button(main_window, text='忘记密码', font=font_set(8), command=reset_pw)
    user_forget_pw_button.place(x=420, y=450)

    # 设置登录、注册按钮
    user_login_button = tk.Button(main_window, text='登录', font=font_set(15), command=user_login)
    user_login_button.place(x=100, y=300)
    user_register_button = tk.Button(main_window, text='注册', font=font_set(15), command=sign_in.sign_in)
    user_register_button.place(x=320, y=300)

    main_window.mainloop()


if __name__ == "__main__":
    start_program()
