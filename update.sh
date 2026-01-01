#!/bin/bash
echo 'rewrite service'
# 注册服务单元
cp mtp.service /etc/systemd/system/mtp.service
# 重载
echo 'reload daemon'
systemctl daemon-reload
# 重启服务
echo 'restart service'
systemctl restart mtp.service
systemctl status mtp.service