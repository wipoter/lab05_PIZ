from rest_framework.views import APIView
from .serializers import PlayerSerializer
from rest_framework.response import Response

class PlayerView(APIView):
    def post(self, request):
        serializer = PlayerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=200)
        return Response(serializer.errors, status=400)