from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Cart, CartProduct
from .serializers import CartProductSerializer, CartSerializer  
import requests

def get_product_type(type_product):
    if type_product == 'book':
        return 1
    elif type_product == 'cloth':
        return 2
    elif type_product == 'mobile':
        return 3
    else:
        return None

class ListCartAPIView(APIView):
    def get(self, request):
        carts = Cart.objects.all()
        serializer = CartSerializer(carts, many=True)
        return Response(serializer.data)

class GetCartAPIView(APIView):
    def get(self, request, user_id):
        try:
            cart = Cart.objects.get(user_id=user_id)
            cart_products = CartProduct.objects.filter(cart=cart)
            serializer = CartProductSerializer(cart_products, many=True)
            product_details = []

            for cart_product in cart_products:
                product_url = get_product_type(cart_product.type_product)
                response = requests.get(f'http://localhost:800{product_url}/{cart_product.type_product}s/{cart_product.product_id}/')
                if response.status_code == 200:
                    product_info = response.json()
                    product_info['quantity'] = cart_product.quantity
                    product_info['type_product']  = cart_product.type_product
                    product_details.append(product_info)
                    
            cart_info = {
                'cart_id': cart.id,
                'user_id': cart.user_id,
                'date': cart.date,
                'products': product_details 
            }


            return Response(cart_info)
        except Cart.DoesNotExist:
            return Response({'message': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

class RetrieveCartAPIView(APIView):
    def get(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
            serializer = CartSerializer(cart)
            return Response(serializer.data)
        except Cart.DoesNotExist:
            return Response({'message': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

class CreateCartAPIView(APIView):
    def post(self, request):
        serializer = CartSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateCartAPIView(APIView):
    def put(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response({'message': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartSerializer(cart, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class DeleteCartAPIView(APIView):
    def delete(self, request, pk):
        try:
            cart = Cart.objects.get(pk=pk)
        except Cart.DoesNotExist:
            return Response({'message': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

        cart.delete()
        return Response({'message': 'Cart deleted successfully'})        

class ViewCartAPIView(APIView):
    def get(self, request, user_id):
        try:
            print('hello')
            cart = Cart.objects.get(user_id=user_id)
            cart_products = CartProduct.objects.filter(cart=cart)
            serializer = CartProductSerializer(cart_products, many=True)
            product_details = []

            # for cart_product in cart_products:
            #     product_url = get_product_type(cart_product.type_product)
            #     response = requests.get(f'http://localhost:800{product_url}/{cart_product.type_product}s/{cart_product.product_id}/')
            #     if response.status_code == 200:
            #         product_details.append(response.json())
                    
            cart_info = {
                'cart_id': cart.id,
                'user_id': cart.user_id,
                'date': cart.date,
                'products': product_details  # Danh sách chi tiết sản phẩm
            }

            # Trả về thông tin của giỏ hàng và chi tiết của từng sản phẩm
            return Response(cart_info)
        except Cart.DoesNotExist:
            return Response({'message': 'Cart not found'}, status=status.HTTP_404_NOT_FOUND)

class AddToCartAPIView(APIView):
    def post(self, request):
        serializer = CartProductSerializer(data=request.data)
        if serializer.is_valid():
            # Lấy thông tin từ request
            print(request.data)

            product_id = serializer.validated_data.get('product_id')
            user_id = request.data
            quantity = serializer.validated_data.get('quantity')
            type_product = serializer.validated_data.get('type_product')

            # Kiểm tra xem giỏ hàng đã tồn tại chưa
            cart = Cart.objects.get(id=request.data['cart'])
            # print(cart)


            # Thêm sản phẩm vào giỏ hàng
            cart_product, created = CartProduct.objects.get_or_create(
                cart=cart,
                product_id=product_id,
                type_product= type_product,
                defaults={'quantity': quantity}
            )

            # Cập nhật số lượng nếu sản phẩm đã tồn tại trong giỏ hàng
            if not created:
                cart_product.quantity += quantity
                cart_product.save()

            return Response({'message': 'Product added to cart successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateCartItemAPIView(APIView):
    def put(self, request, pk):
        try:
            cart_product = CartProduct.objects.get(pk=pk)
        except CartProduct.DoesNotExist:
            return Response({'message': 'Product not found in cart'}, status=status.HTTP_404_NOT_FOUND)

        serializer = CartProductSerializer(cart_product, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'message': 'Product updated in cart successfully'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RemoveCartItemAPIView(APIView):
    def delete(self, request, pk):
        try:
            cart_product = CartProduct.objects.get(pk=pk)
        except CartProduct.DoesNotExist:
            return Response({'message': 'Product not found in cart'}, status=status.HTTP_404_NOT_FOUND)

        cart_product.delete()
        return Response({'message': 'Product removed from cart successfully'})