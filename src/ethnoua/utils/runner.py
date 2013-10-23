from logan.runner import run_app

def generate_settings():
    """
    This command is run when ``default_path`` doesn't exist, or ``init`` is
    run and returns a string representing the default data to put into their
    settings file.
    """
    return ""

def main():
    run_app(
        project='ethnoua',
        default_config_path='~/.ethnoua/',
        default_settings='ethnoua.conf.server',
        settings_initializer='ehtnoua.utils.runner.generate_settings',
        settings_envvar='ETHNOUA_CONF'
    )

if __name__ == '__main__':
    main()