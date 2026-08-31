export const getProductos = async () => {
    const response = await fetch('http://127.0.0.1:8000/productos');
    if (!response.ok) {
        throw new Error('Error al conectar con la API');
    }
    return await response.json();
};

