from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from .models import Node

class NodeAPITests(APITestCase):
    def setUp(self):
        self.create_url = reverse('node-list')
        self.node_data = {
            'name': 'Test Node',
            'prompt': 'What day is today?'
        }

    def test_create_node(self):
        response = self.client.post(self.create_url, self.node_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('prompt', response.data)
        self.assertIn('response', response.data)
        self.assertEqual(response.data['prompt'], self.node_data['prompt'])

    # def test_get_nodes(self):
    #     # Create a node first
    #     self.client.post(self.create_url, self.node_data, format='json')
        
    #     # Fetch the nodes
    #     response = self.client.get(self.create_url, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(len(response.data), 1)
    #     self.assertEqual(response.data[0]['prompt'], self.node_data['prompt'])

    # def test_get_node(self):
    #     # Create a node first
    #     create_response = self.client.post(self.create_url, self.node_data, format='json')
    #     node_id = create_response.data['id']
        
    #     # Fetch the specific node
    #     response = self.client.get(reverse('node-detail', args=[node_id]), format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['prompt'], self.node_data['prompt'])

    # def test_update_node(self):
    #     # Create a node first
    #     create_response = self.client.post(self.create_url, self.node_data, format='json')
    #     node_id = create_response.data['id']
        
    #     # Update the node
    #     updated_data = {
    #         'name': 'Updated Node',
    #         'prompt': 'This is an updated test prompt'
    #     }
    #     response = self.client.put(reverse('node-detail', args=[node_id]), updated_data, format='json')
    #     self.assertEqual(response.status_code, status.HTTP_200_OK)
    #     self.assertEqual(response.data['prompt'], updated_data['prompt'])

    # def test_delete_node(self):
    #     # Create a node first
    #     create_response = self.client.post(self.create_url, self.node_data, format='json')
    #     node_id = create_response.data['id']
        
    #     # Delete the node
    #     response = self.client.delete(reverse('node-detail', args=[node_id]), format='json')
    #     self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        
    #     # Verify the node is deleted
    #     response = self.client.get(reverse('node-detail', args=[node_id]), format='json')
    #     self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
