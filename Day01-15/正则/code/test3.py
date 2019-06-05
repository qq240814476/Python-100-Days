"""
验证输入用户名和QQ号是否有效并给出对应的提示信息

要求：
用户名必须由字母、数字或下划线构成且长度在6~20个字符之间
QQ号是5~12的数字且首位不能为0
"""

import re


def main():
    username = '{"code":71404,"message":"Not Found","data":{}}'
    # qq = input('请输入QQ号: ')
    m1 = re.findall(r'"code":.*?,"message":".*?","data":.*?', username)
    print(m1)
    # if not m1:
    #     print('请输入有效的用户名.')
    # m2 = re.match(r'^[1-9]\d{4,11}$', qq)
    # if not m2:
    #     print('请输入有效的QQ号.')
    # if m1 and m2:
    #     print('你输入的信息是有效的!')


if __name__ == '__main__':
    main()
