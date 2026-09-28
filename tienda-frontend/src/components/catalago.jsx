import React, { useState, useEffect } from "react";
import { getProductos } from "../services/api";

export function Catalogo() {
    const [productos, setProductos] = useState([]);
    const [error, setError] = useState("");

    useEffect(() => {
        async function cargarProductos() {
            try {
                const data = await getProductos();
                // Si el backend devuelve un objeto paginado con .items o una lista directa:
                setProductos(Array.isArray(data) ? data : data.items || []);
            } catch (err) {
                setError("Error al cargar los productos del catálogo.");
            }
        }
        cargarProductos();
    }, []);

    return (
        <div style={{ maxWidth: "800px", margin: "0 auto", padding: "20px" }}>
            <h2>Catálogo de Productos</h2>
            {error && <p style={{ color: "red" }}>{error}</p>}
            <div style={{ display: "grid", gridTemplateColumns: "repeat(auto-fill, minmax(200px, 1fr))", gap: "20px", marginTop: "20px" }}>
                {productos.map((prod) => (
                    <div key={prod.id} style={{ border: "1px solid #ddd", borderRadius: "8px", padding: "15px", textAlign: "center" }}>
                        <h3>{prod.nombre}</h3>
                        <p>{prod.descripcion}</p>
                        <p><strong>${prod.precio}</strong></p>
                        <p style={{ fontSize: "12px", color: "#666" }}>Stock: {prod.stock}</p>
                    </div>
                ))}
            </div>
        </div>
    );
}