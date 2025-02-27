from flask import Flask, request, jsonify
from backend.block_manager import BlockManager
from backend.block import Block

app = Flask(__name__)
block_manager = BlockManager()

@app.route('/create_block', methods=['POST'])
def create_block():
    data = request.json
    block = Block(data['name'], data['prompt'])
    block_manager.add_block(block)
    return jsonify({"message": "Block created successfully"}), 201

@app.route('/connect_blocks', methods=['POST'])
def connect_blocks():
    data = request.json
    output_block = block_manager.blocks[data['output_block_index']]
    input_block = block_manager.blocks[data['input_block_index']]
    block_manager.connect_blocks(output_block, input_block)
    return jsonify({"message": "Blocks connected successfully"}), 200

@app.route('/execute_blocks', methods=['POST'])
def execute_blocks():
    block_manager.execute_blocks()
    return jsonify({"message": "Blocks executed successfully"}), 200

if __name__ == '__main__':
    app.run(debug=True)
