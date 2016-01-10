import click

from tox.session import Session
from tox.session import VirtualEnv
from tox.session import prepare


class ToxShellVirtualEnv(VirtualEnv):
    def test(self, redirect=False):
        action = self.session.newaction(self, "shell")
        with action:
            self.status = 0
            try:
                self._pcall([os.environ['SHELL']], cwd=cwd, action=action, redirect=False,
                            ignore_ret=ignore_ret)
            except tox.exception.InvocationError as err:
                self.session.report.error(str(err))
                self.status = "commands failed"
            except KeyboardInterrupt:
                self.status = "keyboardinterrupt"
                self.session.report.error(self.status)
                raise


class ShellSession(Session):
    def _makevenv(self, name):
        # modified copy of original function
        envconfig = self.config.envconfigs.get(name, None)
        if envconfig is None:
            self.report.error("unknown environment %r" % name)
            raise LookupError(name)
        venv = VirtualEnv(envconfig=envconfig, session=self)
        self._name2venv[name] = venv
        return venv


@click.command()
@click.argument('env')
def main(env):
    try:
        config = prepare(['-e', env])
        retcode = ShellSession(config).runcommand()
        raise SystemExit(retcode)
    except KeyboardInterrupt:
        raise SystemExit(2)