from src.train_model import train_model


def test_train_model():
    res = train_model()
    assert res is None
