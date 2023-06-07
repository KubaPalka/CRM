import pytest
from django.core.exceptions import ValidationError
from crm_app.validators import validate_nip_number

def test_validate_nip_number():
    try:
        validate_nip_number('7352255837')
    except ValidationError:
        assert False, 'Błąd testu poprawnego numeru NIP!'
    with pytest.raises(ValidationError) as e:
        validate_nip_number('735225583a')
    assert str(e.value) == "['NIP może zawierać tylko cyfry!']"
    with pytest.raises(ValidationError) as e:
        validate_nip_number('123')
    assert str(e.value) == "['NIP powinien mieć 10 cyfr!']"



