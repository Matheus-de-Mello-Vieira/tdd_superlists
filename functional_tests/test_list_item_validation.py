from .base import FunctionalTest
from unittest import skip


class ItemValidationTest(FunctionalTest):
    def test_cannot_add_empty_list_items(self):
        # Edith acessa a página inicial e acidentlamente tenta submeter um item
        # vazio na lista. Ela tecla Enter na caixa de entrada vazia

        # A página inicial é atualizada e há uma menssagem de erro informando
        # que itens da lista não podem estar em branco

        # Ela tenta novamente com um texto para o item, e isso agora funcionou

        # De forma pervesa, ela agora decide submeter um segundo item em branco

        # Ela recebe um aviso semelhante na página da lista

        # E ela pode corrigir isso preenchendo o item com um texto
        self.fail('write me!')
