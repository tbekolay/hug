import hug

API = hug.API('git')


@hug.object(name='git', version='1.0.0', api=API)
class GIT(object):
    """An example of command like calls via an Object"""

    def __init__(self):
        self._config = None

    @hug.object.cli_property
    @property
    def config(self):
        return self._config

    @config.setter
    def config(self, _config):
        self._config = _config

    @hug.object.cli
    def push(self, branch='master'):
        if self.config is not None:
            print('Using config file %r' % self.config)
        return 'Pushing {}'.format(branch)

    @hug.object.cli
    def pull(self, branch='master'):
        if self.config is not None:
            print('Using config file %r' % self.config)
        return 'Pulling {}'.format(branch)


if __name__ == '__main__':
    API.cli()
