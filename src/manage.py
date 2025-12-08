#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""

import os
import sys


def main():
    """Run administrative tasks."""
    _ = os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'core.settings')
    try:
        from django.core.management import execute_from_command_line

    except ImportError as exc:
        raise ImportError(
            """Couldn't import Django. Are you sure it's installed and
            available on your PYTHONPATH environment variable? Did you
            forget to activate a virtual environment?"""
        ) from exc

    try:
        from core.docker.docker_run import start_docker_container

    except ImportError as exc:
        raise ImportError(
            """Couldn't import Docker Module. Are you sure it's installed and
            available on your PYTHONPATH environment variable? Did you
            forget to activate a virtual environment?"""
        ) from exc

    _ = start_docker_container()
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()
