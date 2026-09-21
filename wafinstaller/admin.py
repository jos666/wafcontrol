from django.contrib import admin

# Register your models here.

from .models import Attack, AppSetting, DashboardStat

@admin.register(Attack)
class AttackAdmin(admin.ModelAdmin):
    list_display = ('id', 'timestamp', 'ip', 'rule_id', 'severity','message')
    list_filter = ('severity', 'rule_id')
    search_fields = ('ip', 'rule_id', 'msg')
    ordering = ('-timestamp',)

@admin.register(AppSetting)
class AppSettingAdmin(admin.ModelAdmin):
    pass

@admin.register(DashboardStat)
class DashboardStatAdmin(admin.ModelAdmin):
    pass
#@admin.register(CrsVersion)
#class CrsVersionAdmin(admin.ModelAdmin):
#    list_display = ('id', 'version', 'update_time')
#
#@admin.register(DashboardStat)
#class DashboardStatAdmin(admin.ModelAdmin):
#    list_display = ('id', 'stat_date', 'total_attacks', 'blocked_attacks')
