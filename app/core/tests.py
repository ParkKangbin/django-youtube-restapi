from django.test import SimpleTestCase
from unittest.mock import patch, MagicMock
from django.core.management import call_command

from django.db.utils import OperationalError
from psycopg2 import OperationalError as Psycopg20perationalError


@patch('django.db.utils.ConnectionHandler.__getitem__')
class CommandsTests(SimpleTestCase):

    def test_wait_for_db_ready(self, patched_getitem):
        mock_conn = MagicMock()
        patched_getitem.return_value = mock_conn  # MagicMock에는 cursor()가 포함됨!

        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 1)


    @patch('time.sleep')
    def test_wait_for_db_delay(self, patched_sleep, patched_getitem):
        mock_conn = MagicMock()
        mock_conn.cursor.return_value.__enter__.return_value = None  # 커서 mock 처리

        patched_getitem.side_effect = [Psycopg20perationalError] + [OperationalError] * 5 + [mock_conn]

        call_command('wait_for_db')

        self.assertEqual(patched_getitem.call_count, 7)


        #docker-compose run --rm app sh -c 'python manage.py test core'