import sys


def read_data():
    user_infor_dict = {}
    with open(r'{}//data.txt'.format(sys.path[0]), 'r') as f:
        rows = f.readlines()
        for row in rows:
            dict_list = row.strip().split(':')
            if len(dict_list) > 1:
                user_infor_dict[dict_list[0]] = dict_list[1]
    return user_infor_dict


def reset_pwd(name, pwd):
    user_infor = read_data()
    old_pwd = user_infor[name]
    if pwd == old_pwd:
        print('新密码与旧密码一致，请设定其他密码！')
        return False
    else:
        user_infor[name] = pwd
        print('密码重置成功！')
        # 密码写入
        with open(r'{}//data.txt'.format(sys.path[0]), 'w') as f:
            rows = f.readlines()
            for row in rows:
                print(row, end='')


if __name__ == '__main__':
    test_dict = read_data()
    print(test_dict)
    for i in test_dict:
        print('{}:{}'.format(i, test_dict[i]))
