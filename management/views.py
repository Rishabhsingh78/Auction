from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from .models import Auction,User

from .serializers import AuctionSerializer,UpdateAuctionSerializer

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_auction(request):
    serializer = AuctionSerializer(data = request.data,context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def auction_list(request):
    auction = Auction.objects.all()
    serializer = AuctionSerializer(auction,many = True)
    return Response({'Payload':serializer.data},status=status.HTTP_200_OK)


@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_auction(request,auction_id):
    try:
        auction = Auction.objects.get(id=auction_id, created_by=request.user)
    except Auction.DoesNotExist:
        return Response({"error": "Auction not found or you are not the creator."}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = UpdateAuctionSerializer(auction,data = request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PATCH'])
@permission_classes([IsAuthenticated])
def close_auction(request,auction_id):
    try:
        auction = Auction.objects.get(id=auction_id, created_by=request.user)
    except Auction.DoesNotExist:
        return Response({"error": "Auction not found or you are not the creator."}, status=status.HTTP_404_NOT_FOUND)
    auction.is_closed = True
    auction.save()
    serializer = AuctionSerializer(auction)

    return Response({"message": "Auction closed successfully.",'data':serializer.data}, status=status.HTTP_200_OK)