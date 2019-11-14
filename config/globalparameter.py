# coding: utf-8
# author: felix

import os, time

"""
配置全局变量
"""

# 获取项目路径
project_path = os.path.abspath('.')
# project_path = os.path.abspath(os.path.join(os.path.dirname(os.path.realpath(__file__)[0]), '.'))
# 测试用例存放路径
test_case_path = project_path + '\\src\\test_case'
# 测试数据文档存放路径
data_path = project_path + '\\data'
# 日志文件存放路径
log_path = project_path + '\\log\\mylog.log'
# 测试报告存放路径
report_path = project_path + '\\report\\boos '
report_path = report_path + time.strftime('%Y-%m-%d', time.localtime()) + '.html'
# 异常截图存储路径,并以当前时间作为图片名称前缀
img_path = project_path + '\\erron_img\\' + time.strftime('%Y-%m-%d %H.%M.%S', time.localtime()) + '.img'
# 设置发送测试报告的公共邮箱、账号和密码
smtp_seve = 'smtp.163.com'  # 邮箱SMTP服务，各大运营商的smtp服务可以在网上找
email_name = 'shaoyufei1234@163.com'    # 发件人邮箱账号
email_pass = '13691916244shaos'         # 发件人邮箱密码
email_to = '2310563268@qq.com'          # 收件人邮箱账号，多个可写成list