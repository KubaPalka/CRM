def validate_nip_number(nip):
    nip = str(nip)
    if len(nip) != 10:
        return "NIP powinien mieć 10 cyfr!"
    if not nip.isdigit():
        return "NIP może zawierać tylko cyfry!"
    wages = (6, 5, 7, 2, 3, 4, 5, 6, 7)
    checksum = sum(int(nip[i]) * wages[i] for i in range(9))
    if not checksum % 11 == int(nip[-1]):
        return "Numer NIP jest niepoprawny!"
    else:
        return "NIP poprawny"
