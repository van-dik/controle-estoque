from rest_framework import serializers
from .models import Produto


class ProdutoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Produto
        fields = ['id', 'nome', 'codigo', 'quantidade', 'preco', 'criado_em', 'atualizado_em']
        read_only_fields = ['criado_em', 'atualizado_em']


class AtualizarEstoqueSerializer(serializers.Serializer):
    operacao = serializers.ChoiceField(choices=['adicionar', 'remover'])
    quantidade = serializers.IntegerField(min_value=1)

    def validate(self, data):
        if data['operacao'] == 'remover':
            produto = self.context.get('produto')
            if produto and data['quantidade'] > produto.quantidade:
                raise serializers.ValidationError(
                    'Não é possível remover mais itens do que há em estoque.'
                )
        return data
