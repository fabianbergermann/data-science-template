# -- First you import Dynaconf
from dynaconf import Dynaconf

# -- Then you create your `settings` instance
settings = Dynaconf(
    settings_files=[                      # Paths or globs to any toml|yaml|ini|json|py
        "configs/default_settings.toml",  # a file for default settings
        "configs/settings.toml",          # a file for main settings
        "configs/.secrets.toml"           # a file for sensitive data (gitignored)
    ],

    #environments=True,                    # Enable layered environments
                                          # (sections on config file for development, production, testing)

    load_dotenv=True,                     # Load envvars from a file named `.env`
                                          # TIP: probably you don't want to load dotenv on production environments
                                          #      pass `load_dotenv={"when": {"env": {"is_in": ["development"]}}}

    envvar_prefix="DYNACONF",             # variables exported as `DYNACONF_FOO=bar` becomes `settings.FOO == "bar"`
    env_switcher="ENV_FOR_DYNACONF",      # to switch environments `export ENV_FOR_DYNACONF=production`

    dotenv_path="configs/.env"            # custom path for .env file to be loaded
)