#!/bin/bash

# Detect new attached disks without rebooting

for host in /sys/class/scsi_host/*; do echo "- - -" | sudo tee $host/scan; ls /dev/sd* ; done
