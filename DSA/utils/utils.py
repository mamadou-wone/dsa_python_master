class Utils:

    @classmethod
    def to_lower(cls, chain):
        chain_to_lower = ""
        for ch in chain:
            lower = ch
            if 'A' <= lower <= 'Z':
                lower = chr(ord(ch) - ord('A') + ord('a'))
            chain_to_lower += lower
        return chain_to_lower

    @classmethod
    def to_upper(cls, chain):
        chain_to_upper = ""
        for ch in chain:
            upper = ch
            if 'a' <= upper <= 'z':
                upper = chr(ord(ch) - ord('a') + ord('A'))
            chain_to_upper += upper
        return chain_to_upper

    @classmethod
    def to_binary(cls, number):
        tab = []
        while number != 0:
            bin_value = number % 2
            tab.append(bin_value)
            number = int(number / 2)
        result = ""
        for i in range(len(tab) - 1, -1, -1):
            result += str(tab[i])
        return result

    @classmethod
    def to_digit(cls, number):
        tab = []
        result = None
        while number != 0:
            temp = number % 10
            number = int(number / 10)
            tab.append(temp)
        # for i in range(len(tab) - 1, -1, -1):
        #     result = tab[i]
        #     print(result)
        return tab
