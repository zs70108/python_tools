class Converter(object):
    @staticmethod
    def to_ascii(h):
        list_s = []
        # "".join(h.split())
        list_h = h.replace(" ","")
        for i in range(0, len(list_h), 2):
            list_s.append(chr(int(list_h[i:i+2], 16)))
        return ''.join(list_s)

    @staticmethod
    def to_hex(s):
        list_h = []
        for c in s:
            list_h.append(str(hex(ord(c))[2:]))
            list_h.append(" ")
        return ''.join(list_h)