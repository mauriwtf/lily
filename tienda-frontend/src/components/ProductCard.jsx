export default function ProductCard({ producto }) {
  return (
    <div style={{ border: '1px solid #ccc', padding: '16px', borderRadius: '8px', background: '#fff' }}>
      <h3 style={{ marginTop: 0 }}>{producto.nombre}</h3>
      <p><strong>Precio final:</strong> ${producto.precio_final}</p>
      <p><strong>Financiación:</strong> {producto.cuotas_cantidad} cuotas de ${producto.cuotas_valor}</p>
      <p><strong>Garantía:</strong> {producto.garantia_meses} mes(es)</p>
    </div>
  );
}