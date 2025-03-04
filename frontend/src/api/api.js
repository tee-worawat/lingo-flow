// filepath: /Users/worawatlawanont/task_repo/ai_block_software_dev/frontend/src/api/api.js
import axios from 'axios';

const apiClient = axios.create({
  baseURL: 'http://localhost:8000/api', // Adjust the base URL as needed
  withCredentials: false,
  headers: {
    Accept: 'application/json',
    'Content-Type': 'application/json'
  }
});

export default {
  getNodes() {
    return apiClient.get('/nodes/');
  },
  getNode(id) {
    return apiClient.get(`/nodes/${id}/`);
  },
  createNode(node) {
    return apiClient.post('/nodes/', node);
  },
  updateNode(id, node) {
    return apiClient.put(`/nodes/${id}/`, node);
  },
  deleteNode(id) {
    return apiClient.delete(`/nodes/${id}/`);
  }
};