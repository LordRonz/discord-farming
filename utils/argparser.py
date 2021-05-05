def get_args():
    import argparse
    parser = argparse.ArgumentParser(description='Sucking MEE6\'s cock')
    parser.add_argument('-i', default=3.0, type=float, help='initial delay(sec)', )
    parser.add_argument('-d', default=60.0, type=float, help='delay between messages(sec)')
    parser.add_argument('-l', action='store_true', help='locate textbox')
    parser.add_argument('-r', action='store_true', help='delete message after sending it')
    parser.add_argument('-s', default=None, help='test file source(shakespeare, or potter, or uzumaki, or AMOGUS)')
    parser.add_argument('-w', action='store_true', help='write mode(default=copy paste mode)')

    return vars(parser.parse_args())