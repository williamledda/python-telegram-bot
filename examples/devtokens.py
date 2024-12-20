import configparser


class DevTokens:
    def __init__(self):
        tokens_config = configparser.ConfigParser()
        tokens_config.read('conf/tokens.ini')

        if 'devtokens' in tokens_config:
            self.tokens = tokens_config['devtokens']

    def get_token(self, key: str) -> str:
        return self.tokens[key]


# if __name__ == '__main__':
#     devtokens = DevTokens()
#     print(devtokens.get_token('willdevbot'))