#!/bin/bash

python3 manage.py create_tables
python3 manage.py add_data_tables
/usr/sbin/apache2ctl -D FOREGROUND

