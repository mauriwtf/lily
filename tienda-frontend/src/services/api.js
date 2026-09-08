export const getProductos = async ({ page = 0, limit = 2, nombre = '' } = {}) => {
  const params = new URLSearchParams({
    page: page.toString(),
    limit: limit.toString(),
  });

  if (nombre.trim() !== '') {
    params.append('nombre', nombre);
  }

  const response = await fetch(`http://127.0.0.1:8000/productos?${params.toString()}`);
  if (!response.ok) {
    throw new Error('Error al conectar con la API');
  }
  return await response.json();
};