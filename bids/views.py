from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from .models import Bids
from management.models import Auction
from .serializer import *


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def place_bid(request,auction_id):
    try:
        auction = Auction.objects.get(id = auction_id)
    except Auction.DoesNotExist:
        return Response({"error": "Auction not found."}, status=status.HTTP_404_NOT_FOUND)
    serializer = BidSerializer(data=request.data, context={'request': request, 'auction': auction})
    if serializer.is_valid():
        serializer.save()

        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def bids_list(request):
    bids = Bids.objects.all()
    serializer = BidListSerializer(bids,many = True)
    return Response({'Data':serializer.data},status=status.HTTP_200_OK)