class Balance:
    def __init__(self, amount_owe=0.0, amount_get_back=0.0):
        self._amount_owe = amount_owe
        self._amount_get_back = amount_get_back

    @property
    def amount_owe(self):
        return self._amount_owe

    @amount_owe.setter
    def amount_owe(self, value):
        self._amount_owe = value

    @property
    def amount_get_back(self):
        return self._amount_get_back

    @amount_get_back.setter
    def amount_get_back(self, value):
        self._amount_get_back = value