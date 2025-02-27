import React from 'react';

function Block({ id }) {
  return (
    <div className="block" id={id}>
      <h2>Block {id}</h2>
      <textarea placeholder="Enter prompt here..."></textarea>
    </div>
  );
}

export default Block;
