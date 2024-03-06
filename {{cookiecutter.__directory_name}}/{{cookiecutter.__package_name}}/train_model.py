"""
This is the demo code that uses Dynaconf to access settings

Author: Khuyen Tran
"""

from config import settings


def train_model():
    """Function to train the model"""

    print(f"Train modeling using {settings.data.processed}")
    print(f"Model used: {settings.model.name}")
    print(f"Save the output to {settings.data.final}")


if __name__ == "__main__":
    train_model()
