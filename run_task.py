import os
import django

# 1. 告诉 Django 去哪里找 settings 文件
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WafControl.settings')

# 2. 初始化 Django（必须在这一步之后才能 import 模型）
django.setup()
from wafinstaller.tasks import _update_waf_attacks_core, ngx_mod, delete_old_attacks, update_dashboard_stats



if __name__ == '__main__':
    update_dashboard_stats()
    print("delete: ", delete_old_attacks())
    _update_waf_attacks_core(ngx_mod, 'nginx')
