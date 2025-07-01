import time
from django.db import connections
from django.db.utils import OperationalError
from django.core.management.base import BaseCommand
from psycopg2 import OperationalError as Psycopg2OperationalError

class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.write('⏳ DB 연결 시도 중...')

        for attempt in range(20):  # 최대 20회 시도 (20초)
            try:
                conn = connections['default']
                conn.cursor()
                break
            except (OperationalError, Psycopg2OperationalError):
                self.stdout.write(f'🔁 [{attempt+1}] 아직 DB가 준비되지 않았습니다. 다시 시도...')
                time.sleep(1)

        self.stdout.write(self.style.SUCCESS('✅ DB 연결 성공!'))
