from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from .models import Node
from .serializers import NodeSerializer
import requests
import os
import logging

class NodeViewSet(viewsets.ModelViewSet):
    queryset = Node.objects.all()
    serializer_class = NodeSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        prompt = serializer.validated_data['prompt']
        prompt = [{'role': 'system', 'content': prompt}]
        # Call ChatGPT API
        chatgpt_response = self.call_chatgpt_api(prompt)
        
        # Save the node with the generated response
        node = serializer.save()
        node.response = chatgpt_response
        node.save()
        
        headers = self.get_success_headers(serializer.data)
        return Response({'prompt': prompt, 'response': chatgpt_response}, status=status.HTTP_201_CREATED, headers=headers)

    def call_chatgpt_api(self, prompt):

        logger = logging.getLogger(__name__)
        logging.basicConfig()
        api_key = os.getenv('OPENAI_API_KEY')
        logger.setLevel(logging.DEBUG)
        handler = logging.StreamHandler()
        handler.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)
        logger.addHandler(handler)
        logger.info(f"API Key: {api_key}")
        headers = {
            'Authorization': f'Bearer {api_key}',
            'Content-Type': 'application/json'
        }
        data = {
            'messages': prompt,
            'model': 'gpt-4o-mini',
            'max_tokens': 150,
            'temperature': 0.5
        }
        response = requests.post('https://api.openai.com/v1/chat/completions', headers=headers, json=data)
        response_data = response.json()
        # Log the response from GPT
        logger.info(f"GPT-4 Response: {response_data}")

        return response_data['choices'][0]['message']['content'].strip()
    
