import sys
import tkinter as tk
from tkinter import messagebox
from data_process import read_data


def font_set(size):
    font = ('Microsoft YaHei', size)
    return font


def sign_in():
    sign_in_window = tk.Toplevel()
    sign_in_window.title('Welcome To Maker‘s Game Space！')
    width = 400
    height = 400
    screen_width, screen_height = sign_in_window.maxsize()
    align_str = "{}x{}+{}+{}".format(width, height, int((screen_width - width) / 2), int((screen_height - height) / 2))
    sign_in_window.geometry(align_str)
    sign_in_window.resizable(width=False, height=False)
    sign_in_window.attributes('-alpha', 0.9)
    sign_in_window.attributes('-topmost', 1)

    # 用户名标签、输入框
    new_user_name_label = tk.Label(sign_in_window, text='用户名', font=font_set(15))
    new_user_name_label.place(x=50, y=50)
    new_user_name_text = tk.StringVar()
    new_user_name_text.set('请输入用户名')
    new_user_entry = tk.Entry(sign_in_window, text=new_user_name_text, font=font_set(15), width=15)
    new_user_entry.place(x=170, y=50)

    # 输入密码标签、输入框
    new_pw1_label = tk.Label(sign_in_window, text='输入密码', font=font_set(15))
    new_pw1_label.place(x=50, y=100)
    new_pw1_text = tk.StringVar()
    new_pw1_text.set('请输入密码')
    new_pw1_entry = tk.Entry(sign_in_window, text=new_pw1_text, font=font_set(15), width=15)
    new_pw1_entry.place(x=170, y=100)

    # 确认密码标签、输入框
    new_pw2_label = tk.Label(sign_in_window, text='确认密码', font=font_set(15))
    new_pw2_label.place(x=50, y=150)
    new_pw2_text = tk.StringVar()
    new_pw2_text.set('请确认密码')
    new_pw2_entry = tk.Entry(sign_in_window, text=new_pw2_text, font=font_set(15), width=15)
    new_pw2_entry.place(x=170, y=150)

    # 信息确认
    def infor_confirm():
        user_dict = read_data()
        name = new_user_name_text.get()
        pw1 = new_pw1_text.get()
        pw2 = new_pw2_text.get()

        if name in user_dict:
            print('用户已存在，请选择登录！')
            tk.messagebox.showinfo(title='用户已存在', message='用户已存在，请选择登录！')
            sign_in_window.destroy()
        elif pw1 == pw2:
            with open(r'{}//data.txt'.format(sys.path[0]), 'a') as f:
                f.writelines('{}:{}'.format(name, pw1) + '\n')
                f.flush()
            f.close()
            print('注册成功')
            tk.messagebox.showinfo(title='注册成功', message='注册成功，请登录!')
            sign_in_window.destroy()
        else:
            print('两次密码不一致！')
            tk.messagebox.showerror(title='', message='两次密码不一致，请确认密码！')

    # 注册按钮
    sign_in_button = tk.Button(sign_in_window, text='注册', width=20, command=infor_confirm)
    sign_in_button.place(x=120, y=300)

    sign_in_window.mainloop()


if __name__ == '__main__':
    sign_in()
