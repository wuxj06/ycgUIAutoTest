__author__ = 'wuxj06'
import os

base_dir = os.path.split(os.path.realpath(__file__))[0].replace('Common','')

#截图保存地址
img_dir = base_dir + 'img/'
#日志保存地址
log_dir = base_dir + 'Logs/'
#报告保存地址
report_dir = base_dir + 'HtmlReport/'
#测试附件地址
attach_dir = base_dir +"Attachment\\"
