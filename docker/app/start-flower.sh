
#!/bin/sh

set -o errexit
set -o nounset

celery flower -A test_task_yazz.apps.taskapp --basic_auth="${CELERY_FLOWER_USER}:${CELERY_FLOWER_PASSWORD}"
