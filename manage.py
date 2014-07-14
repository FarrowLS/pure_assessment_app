#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    # NOTE: ALL SETTINGS FILES ARE HANDLED VIA ENVIRONMENTAL VARIABLES. EX. POINTING TO development.py FOR DEV AND production.py FOR PRODUCTION
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "pure_assessment_app.settings")

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
