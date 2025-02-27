class UserInterface:
    def __init__(self, block_manager):
        self.block_manager = block_manager

    def create_block(self, name, prompt):
        block = Block(name, prompt)
        self.block_manager.add_block(block)

    def connect_blocks(self, output_block, input_block):
        self.block_manager.connect_blocks(output_block, input_block)

    def run(self):
        self.block_manager.execute_blocks()
