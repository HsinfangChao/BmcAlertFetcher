# install project dependency
pip install -r /usr/local/BMCAlertFetcher/requirements.txt

sudo useradd -r -g bmc-alert-fetcher -s /bin/false bmc-alert-fetcher

# config systemd
file_path="/etc/systemd/system/bmc-alert-fetcher.service"
cat <<EOL > $file_path
[Unit]  
Description=bmc-alert-fetcher
After=syslog.target network.target 
  
[Service]   
User=bmc-alert-fetcher
Group=bmc-alert-fetcher
Type=simple
ExecStart=/usr/bin/python3 /usr/local/BMCAlertFetcher/baf.py
WorkingDirectory=/usr/local/
Restart=on-failure
  
[Install]  
WantedBy=multi-user.target
EOL

chown -R bmc-alert-fetcher:bmc-alert-fetcher $file_path
chmod 644 $file_path
systemctl daemon-reload

# start baf service
systemctl enable bmc-alert-fetcher
output=$(systemctl start bmc-alert-fetcher 2>&1)
if [ $? -ne 0 ]; then
    echo "start bmc-alert-fetcher err: $output"
fi