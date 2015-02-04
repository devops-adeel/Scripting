
from net_system.models import Credentials
import django


if __name__ == "__main__":

    django.setup()

    cisco_creds = Credentials.objects.get_or_create(
        username = 'pyclass',
        password = '88newclass',
        description = 'Cisco router credentials'
    )
    print cisco_creds

    arista_creds = Credentials.objects.get_or_create(
        username = 'admin1',
        password = '99saturday',
        description = 'Arista credentials'
    )
    print arista_creds
