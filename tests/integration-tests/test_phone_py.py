import pytest

from src.agenda.agenda_py import Agenda

@pytest.fixture
def agenda(tmpdir):
    """Provides an empty agenda """
    return Agenda(tmpdir)


def test_pesquisar_por_nome(agenda):
    agenda.add("Bob", "12345")
    assert "12345" == agenda.search("Bob")


def test_agenda_contem_todos_nomes(agenda):
    agenda.add("Bob", "12345")
    assert "Bob" in agenda.nomes()


def test_nome_nao_encontrado_raises_error(agenda):
    # agenda.add("Python", "12345")
    with pytest.raises(KeyError):
        agenda.search("Python")


def test_get_user_from_api(agenda):
    user = agenda.get_user_from_api("beatles")
    assert user == "beatles"
