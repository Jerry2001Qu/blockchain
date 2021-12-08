from blockchain.src.key import Key

def test_verify():
    key = Key()
    message = b"I'm going left"

    signature = key.sign(message)
    assert Key.verify(message, signature, key.get_pub_key())

    fake_message = b"I'm going right"
    assert not Key.verify(fake_message, signature, key.get_pub_key())
