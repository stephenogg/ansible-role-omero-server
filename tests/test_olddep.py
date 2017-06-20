import testinfra.utils.ansible_runner
import re

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    '.molecule/ansible_inventory').get_hosts('omero-server-olddep')

OMERO = '/opt/omero/server/OMERO.server/bin/omero'


def test_omero_version(Command, Sudo):
    with Sudo('data-importer'):
        ver = Command.check_output("%s version" % OMERO)
    assert re.match('5\.2\.\d+-ice35-', ver)


def test_postgres_version(Command):
    ver = Command.check_output("psql --version")
    assert ver.startswith('psql (PostgreSQL) 9.4.')
