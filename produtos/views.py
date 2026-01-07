from django.db.models import Q
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from .models import Produto
from .serializers import ProdutoSerializer, AtualizarEstoqueSerializer


class ProdutoViewSet(viewsets.ModelViewSet):
    queryset = Produto.objects.all()
    serializer_class = ProdutoSerializer

    def get_queryset(self):
        queryset = Produto.objects.all()
        search = self.request.query_params.get('search', None)
        
        if search:
            queryset = queryset.filter(
                Q(nome__icontains=search) | Q(codigo__icontains=search)
            )
        
        return queryset

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

    @action(detail=False, methods=['get'])
    def estoque_baixo(self, request):
        limite = request.query_params.get('limite', '10')
        
        try:
            limite = int(limite)
        except ValueError:
            return Response(
                {'erro': 'O parâmetro limite deve ser um número'},
                status=status.HTTP_400_BAD_REQUEST
            )
        
        produtos = Produto.objects.filter(quantidade__lte=limite)
        serializer = ProdutoSerializer(produtos, many=True)
        return Response(serializer.data)
