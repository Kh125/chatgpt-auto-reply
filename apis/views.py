from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView
from django.conf import settings
from .serializers import BookSerializer
from .models import Book
import requests
import openai

openai.api_key = settings.OPENAI_API_KEY
openai.organization = settings.OPENAI_ORGANIZATION

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class ChatAPIView(APIView):
    def post(self, request, *args, **kwargs):
        if not openai.api_key:
            return Response(
                {'error': 'OPENAI_API_KEY is not configured. Please set it in your environment variables or .env file.'},
                status=status.HTTP_500_INTERNAL_SERVER_ERROR,
            )

        user_message = request.data.get('message')

        if not user_message:
            return Response("Provide a relevant message from user!", status=status.HTTP_400_BAD_REQUEST)
        
        prompt = f"User message: {user_message} \n Provide relavent response from api data."

        try:
            gpt_response = openai.chat.completions.create(
                model="gpt-4o-mini-2024-07-18",
                messages= [{
                    "role": "user",
                    "content": prompt
                }],
                max_tokens=150
            )

            reply = gpt_response.choices[0].message.content

            return Response({'reply': reply})
        
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class RandomUserAPI(APIView):
    def get(self, request, *args, **kwargs):
        try:
            response = requests.get('https://randomuser.me/api/')
            response.raise_for_status()

            data = response.json()

            data = data['results']

            return Response(data, status=status.HTTP_200_OK)
        except Exception as e:
            return Response({'error': str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
