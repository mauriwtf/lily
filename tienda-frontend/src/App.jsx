import { useState, useEffect } from 'react';
import { getProductos } from './services/api';
import { ProductCard } from './components/ProductCard';

export function App() {
  const [productos, setProductos] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  useEffect(() => {
    setIsLoading(true);
    setError(null);

    getProductos()
      .then((data) => {
        setProductos(data);
      })
      .catch((err) => {
        setError(err.message || 'Ocurrió un error inesperado');
      })
      .finally(() => {
        setIsLoading(false);
      });
  }, []);

  return (
    <div style={{ padding: '20px', maxWidth: '1000px', margin: '0 auto', fontFamily: 'sans-serif' }}>
      <h1>Catálogo FreshMix</h1>

      {/* Estado de Carga */}
      {isLoading && <p style={{ fontSize: '18px', color: '#555' }}>Cargando productos...</p>}

      {/* Estado de Error */}
      {!isLoading && error && (
        <div style={{ color: '#d9534f', padding: '15px', border: '1px solid #d9534f', borderRadius: '5px', backgroundColor: '#fdf7f7' }}>
          <p style={{ margin: 0 }}><strong>Error:</strong> {error}</p>
        </div>
      )}

      {/* Catálogo Vacío */}
      {!isLoading && !error && productos.length === 0 && (
        <p style={{ color: '#777', fontStyle: 'italic' }}>No hay productos disponibles en este momento.</p>
      )}

      {/* Listado de Productos */}
      {!isLoading && !error && productos.length > 0 && (
        <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '20px' }}>
          {productos.map((prod) => (
            <ProductCard key={prod.id} producto={prod} />
          ))}
        </div>
      )}
    </div>
  );
}

export default App;