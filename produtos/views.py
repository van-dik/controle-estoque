from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Produto
from .serializers import ProdutoSerializer, AtualizarEstoqueSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    @action(detail=True, methods=['post'])
    def atualizar_estoque(self, request, pk=None):
        produto = self.get_object()
        serializer = AtualizarEstoqueSerializer(
            data=request.data,
            context={'produto': produto}
        )
        
        if serializer.is_valid():
            operacao = serializer.validated_data['operacao']
            quantidade = serializer.validated_data['quantidade']
            
            if operacao == 'adicionar':
                produto.quantidade += quantidade
            else:  # remover
                produto.quantidade -= quantidade
            
            produto.save()
            return Response(ProdutoSerializer(produto).data)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
