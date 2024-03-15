from typing import Literal

import click
from dotenv import find_dotenv, load_dotenv

from config import settings
from project_utils import logger
from project_utils.utils import get_project_root


def main(environment: Literal["staging", "production"]):
    """Runs data processing scripts to turn raw data from (../raw) into
    cleaned data ready to be analyzed (saved in ../processed).
    """
    logger.info(f"making final data set from raw data in environment {environment}")
    logger.info(f"Train modeling using {settings.data.processed}")
    logger.info(f"Model used: {settings.model.name}")
    logger.info(f"Save the output to {settings.data.final}")


@click.command()
@click.option(
    "--environment",
    default="staging",
    type=click.Choice(["staging", "production"]),
    help="The environment to use",
)
def main_cli(environment):
    main(environment)


if __name__ == "__main__":
    root_path = get_project_root()
    logger.info(f"the root path is {root_path}")

    # find .env automagically by walking up directories until it's found, then
    # load up the .env entries as environment variables
    load_dotenv(find_dotenv())

    main(environment="production")
