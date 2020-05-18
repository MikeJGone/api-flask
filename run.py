from flask_tt import app
import logging
import argparse

parser = argparse.ArgumentParser(description='please input ip and port')


def parse_arge():
    parser.add_argument('-host', type=str, dest='host')
    parser.add_argument('-port', type=str, dest='port')
    return parser.parse_args()


if __name__ == '__main__':
    logger = logging.getLogger(__name__)
    args = parse_arge()
    logger.warning('WEB START')
    app.run(host=args.host, port=args.port)
