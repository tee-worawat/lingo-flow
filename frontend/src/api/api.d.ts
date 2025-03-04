declare module '@/api/api' {
  interface Node {
    prompt: string;
  }

  export function getNodes(): Promise<{ data: Node[] }>;
  export function createNode(node: Node): Promise<{ data: Node }>;
}