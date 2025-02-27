import React from 'react';

function Connection({ from, to }) {
  return (
    <div className="connection">
      <p>Connection from {from} to {to}</p>
    </div>
  );
}

export default Connection;
