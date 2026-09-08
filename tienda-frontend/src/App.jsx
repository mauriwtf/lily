import { useState, useEffect } from 'react';
import { getProductos } from './services/api';
import { ProductCard } from './components/ProductCard';

export function App() {
  const [productos, setProductos] = useState([]);
  const [isLoading, setIsLoading] = useState(true);
  const [error, setError] = useState(null);

  // Paso 2: Estados de paginación y búsqueda
  const [page, setPage] = useState(0);
  const [busqueda, setBusqueda] = useState('');

  const limit = 2; // Límite de productos por página para probar la paginación

  // Paso 2: useEffect dependiente de [page, busqueda]
  useEffect(() => {
    setIsLoading(true);
    setError(null);

    getProductos({ page, limit, nombre: busqueda })
      .then((data) => {
        setProductos(data);
      })
      .catch((err) => {
        setError(err.message || 'Ocurrió un error al cargar los productos');
      })
      .finally(() => {
        setIsLoading(false);
      });
  }, [page, busqueda]);

  // Paso 4: Manejador del buscador
  const handleBusquedaChange = (e) => {
    const valor = e.target.value;
    setPage(0); // Reinicia la página a 0 al filtrar
    setBusqueda(valor);
  };

  return (
    <div style={{ padding: '20px', maxWidth: '1000px', margin: '0 auto', fontFamily: 'sans-serif' }}>
      <h1>Catálogo FreshMix</h1>

      {/* Paso 4: Input Buscador */}
      <div style={{ marginBottom: '20px' }}>
        <input
          type="text"
          placeholder="Buscar jugo por nombre..."
          value={busqueda}
          onChange={handleBusquedaChange}
          style={{
            padding: '10px',
            width: '100%',
            maxWidth: '350px',
            borderRadius: '5px',
            border: '1px solid #ccc',
            fontSize: '16px'
          }}
        />
      </div>

      {isLoading && <p style={{ fontSize: '18px', color: '#555' }}>Cargando productos...</p>}

      {!isLoading && error && (
        <div style={{ color: '#d9534f', padding: '15px', border: '1px solid #d9534f', borderRadius: '5px', backgroundColor: '#fdf7f7' }}>
          <p style={{ margin: 0 }}><strong>Error:</strong> {error}</p>
        </div>
      )}

      {!isLoading && !error && productos.length === 0 && (
        <p style={{ color: '#777', fontStyle: 'italic' }}>No se encontraron productos que coincidan con la búsqueda.</p>
      )}

      {!isLoading && !error && productos.length > 0 && (
        <>
          <div style={{ display: 'grid', gridTemplateColumns: 'repeat(auto-fit, minmax(250px, 1fr))', gap: '20px' }}>
            {productos.map((prod) => (
              <ProductCard key={prod.id} producto={prod} />
            ))}
          </div>

          {/* Paso 3: Botones de Paginación */}
          <div style={{ marginTop: '30px', display: 'flex', gap: '15px', alignItems: 'center' }}>
            <button
              onClick={() => setPage((prev) => Math.max(prev - 1, 0))}
              disabled={page === 0}
              style={{ padding: '8px 16px', cursor: page === 0 ? 'not-allowed' : 'pointer' }}
            >
              « Anterior
            </button>

            <span>Página {page + 1}</span>

            <button
              onClick={() => setPage((prev) => prev + 1)}
              disabled={productos.length < limit}
              style={{ padding: '8px 16px', cursor: productos.length < limit ? 'not-allowed' : 'pointer' }}
            >
              Siguiente »
            </button>
          </div>
        </>
      )}
    </div>
  );
}

export default App;